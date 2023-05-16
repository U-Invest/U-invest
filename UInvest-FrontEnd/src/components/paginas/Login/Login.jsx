import React from 'react';
import "./Login.css";
import { useState } from 'react';
import { fazerLogin } from '../../../Data';

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    let usuario = {
      email: email,
      password: password,
    };

    fazerLogin(usuario)
      .then(data => {
        // Tratar a resposta da solicitação GET
        console.log(data);
      })
      .catch(error => {
        // Lidar com erros, se houver
        console.error(error);
      });
 


    event.preventDefault();
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Usuario: ", usuario)
  };

  return (

    // Container da caixa de cadastro
    <div className="login-container">
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
          <label htmlFor="password">Senha:</label>
          <input
            type="password"
            id="password"
            placeholder="  Digite sua senha: "
            value={password}
            onChange={(event) => setPassword(event.target.value)}
         />
        </div>


        <button type="submit">Login</button>

      </form>
    </div>
  );
};
export default Login;