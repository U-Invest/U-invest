import React from 'react';
import "./Login.css";
import { useState } from 'react';

const Login = () => {
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Username:", username);
    console.log("Email:", email);
    console.log("Password:", password);
  };

  return (

    // Container da caixa de cadastro
    <div className="signup-container">
      <form onSubmit={handleSubmit}>
        <h1>Login</h1>


        {/* Input do email */}
        <div className="input-group">
          <label htmlFor="email">Username:</label>
          <input
            type="email"
            id="email"
            placeholder="  Digite seu e-mail ou username:"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>

        <div className="input-group">
          <label htmlFor="email">Senha:</label>
          <input
            type="email"
            id="email"
            placeholder="  Digite sua senha: "
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>


        <button type="submit">Login</button>

      </form>
    </div>
  );
};
export default Login;