import React, { useContext, useState } from "react";
import { Link } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import UInvestLogo from "../../assets/logonavcerta.png";
import "./Navbar.css";
import { AuthContext } from "./AuthContext";
import profile_picture from "../../assets/foto_usuraio.png";
import ucoin from "../../assets/u-coins.png";
import ucoin2 from "../../assets/ucoin tentativa.png";
import { AiFillHome } from "react-icons/ai";
import { FaRobot } from "react-icons/fa";
import { BsFillBookFill } from "react-icons/bs";
import { IoMdContacts } from "react-icons/io";
import { AiOutlineLogin } from "react-icons/ai";
import { AiOutlineUserAdd } from "react-icons/ai";

const Navbar = () => {
  const { isAuthenticated, handleLogout } = useContext(AuthContext);
  const [loggingOut, setLoggingOut] = useState(false);

  const handleLogoutClick = async () => {
    try {
      setLoggingOut(true); // Ativar indicador de carregamento do logout
      await handleLogout(); // Esperar pela função de logout assíncrona

      setTimeout(() => {
        // Executar ações após o tempo de carregamento
        setLoggingOut(false); // Desativar indicador de carregamento
        toast.success("Logout concluído", {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
        });
      }, 3000);
    } catch (error) {
      // Lida com erros durante o logout
      console.log(error);
      setLoggingOut(false); // Desativar indicador de carregamento
      toast.error("Erro ao fazer logout", {
        position: toast.POSITION.TOP_CENTER,
        autoClose: 3000,
      });
    }
  };

  return (
    <>
      <ToastContainer />
      <nav className="navbar">
        <Link to="/">
          <div className="logo">
            <img src={UInvestLogo} alt="Logo" />
          </div>
        </Link>
        <ul className="nav-links">
          <li>
            <Link to="/" className="nav-link1">
              <AiFillHome />
            </Link>
          </li>
          <li>
            <Link to="/teacher" className="nav-link1">
              <FaRobot />
            </Link>
          </li>
          <li>
            <Link to="/catalogocursos" className="nav-link1">
              <BsFillBookFill />
            </Link>
          </li>
          <li>
            <Link to="/contato" className="nav-link1">
              <IoMdContacts />
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
              <li>
                <Link to="/">
                  <div className="ucoin">
                    <img src={ucoin2} alt="ucoin" />
                  </div>
                </Link>
              </li>
            </>
          ) : (
            <>
              <li>
                <Link to="/cadastro" className="nav-link2">
                  <AiOutlineUserAdd />
                </Link>
              </li>
              <li>
                <Link to="/login" className="nav-link2">
                  <AiOutlineLogin />
                </Link>
              </li>
            </>
          )}
        </ul>

        <ul className="nav-links2">
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
                  <div className="profile-picture-nav">
                    <img src={profile_picture} alt="Foto de perfil" />
                  </div>
                </Link>
              </li>
              <li>
                <Link to="/">
                  <div className="ucoin">
                    <img src={ucoin2} alt="ucoin" />
                    <p>0.00</p>
                  </div>
                </Link>
              </li>
              <li>
                <button onClick={handleLogoutClick} className="nav-link3">
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
      {loggingOut && (
        <div className="loading-overlay">
          <div className=""> Carregando...</div>
        </div>
      )}
    </>
  );
};

export default Navbar;
