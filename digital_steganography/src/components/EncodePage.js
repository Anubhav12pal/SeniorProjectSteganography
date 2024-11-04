import React, { useState } from 'react';
import './EncodePage.css';

const EncodePage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [secretMessage, setSecretMessage] = useState('');

  // Function to handle image upload
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
    }
  };

  // Function to handle text file upload and read its contents
  const handleTextFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setSecretMessage(event.target.result);
      };
      reader.readAsText(file);
    }
  };

  // Function to handle encoding logic
  const handleEncode = async () => {
    if (selectedImage && secretMessage) {
      // Prepare the form data to send to the backend
      const formData = new FormData();
      formData.append('image', selectedImage); // Attach the image file
      formData.append('secret_message', secretMessage); // Attach the secret message

      try {
        // Send the form data to the backend
        const response = await fetch("http://127.0.0.1:5000/api/encode", {
          method: "POST",
          body: formData // Pass FormData directly without headers
        });

        if (response.ok) {
          alert('Message successfully encoded in the image.');
        } else {
          const errorData = await response.json();
          alert(`Error: ${errorData.error}`);
        }
      } catch (error) {
        console.error('Encoding error:', error);
        alert('An error occurred. Please try again.');
      }
    } else {
      alert('Please select an image and upload a text file with a secret message.');
    }
  };

  return (
    <div className="encode-container">
      <h1>Encode Data</h1>
      <p>Select an image and upload a text file to hide the secret message.</p>

      <div className="form-group">
        <label htmlFor="image-upload" className="form-label">Select Image:</label>
        <input type="file" id="image-upload" accept="image/*" onChange={handleImageChange} />
      </div>

      {selectedImage && (
        <div className="preview">
          <h3>Image Preview:</h3>
          <img src={URL.createObjectURL(selectedImage)} alt="Selected" />
        </div>
      )}

      <div className="form-group">
        <label htmlFor="text-upload" className="form-label">Upload Text File:</label>
        <input type="file" id="text-upload" accept=".txt" onChange={handleTextFileChange} />
      </div>

      {secretMessage && (
        <div className="message-preview">
          <h3>Text Preview:</h3>
          <textarea value={secretMessage} readOnly />
        </div>
      )}

      <button onClick={handleEncode} className="encode-btn">Encode Message</button>
    </div>
  );
};

export default EncodePage;