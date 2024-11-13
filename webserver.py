from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from encryption import Steganography
from Database import Database
import logging
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

# Initialize the database connection
user = os.getenv("DB2_USER")
password = os.getenv("DB2_PASSWORD")
host = os.getenv("DB2_HOST", "localhost")
dbname = os.getenv("DB2_NAME")

db = Database(user=user, password=password, host=host, dbname=dbname)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/create-account', methods=['POST'])
def create_account():
    data = request.json
    username = data['username']
    full_name = data['full_name']
    password = data['password']
    try:
        logging.debug(f"Creating account for username: {username}, full_name: {full_name}")
        db.saveCredentials(username, full_name, password)
        return jsonify({'message': 'Account created successfully'}), 201
    except Exception as e:
        logging.error(f"Error creating account: {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    if db.validatePassword(username, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/encode', methods=['POST'])
def encode():
    if 'image' not in request.files or 'secret_message' not in request.form:
        return jsonify({'error': 'Image file and secret message are required'}), 400

    image_file = request.files['image']
    secret_message = request.form['secret_message']

    os.makedirs('temp', exist_ok=True)  # Ensure the temp directory exists
    input_image_path = f'temp/{image_file.filename}'
    image_file.save(input_image_path)

    output_image_path = 'encoded_image.png'

    try:
        Steganography.encrypt_message(input_image_path, output_image_path, secret_message)
        return jsonify({'message': 'Message hidden and saved in image', 'encoded_image_path': output_image_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/encoded_image.png')
def get_encoded_image():
    return send_from_directory('.', 'encoded_image.png', as_attachment=True)

@app.route('/api/decode', methods=['POST'])
def decode():
    if 'image' not in request.files:
        return jsonify({'error': 'Image file is required'}), 400

    image_file = request.files['image']

    # Save the uploaded image temporarily
    os.makedirs('temp', exist_ok=True)
    input_image_path = f'temp/{image_file.filename}'
    image_file.save(input_image_path)

    try:
        # Decode the hidden message
        secret_message = Steganography.decrypt_message(input_image_path)
        logging.debug(f"Decoded message (raw): {repr(secret_message)}")  # Log as repr to see exact value

        if not secret_message:
            # Handle case where no message is found in the image
            logging.warning("No hidden message found.")
            return jsonify({'error': 'No hidden message found in the image.'}), 400

        # Save the decoded message to a text file
        output_text_path = 'temp/decoded_message.txt'
        with open(output_text_path, 'w') as file:
            file.write(secret_message)

        return jsonify({
            'secret_message': secret_message,
            'output_text_path': output_text_path
        }), 200
    except Exception as e:
        logging.error(f"Error during decoding: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/temp/<filename>')
def get_temp_file(filename):
    return send_from_directory('temp', filename, as_attachment=True)

@app.route('/api/save-image', methods=['POST'])
def save_image():
    data = request.json
    username = data['username']
    image_name = data['image_name']
    image_data = data['image_data']  # Assuming image_data is base64 encoded

    try:
        db.saveImage(username, image_name, image_data)
        return jsonify({'message': 'Image saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/retrieve-image', methods=['POST'])
def retrieve_image():
    data = request.json
    username = data['username']
    image_name = data['image_name']

    try:
        image_data = db.retrieveImage(username, image_name)
        if image_data:
            return jsonify({'image_data': image_data}), 200
        else:
            return jsonify({'error': 'Image not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
