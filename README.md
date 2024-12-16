# Digital Steganography Project

This project demonstrates a digital steganography application that allows users to encode and decode messages within images. The project consists of a React frontend, a Flask backend, and a PostgreSQL database. It supports both 1-bit and 2-bit encryption techniques, and includes a comparison of Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR) for these methods.

## Table of Contents

- Project Overview
- Setup Instructions
  - React Frontend Setup
  - Python Backend Setup
  - PostgreSQL Database Setup
  - Integration Using Flask
- White Paper Summary
- License

## Project Overview

The digital steganography project allows users to securely encode and decode messages within images. The project is divided into three main components:

1. **React Frontend**: Provides the user interface for encoding and decoding messages.
2. **Python Backend**: Handles the steganography logic and interacts with the database.
3. **PostgreSQL Database**: Stores user credentials and images.

The application supports both 1-bit and 2-bit encryption techniques. Users can input an image and a text message, which the app will encode into the image. The encoded image can then be decoded to retrieve the hidden message.

## Setup Instructions

### React Frontend Setup

1. **Navigate to the frontend directory**:

   ```sh
   cd digital_steganography
   ```

2. **Install dependencies**:

   ```sh
   npm install
   ```

3. **Start the development server**:
   ```sh
   npm start
   ```

The React application will be available at `http://localhost:3000`.

### Python Backend Setup

1. **Create a virtual environment**:

   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set environment variables**:
   Create a `.env` file in the root directory and add the following:

   ```env
   DB2_USER=<your_db_user>
   DB2_PASSWORD=<your_db_password>
   DB2_HOST=<your_db_host>
   DB2_NAME=<your_db_name>
   ```

5. **Run the Flask server**:
   ```sh
   python webserver.py
   ```

The Flask backend will be available at `http://127.0.0.1:5000`.

### PostgreSQL Database Setup

1. **Install PostgreSQL**:
   Follow the instructions on the [official PostgreSQL website](https://www.postgresql.org/download/) to install PostgreSQL on your system.

2. **Create a new database**:

   ```sh
   createdb <your_db_name>
   ```

3. **Create a new user and grant privileges**:

   ```sql
   CREATE USER <your_db_user> WITH PASSWORD '<your_db_password>';
   GRANT ALL PRIVILEGES ON DATABASE <your_db_name> TO <your_db_user>;
   ```

4. **Initialize the database schema**:
   The `Database` class in [Database.py](http://_vscodecontentref_/0) will automatically create the necessary tables when the Flask server is started.

### Integration Using Flask

The Flask backend integrates the React frontend and PostgreSQL database using the following steps:

1. **CORS Configuration**:
   The Flask app is configured to allow cross-origin requests from the React frontend:

   ```py
   from flask_cors import CORS
   CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
   ```

2. **API Endpoints**:
   The backend provides several API endpoints for user authentication and steganography operations:

   - `/api/create-account`: Create a new user account.
   - `/api/login`: Authenticate a user.
   - `/api/encode`: Encode a message within an image.
   - `/api/decode`: Decode a message from an image.

3. **Database Interaction**:
   The `Database` class handles interactions with the PostgreSQL database, including creating tables, saving credentials, and storing/retrieving images.

## White Paper Summary

The white paper provides an in-depth explanation of the digital steganography techniques used in this project. It covers the following topics:

- **Introduction to Steganography**: An overview of steganography and its applications.
- **Encoding and Decoding Algorithms**: Detailed descriptions of the algorithms used to encode and decode messages within images.
- **1-bit and 2-bit Encryption**: Explanation of the 1-bit and 2-bit encryption techniques and their comparison.
- **MSE and PSNR Comparison**: Analysis of the Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR) for the different encryption methods.
- **Security Considerations**: Discussion of the security measures implemented to protect encoded messages.
- **Performance Analysis**: Evaluation of the performance of the steganography algorithms.

---

For more information, please refer to the white paper and the project documentation.
