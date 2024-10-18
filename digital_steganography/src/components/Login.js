import React, { useState } from 'react';
import './Login.css';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Username:', username);
    console.log('Password:', password);
  };

  return (
    <div className="login-page" style={{ height: "100vh", display: "flex", justifyContent: "center", alignItems: "center" }}>
      <div className="login-container" style={{ textAlign: "center" }}>
        <h1>Log in to Your Account!</h1>
        <form onSubmit={handleSubmit} style={{ height: "90vh", display: "flex", flexDirection: "column", alignItems: "center" }}>
            <div style={{ display: "flex", flexDirection: "column", width: "250px" }}>
            <input
              type="username"
              name="username"
              placeholder="Enter username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              style={{ margin: "10px", height: "20px", fontSize: "16px" }}
            />
            <input
              type="password"
              name="password"
              placeholder="Enter password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              style={{ margin: "10px", height: "20px", fontSize: "16px" }}
            />
          </div>
            <button type="submit" style={{ marginTop: "20px", padding: "10px 20px", fontSize: "16px" }}>
                Login
            </button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;