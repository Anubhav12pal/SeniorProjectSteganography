import React from 'react';
import './Login.css';
import { Link } from 'react-router-dom';

const Login = () => {
  return (
    <div className="login-container">
      <div className="login-box">
        <div className="login-header">
          <img src="Images/Logo.png" alt="Invooce Logo" className="logo" />
        </div>
        <h2>Login</h2>
        <p>Hi, Welcome back 👋</p>
        <form>
          <label htmlFor="email">Email</label>
          <input type="email" id="email" placeholder="E.g. johndoe@email.com" required />
          
          <label htmlFor="password">Password</label>
          <div className="password-container">
            <input type="password" id="password" placeholder="Enter your password" required />
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

        <p className="register-text">
          Not registered yet? <Link to="/create-account" className="register-link">Create an account</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
