import React from "react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import 'react-toastify/dist/ReactToastify.min.css';
import { Link } from "react-router-dom";
import "./Cadastro.css";
import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheck } from "@fortawesome/free-solid-svg-icons";
import background from "../../../assets/login-page.svg"


const Cadastro = () => {
  const [termsChecked, setTermsChecked] = useState(false);
  const [name, setName] = useState("");
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [birthdate, setBirthdate] = useState("");
  const [phone, setPhone] = useState("");
  const [profileType, setProfileType] = useState("not-investor");
  const [CPF, setCPF] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handlePerfilChange = (event) => {
    setProfileType(event.target.value);
  };

  const parts = birthdate.split("-");
  const birthdateFormatted = `${parts[2]}${parts[1]}${parts[0]}`;
  
  
  let usuario = {
    cpf: CPF,
    email: email,
    celular: phone,
    nome: name,
    saldo: 0,
    senha: password,
    perfil_investidor: profileType,
    nickName: username,
    nascimento: birthdateFormatted,
  };

  const handleTermsChange = (event) => {
    setTermsChecked(event.target.checked);
  };
  
  const handleSubmit = (event) => {
    event.preventDefault();

    if (!termsChecked) {
      setError("Por favor, aceite os termos e condições.");
      return;
    }

    setLoading(true);
    setError("");


    fetch(`http://localhost:8080/UInvest/usuario`, {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(usuario),
    })
      .then(() => {
        toast.success("Cadastro feito com sucesso!");
        setTimeout(() => {
          window.location = "/login";
        }, 2000);
      })
      .catch((error) => {
        setError("Ocorreu um erro ao cadastrar. Por favor, tente novamente.");
        console.error(error); 
      })
      .finally(() => {
        setLoading(false);
      });
  };
  
  return (
    // Container da caixa de cadastro
      
      <div className="signup-container background-image">
        <div className="form-wrapper">
        {loading && <div className="loading-indicator">Carregando...</div>} {/* Exibe o indicador de carregamento se o estado de carregamento for true */}
        {error && <div className="error-message">{error}</div>}
        <ToastContainer />
        <form className="signup-form" onSubmit={handleSubmit}>
            <h1>Cadastre-se</h1>

            {/* Input do nome */}
            <div className="name-inputgroup">
              <label htmlFor="name">Nome completo:</label>
              <input
                type="name"
                id="name"
                placeholder="Digite seu nome:"
                value={name}
                onChange={(event) => setName(event.target.value)}
              />
            </div>

            {/* Input do username */}
            <div className="username-inputgroup">
              <label htmlFor="name">Username:</label>
              <input
                type="name"
                id="username"
                placeholder="Digite seu username:"
                value={username}
                onChange={(event) => setUserName(event.target.value)}
              />
            </div>

            {/* Input do email */}
            <div className="email-inputgroup">
              <label htmlFor="email">Email:</label>
              <input
                type="email"
                id="email"
                placeholder="Digite seu e-mail: "
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            </div>

            <div className="password-inputgroup">
              <label htmlFor="password">Senha:</label>
              <input
                type="password"
                id="password"
                placeholder="Digite sua senha: "
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </div>

            <div className="confirm-password-inputgroup">
              <label htmlFor="confirmPassword">Confirme:</label>
              <input
                type="password"
                id="confirmpassword"
                placeholder="Confirme sua senha:"
                value={confirmPassword}
                onChange={(event) => setConfirmPassword(event.target.value)}
              />
            </div>

            {/* Input do perfil do investidor */}
            <div className="profile">
              <h2>Perfil de investidor</h2>
              <label htmlFor="perfil">Selecione seu perfil de investidor:</label>
              <select id="perfil" value={profileType} onChange={handlePerfilChange}>
                <option value="nao-investidor">Não Investidor</option>
                <option value="iniciante">Iniciante</option>
                <option value="conservador">Conservador</option>
                <option value="moderado">Moderado</option>
              </select>
            </div>

            {/* Input do telefone */}
            <div className="phone-inputgroup">
              <label htmlFor="phone">Telefone:</label>
              <input
                type="tel"
                id="phone"
                placeholder=" Digite seu telefone:"
                value={phone}
                onChange={(event) => setPhone(event.target.value)}
              />
            </div>

            {/* Input do CPF */}
            <div className="cpf-inputgroup">
              <label htmlFor="cpf">CPF:</label>
              <input
                type="text"
                id="CPF"
                placeholder="Digite seu CPF:"
                value={CPF}
                onChange={(event) => setCPF(event.target.value)}
              />
            </div>

            {/* Input da data de nascimento */}
            <div className="form-input">
              <label htmlFor="birthdate">Data de nascimento:</label>
              <input
                type="date"
                id="birthdate"
                placeholder="Digite sua data de nascimento"
                value={birthdate}
                onChange={(event) => setBirthdate(event.target.value)}
              />
            </div>

            {/* Input do check de termo */}
            <div className="termos-inputgroup">
          <input
            type="checkbox"
            id="terms"
            checked={termsChecked}
            onChange={handleTermsChange}
          />
          <label htmlFor="terms">
            Eu concordo com os termos e condições
            <FontAwesomeIcon
              icon={faCheck}
              className={termsChecked ? "check-icon checked" : "check-icon"}
            />
          </label>
        </div>

            <button className="signup-button" type="submit" >Cadastre-se</button>
            <p>
              Já possui uma conta?{" "}
              <Link to="/login">
                {" "}
                Faça<span id="login-link"> Login </span>{" "}
              </Link>
            </p>
          </form>
          {error && <div className="error-message">{error}</div>}
        </div>
        </div>
  );
};

export default Cadastro;
