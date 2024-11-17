// src/components/DecodePage.js
import React, { useState } from 'react';
import './DecodePage.css';

const DecodePage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [decodedMessage, setDecodedMessage] = useState('');

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file); // Save the selected file
    }
  };

  const handleDecode = async () => {
  if (selectedImage) {
    const formData = new FormData();
    formData.append('image', selectedImage);

    try {
      const response = await fetch("http://127.0.0.1:5000/api/decode", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setDecodedMessage(data.secret_message); // Display the decoded message
        console.log(`Decoded message saved at: ${data.output_text_path}`);
      } else {
        const errorData = await response.json();
        alert(`Error: ${errorData.error}`); // Show error messages returned by the backend
      }
    } catch (error) {
      console.error("Decoding error:", error);
      alert("An error occurred. Please try again.");
    }
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
          <img src={URL.createObjectURL(selectedImage)} alt="Selected" />
        </div>
      )}

      <button onClick={handleDecode} className="decode-btn">Decode Message</button>

      {decodedMessage && (
        <div className="decoded-message">
          <h3>Decoded Message:</h3>
          <p>{decodedMessage}</p>
          <a
            href="http://127.0.0.1:5000/temp/decoded_message.txt"
            download="decoded_message.txt"
          >
            Download Decoded Message
          </a>
        </div>
      )}
    </div>
  );
};

export default DecodePage;
