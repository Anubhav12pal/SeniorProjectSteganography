// src/components/AboutPage.js
import React from 'react';
import './AboutPage.css';

const AboutPage = () => {
  return (
    <div className="about-container">
      <section className="about-header">
        <h1>About StegSecure</h1>
        <p>Your go-to solution for securely hiding sensitive information within images using LSB steganography.</p>
      </section>

      <section className="about-content">
        <div className="about-section">
          <h2>What We Do</h2>
          <p>
            StegSecure provides an easy-to-use platform that allows users to hide data within images using 
            Least Significant Bit (LSB) steganography. Whether you need to hide personal messages, documents, or files, 
            our tool helps ensure your information remains confidential and undetectable by normal viewers.
          </p>
        </div>

        <div className="about-section">
          <h2>How It Works</h2>
          <p>
            Steganography is the art of hiding data within another file—in our case, images. LSB steganography works 
            by embedding the secret data in the least significant bits of image pixels, altering them just enough to 
            store the data without making noticeable changes to the image. This technique ensures that your data remains 
            hidden and secure.
          </p>
        </div>

        <div className="about-section">
          <h2>Our Mission</h2>
          <p>
            Our mission is to provide individuals and organizations with a secure and easy way to hide sensitive data 
            in plain sight. In an age where privacy is crucial, we aim to simplify data security through steganography, 
            making it accessible to everyone.
          </p>
        </div>

        <div className="about-section">
          <h2>Why Steganography?</h2>
          <p>
            Steganography offers an additional layer of security for transmitting confidential information, as it 
            hides data in a way that is undetectable by unauthorized viewers. Unlike encryption, which is often 
            recognizable, steganography hides the existence of the hidden data entirely.
          </p>
        </div>
      </section>
    </div>
  );
};

export default AboutPage;
