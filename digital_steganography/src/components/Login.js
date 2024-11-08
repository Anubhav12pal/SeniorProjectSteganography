import React, { useState } from 'react';
import './Login.css';
import { Link, useNavigate } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Clear any previous error messages

    try {
      const response = await fetch('http://127.0.0.1:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: email, password }),
      });

      // Check for successful login
      if (response.ok) {
        const data = await response.json();
        console.log(data.message);

        // Store session data and navigate
        localStorage.setItem('user', JSON.stringify({ email }));
        navigate('/homepage');
      } else if (response.status === 401) {
        // Unauthorized - Invalid credentials
        setError('Invalid credentials. Please try again.');
      } else {
        // Unexpected error
        const errorData = await response.json();
        setError(errorData.error || 'An unexpected error occurred.');
      }
    } catch (err) {
      setError('An error occurred. Please check your network connection and try again.');
      console.error(err);
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <div className="login-header">
          <img src="Images/Logo.png" alt="Invooce Logo" className="logo" />
        </div>
        <h2>Login</h2>
        <p>Hi, Welcome back 👋</p>
        <form onSubmit={handleSubmit}>
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
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <span className="password-icon"></span>
          </div>

          <div className="form-options">
            <div>
              <input type="checkbox" id="remember-me" />
              <label htmlFor="remember-me">Remember Me</label>
            </div>
            <Link to="/forgot-password" className="forgot-password">Forgot Password?</Link>
          </div>

          <button type="submit" className="custom-login-btn">Login</button>
        </form>

        {error && <p className="error-text">{error}</p>}

        <p className="register-text">
          Not registered yet? <Link to="/create-account" className="register-link">Create an account</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
