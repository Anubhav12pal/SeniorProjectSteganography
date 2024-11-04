import React, { useState } from 'react'; // Import useState for managing component state
import './Login.css';
import { Link, useNavigate } from 'react-router-dom';

const Login = () => {
  // Define state variables for email, password, and error message
  const [email, setEmail] = useState(''); 
  const [password, setPassword] = useState(''); 
  const [error, setError] = useState(''); 

  const navigate = useNavigate(); // To handle navigation after successful login

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: email, password }), // Send the email as username
      });

      if (response.status === 200) {
        // On successful login, save the user data to localStorage and navigate to a different route
        const data = await response.json();
        console.log(data.message); 
        localStorage.setItem('user', JSON.stringify({ email })); // Save user session

        navigate('/homepage');
      } else {
        // Handle unsuccessful login attempts
        setError('Invalid credentials. Please try again.');
      }
    } catch (err) {
      // Handle error cases
      setError('An error occurred. Please try again.');
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

        {error && <p className="error-text">{error}</p>} {/* Display error message if there is any */}

        <p className="register-text">
          Not registered yet? <Link to="/create-account" className="register-link">Create an account</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;