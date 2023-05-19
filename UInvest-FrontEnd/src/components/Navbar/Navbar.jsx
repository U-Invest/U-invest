import React from 'react';
import { Link } from 'react-router-dom';
import UInvestLogo from '../../assets/logonavcerta.png';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/">
        <div className="logo">
          <img src={UInvestLogo} alt="Logo" />
        </div>
      </Link>
      <ul className="nav-links">
        <li>
          <Link to="/" className="nav-link1">Home</Link>
        </li>
        <li>
          <Link to="/teacher" className="nav-link1">Droid</Link>
        </li>
        <li>
          <Link to="/catalogocursos" className="nav-link1">Cursos</Link>
        </li>
        <li>
          <Link to="/contato" className="nav-link1">Contato</Link>
        </li>
        <li>
          <Link to="/cadastro" className="nav-link2">Cadastre-se</Link>
        </li>
        <li>
          <Link to="/login" className="nav-link2">Login</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
