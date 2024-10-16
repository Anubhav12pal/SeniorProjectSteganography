// src/components/HomePage.js
import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

const HomePage = () => {
  return (
    <div className="home-container">
      <section className="hero">
        <div className="hero-content">
          <h1>Welcome to StegSecure</h1>
          <p>Hide your secrets securely using image steganography with the power of Least Significant Bit (LSB) encoding.</p>
          <div className="cta-buttons">
            <Link to="/encodedata" className="btn">Start Encoding</Link>
            <Link to="/decodedata" className="btn btn-secondary">Start Decoding</Link>
          </div>
        </div>
      </section>

      <section className="info-section">
        <h2>What is Steganography?</h2>
        <p>
          Steganography is the practice of concealing messages or information within other non-secret text or data. With StegSecure, 
          you can hide your data within images using the LSB method, where the least significant bits of image pixels are modified to 
          contain your secret information.
        </p>
      </section>

      <section className="demo-section">
        <h2>How it Works</h2>
        <div className="demo-content">
          <p>1. Select an image.</p>
          <p>2. Input the text or file you want to hide.</p>
          <p>3. Click "Encode" to hide the data in the image.</p>
          <p>4. To retrieve hidden data, upload the image and click "Decode."</p>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
