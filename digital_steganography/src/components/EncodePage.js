// src/components/EncodePage.js
import React, { useState } from 'react';
import './EncodePage.css';

const EncodePage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [secretMessage, setSecretMessage] = useState('');

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(URL.createObjectURL(file));
    }
  };

  const handleMessageChange = (e) => {
    setSecretMessage(e.target.value);
  };

  const handleEncode = () => {
    if (selectedImage && secretMessage) {
      // Perform the LSB encoding logic here
      alert("Encoding the message...");
    } else {
      alert("Please select an image and enter a secret message.");
    }
  };

  return (
    <div className="encode-container">
      <h1>Encode Data</h1>
      <p>Select an image and enter the secret message to hide.</p>

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
        <label htmlFor="message-input" className="form-label">Enter Secret Message:</label>
        <textarea id="message-input" value={secretMessage} onChange={handleMessageChange} placeholder="Enter your message here..." />
      </div>

      <button onClick={handleEncode} className="encode-btn">Encode Message</button>
    </div>
  );
};

export default EncodePage;
