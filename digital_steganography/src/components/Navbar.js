import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const navigate = useNavigate();

  // Check if the user is logged in when the component mounts
  useEffect(() => {
    // Check if user information is stored in local storage (or another way you track login state)
    const user = localStorage.getItem('user');
    if (user) {
      setIsLoggedIn(true);
    }
  }, []);

  // Handle logging out
  const handleLogout = () => {
    // Clear user information (or token) from localStorage
    localStorage.removeItem('user');
    setIsLoggedIn(false);
    navigate('/homepage'); // Redirect to login page after logging out
  };

  return (
    <header className="navbar">
      <div className="navbar-brand">
        <img src="/Images/Logo.png" alt="Logo" />
        <h1>
          <span className="brand-s">S</span>teg
          <span className="brand-s">S</span>ecure
        </h1>
      </div>
      <div className="navbar-main">
        <nav className="navbar-menu">
          <ul className="navbar-links">
            <li><Link to="/homepage">Home</Link></li>
            <li><Link to="/encodedata">Encode Data</Link></li>
            <li><Link to="/decodedata">Decode Data</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/help">Help</Link></li>
          </ul>
        </nav>
        <div className="navbar-login">
          {isLoggedIn ? (
            <button onClick={handleLogout} className="login-btn">Sign Out</button>
          ) : (
            <Link to="/login" className="login-btn">Login</Link>
          )}
        </div>
      </div>
    </header>
  );
};

export default Navbar;
