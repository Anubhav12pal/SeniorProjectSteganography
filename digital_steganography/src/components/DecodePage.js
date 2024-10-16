// src/components/DecodePage.js
import React, { useState } from 'react';
import './DecodePage.css';

const DecodePage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [decodedMessage, setDecodedMessage] = useState('');

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(URL.createObjectURL(file));
    }
  };

  const handleDecode = () => {
    if (selectedImage) {
      // LSB decoding logic here
      setDecodedMessage("This is a decoded message!"); // Placeholder for the decoded message
    } else {
      alert("Please select an image to decode.");
    }
  };

  return (
    <div className="decode-container">
      <h1>Decode Data</h1>
      <p>Upload an image with hidden data to extract the secret message.</p>

      <div className="form-group">
        <label>Select Image:</label>
        <input type="file" accept="image/*" onChange={handleImageChange} />
      </div>

      {selectedImage && (
        <div className="preview">
          <h3>Image Preview:</h3>
          <img src={selectedImage} alt="Selected" />
        </div>
      )}

      <button onClick={handleDecode} className="decode-btn">Decode Message</button>

      {decodedMessage && (
        <div className="decoded-message">
          <h3>Decoded Message:</h3>
          <p>{decodedMessage}</p>
        </div>
      )}
    </div>
  );
};

export default DecodePage;
