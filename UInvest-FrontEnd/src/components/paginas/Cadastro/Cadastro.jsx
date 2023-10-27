import React from "react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import 'react-toastify/dist/ReactToastify.min.css';
import { Link } from "react-router-dom";
import "./Cadastro.css";
import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheck } from "@fortawesome/free-solid-svg-icons";


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

  const isValidFullName = (fullName) => {
    return /^[A-Za-z\s]+$/.test(fullName);
  };

  const isValidEmail = (email) => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  };

  const isValidPassword = (password) => {
    return /^(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$/.test(password);
  };

  const isValidPhone = (phone) => {
    return /^\(\d{2}\)\d{5}-\d{4}$/.test(phone);
  };

  const isValidCPF = (cpf) => {
    return /^\d{3}\.\d{3}\.\d{3}-\d{2}$/.test(cpf);
  };

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

  const formatPhoneNumber = (input) => {
    const phoneNumber = input.replace(/\D/g, "");

    if (phoneNumber.length >= 10) {
      const formattedPhoneNumber =
        `(${phoneNumber.slice(0, 2)})${phoneNumber.slice(2, 7)}-${phoneNumber.slice(7, 11)}`;
      setPhone(formattedPhoneNumber);
    } else {
      setPhone(phoneNumber);
    }
  };

  const handlePhoneChange = (event) => {
    formatPhoneNumber(event.target.value);
  };

  const formatCPF = (input) => {
    const cpf = input.replace(/\D/g, "");

    if (cpf.length >= 11) {
      const formattedCPF =
        `${cpf.slice(0, 3)}.${cpf.slice(3, 6)}.${cpf.slice(6, 9)}-${cpf.slice(9, 11)}`;
      setCPF(formattedCPF);
    } else {
      setCPF(cpf);
    }
  };

  const handleCPFChange = (event) => {
    formatCPF(event.target.value);
  };


  const handleSubmit = (event) => {
    event.preventDefault();

    if (!termsChecked) {
      setError("Por favor, aceite os termos e condições.");
      return;
    }

    if (!isValidFullName(name)) {
      setError("Nome completo inválido. Não pode conter caracteres especiais, números ou estar em branco.");
      return;
    }

    if (!username) {
      setError("Username não pode estar em branco.");
      return;
    }

    if (!isValidEmail(email)) {
      setError("Email inválido. Deve conter um formato válido (ex: example@example.com).");
      return;
    }

    if (!isValidPassword(password)) {
      setError("Senha inválida. Deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial.");
      return;
    }

    if (password !== confirmPassword) {
      setError("A senha e a confirmação de senha não coincidem.");
      return;
    }

    if (!isValidPhone(phone)) {
      setError("Telefone inválido.");
      return;
    }

    if (!isValidCPF(CPF)) {
      setError("CPF inválido.");
      return;
    }

    if (!birthdate) {
      setError("Selecione uma data de nascimento válida.");
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
              onChange={(event) => {
                const value = event.target.value;
                if (value.length <= 20) {
                  setUserName(value);
                }
              }}
              maxLength={20} // Adição do atributo maxLength com valor 20
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

          <div className="phone-inputgroup">
            <label htmlFor="phone">Telefone:</label>
            <input
              type="tel"
              id="phone"
              placeholder="Digite seu telefone:"
              value={phone}
              onChange={handlePhoneChange}
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
              onChange={handleCPFChange} 
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
