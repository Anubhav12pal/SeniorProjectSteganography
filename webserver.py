from flask import Flask, request, jsonify
from flask_cors import CORS
from encryption import Steganography
from Database import Database
import logging
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
    data = request.json
    input_image_path = data['input_image_path']
    output_image_path = data['output_image_path']
    secret_message = data['secret_message']
    
    try:
        Steganography.encrypt_message(input_image_path, output_image_path, secret_message)
        return jsonify({'message': 'Message hidden and saved in image'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/decode', methods=['POST'])
def decode():
    data = request.json
    encoded_image_path = data['encoded_image_path']
    
    try:
        secret_message = Steganography.decrypt_message(encoded_image_path)
        return jsonify({'secret_message': secret_message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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