import React from 'react';
import './ForgotPassword.css';

const ForgotPassword = () => {
  return (
    <div className="forgot-password-container">
      <div className="forgot-password-box">
        <div className="forgot-password-header">
          <img src="Images/Logo.png" alt="Invooce Logo" className="logo" />
        </div>
        <h2>Forgot Password</h2>
        <p>Enter your email to reset your password 👇</p>
        <form>
          <label htmlFor="email">Email</label>
          <input type="email" id="email" placeholder="E.g. johndoe@email.com" required />

          <button type="submit" className="custom-reset-btn">Reset Password</button>
        </form>

        <p className="back-to-login">
          Remembered your password? <a href="login" className="login-link">Go back to login</a>
        </p>
      </div>
    </div>
  );
};

export default ForgotPassword;
