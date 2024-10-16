// src/components/HelpPage.js
import React, { useState } from 'react';
import './HelpPage.css';

const HelpPage = () => {
  return (
    <div className="help-container">
      <h1>Help & Support</h1>

      <section className="help-section">
        <h2>How to Use StegSecure</h2>
        <p>StegSecure allows you to hide secret data in images using the Least Significant Bit (LSB) steganography technique. Below are the steps for encoding and decoding data.</p>
      </section>

      <section className="help-section">
        <h3>1. Encoding Data (Hiding Data)</h3>
        <ol>
          <li>Go to the <strong>Encode Data</strong> page.</li>
          <li>Upload the image you want to use for hiding your data.</li>
          <li>Enter the secret message or select the file you want to hide.</li>
          <li>Click the <strong>Encode</strong> button to hide your message in the image.</li>
          <li>Download the new image that now contains your hidden data.</li>
        </ol>
        <p><em>Note:</em> Make sure the image is large enough to hide the amount of data you're trying to encode. The more data you hide, the more the image quality can degrade.</p>
      </section>

      <section className="help-section">
        <h3>2. Decoding Data (Extracting Hidden Data)</h3>
        <ol>
          <li>Go to the <strong>Decode Data</strong> page.</li>
          <li>Upload the image that contains hidden data.</li>
          <li>Click the <strong>Decode</strong> button to reveal the hidden message or file.</li>
          <li>The hidden message will be displayed on the page, or the hidden file will be available for download.</li>
        </ol>
        <p><em>Tip:</em> Make sure you upload the exact image that was used for encoding, otherwise the decoding process will fail.</p>
      </section>

      <section className="help-section">
        <h2>Frequently Asked Questions (FAQ)</h2>

        <h3>Q1: What is steganography?</h3>
        <p>Steganography is the practice of hiding a secret message or file within another non-secret file. In the case of StegSecure, we hide data in images using a technique called Least Significant Bit (LSB) steganography.</p>

        <h3>Q2: What is LSB steganography?</h3>
        <p>Least Significant Bit (LSB) steganography is a technique where the least significant bit of each pixel in an image is altered to store secret data. Since the change is minimal, it is difficult for the human eye to detect the difference in the image.</p>

        <h3>Q3: How much data can I hide in an image?</h3>
        <p>The amount of data you can hide in an image depends on the size of the image. Larger images can store more data. However, the more data you hide, the more the image may degrade in quality.</p>

        <h3>Q4: Is there any limit to the file size for encoding?</h3>
        <p>Yes, the size of the file you can encode is limited by the image size and format. High-resolution images can store more data, but if the image is too small, there might not be enough capacity to hide large files.</p>

        <h3>Q5: Is my hidden data secure?</h3>
        <p>Steganography provides a layer of security by hiding the existence of data, but it is recommended to encrypt your data before encoding it in an image for enhanced security.</p>
      </section>

      <section className="help-section">
        <h2>Contact Support</h2>
        <p>If you have any questions or need further assistance, please contact us at <a href="mailto:support@stegsecure.com">support@stegsecure.com</a>.</p>
      </section>
    </div>
  );
};

export default HelpPage;
