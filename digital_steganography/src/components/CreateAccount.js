import React, { useState } from 'react';
import './CreateAccount.css';

const CreateAccount = () => {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('Form submitted');

    if (password !== confirmPassword) {
      setMessage('Passwords do not match');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/api/create-account', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: email, full_name: fullName, password }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error:', errorText);
        setMessage('An error occurred. Please try again.');
        return;
      }

      const data = await response.json();
      setMessage(data.message || data.error);
    } catch (error) {
      console.error('Error:', error);
      setMessage('An error occurred. Please try again.');
    }
  };

  return (
    <div className="create-account-container">
      <div className="create-account-box">
        <div className="create-account-header">
          <img src="Images/Logo.png" alt="Invooce Logo" className="logo" />
        </div>
        <h2>Create Account</h2>
        <p>Join us and manage your tasks effortlessly 👋</p>
        <form onSubmit={handleSubmit}>
          <label htmlFor="full-name">Full Name</label>
          <input
            type="text"
            id="full-name"
            placeholder="Enter your full name"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            required
          />

          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            placeholder="E.g. johndoe@email.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          
          <label htmlFor="password">Password</label>
          <div className="password-container">
            <input
              type="password"
              id="password"
              placeholder="Enter a secure password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <span className="password-icon"></span>
          </div>

          <label htmlFor="confirm-password">Confirm Password</label>
          <div className="password-container">
            <input
              type="password"
              id="confirm-password"
              placeholder="Re-enter your password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
            <span className="password-icon"></span>
          </div>

          <button type="submit" className="custom-create-btn">Create Account</button>
        </form>

        {message && <p className="message">{message}</p>}

        <p className="login-text">
          Already have an account? <a href="login" className="login-link">Login here</a>
        </p>
      </div>
    </div>
  );
};

export default CreateAccount;