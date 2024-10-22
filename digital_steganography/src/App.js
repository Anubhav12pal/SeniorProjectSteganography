// src/App.js
import React from 'react';
import Navbar from './components/Navbar.js';
import Footer from './components/Footer.js';
import HomePage from './components/HomePage.js';
import AboutPage from './components/AboutPage.js';
import EncodePage from './components/EncodePage.js';
import DecodePage from './components/DecodePage.js';
import HelpPage from './components/HelpPage.js';
import LoginPage from './components/Login.js';
import ForgotPassword from './components/ForgotPassword.js';
import CreateAccount from './components/CreateAccount.js';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/encodedata" element={<EncodePage />} />
          <Route path="/decodedata" element={<DecodePage />} />
          <Route path="/help" element={<HelpPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/create-account" element={<CreateAccount />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
