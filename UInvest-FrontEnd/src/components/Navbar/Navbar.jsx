import React, { useContext } from "react";
import { Link } from "react-router-dom";
import UInvestLogo from "../../assets/logonavcerta.png";
import "./Navbar.css";
import { AuthContext } from "./AuthContext";
import profile_picture from "../../assets/foto_usuraio.png";
import ucoin from "../../assets/u-coins.png";

const Navbar = () => {
  const { isAuthenticated, handleLogout } = useContext(AuthContext);

  return (
    <nav className="navbar">
      <Link to="/">
        <div className="logo">
          <img src={UInvestLogo} alt="Logo" />
        </div>

        <div className="ucoin">
          <img src={ucoin} alt="ucoin" />
        </div>

      </Link>
      <ul className="nav-links">
        <li>
          <Link to="/" className="nav-link1">
            Home
          </Link>
        </li>
        <li>
          <Link to="/teacher" className="nav-link1">
            Droid
          </Link>
        </li>
        <li>
          <Link to="/catalogocursos" className="nav-link1">
            Cursos
          </Link>
        </li>
        <li>
          <Link to="/contato" className="nav-link1">
            Contato
          </Link>
        </li>
        {isAuthenticated ? (
          <>
            <li>
              <Link to="/areausuario">
              <div className="profile-picture">
                <img src={profile_picture} alt="Logo" />
                </div>
              </Link>
            </li>


            <li>
              <button onClick={handleLogout} className="nav-link3">
                Logout
              </button>
            </li>
          </>
        ) : (
          <>
            <li>
              <Link to="/cadastro" className="nav-link2">
                Cadastre-se
              </Link>
            </li>
            <li>
              <Link to="/login" className="nav-link2">
                Login
              </Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
