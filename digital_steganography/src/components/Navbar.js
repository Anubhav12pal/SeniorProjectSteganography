import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
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
            <li><Link to="/">Home</Link></li>
            <li><Link to="/encodedata">Encode Data</Link></li>
            <li><Link to="/decodedata">Decode Data</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/help">Help</Link></li>
          </ul>
        </nav>
        <div className="navbar-login">
          <Link to="/login" className="login-btn">Login</Link>
        </div>
      </div>
    </header>
  );
};

export default Navbar;
