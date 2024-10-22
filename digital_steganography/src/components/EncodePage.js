// src/components/EncodePage.js
import React, { useState } from 'react';
import './EncodePage.css';

const EncodePage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [secretMessage, setSecretMessage] = useState('');

  // Function to handle image upload
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(URL.createObjectURL(file));
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
  const handleEncode = () => {
    if (selectedImage && secretMessage) {
      // Perform the LSB encoding logic here
      alert("Encoding the message...");
    } else {
      alert("Please select an image and upload a text file with a secret message.");
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
          <img src={selectedImage} alt="Selected" />
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
