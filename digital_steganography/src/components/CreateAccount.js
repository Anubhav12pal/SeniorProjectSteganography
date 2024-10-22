import React from 'react';
import './CreateAccount.css';

const CreateAccount = () => {
  return (
    <div className="create-account-container">
      <div className="create-account-box">
        <div className="create-account-header">
          <img src="Images/Logo.png" alt="Invooce Logo" className="logo" />
        </div>
        <h2>Create Account</h2>
        <p>Join us and manage your tasks effortlessly 👋</p>
        <form>
          <label htmlFor="full-name">Full Name</label>
          <input type="text" id="full-name" placeholder="Enter your full name" required />

          <label htmlFor="email">Email</label>
          <input type="email" id="email" placeholder="E.g. johndoe@email.com" required />
          
          <label htmlFor="password">Password</label>
          <div className="password-container">
            <input type="password" id="password" placeholder="Enter a secure password" required />
            <span className="password-icon"></span>
          </div>

          <label htmlFor="confirm-password">Confirm Password</label>
          <div className="password-container">
            <input type="password" id="confirm-password" placeholder="Re-enter your password" required />
            <span className="password-icon"></span>
          </div>

          <button type="submit" className="custom-create-btn">Create Account</button>
        </form>

        <p className="login-text">
          Already have an account? <a href="login" className="login-link">Login here</a>
        </p>
      </div>
    </div>
  );
};

export default CreateAccount;
