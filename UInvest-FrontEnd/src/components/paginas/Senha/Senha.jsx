import React from "react";
import "./Senha.css";

function ForgotPassword() {
  return (
    <div className="container-password">
      <h1 className="password-h1">Esqueci Minha Senha</h1>
      <div className="email-password">
          <label htmlFor="email"></label>
          <input
            type="text"
            id="email"
            placeholder="Digite seu e-mail"
            // value={email}
            // onChange={(event) => setEmail(event.target.value)}
          />
          <button className="button-forgot-password">Enviar</button>
        </div>
      <p className="password-p">Um e-mail será enviado para a sua caixa de correspondência. Obrigado por utilizar o nosso site!</p>
    </div>
  );
}

export default ForgotPassword;
