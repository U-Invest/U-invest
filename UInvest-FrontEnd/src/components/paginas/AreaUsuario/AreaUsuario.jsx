import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./AreaUsuario.css";
import profile_picture from "../../../assets/foto_usuraio.png";

const AreaUsuario = () => {
  const navigate = useNavigate();
  const sessionEmail = sessionStorage.getItem("sessao");

  useEffect(() => {
    if (!sessionEmail) {
      navigate("/login");
    }
  }, [navigate, sessionEmail]);

  return (
    <div className="area-usuario">
      <h2>Seus dados pessoais</h2>
      <form>
        <div className="form-group">
          <img className="profile-picture-user" src={profile_picture} alt="" />
          <label htmlFor="nome">Nome completo</label>
          <input type="text" id="nome" name="nome" required />
        </div>
        <div className="form-group">
          <label htmlFor="cpf">CPF</label>
          <input type="text" id="cpf" name="cpf" required />
        </div>
        <div className="form-group">
          <label htmlFor="email">E-mail</label>
          <input type="email" id="email" name="email" required />
        </div>
        <div className="form-group">
          <label htmlFor="celular">Celular</label>
          <input type="text" id="celular" name="celular" required />
        </div>
        <div className="form-group">
          <label htmlFor="senha">Senha</label>
          <input type="password" id="senha" name="senha" required />
        </div>
        <div className="form-group">
          <label htmlFor="perfil_investidor">Perfil de investidor</label>
          <select id="perfil_investidor" name="perfil_investidor" required>
            <option value="">Selecione</option>
            <option value="conservador">Conservador</option>
            <option value="moderado">Moderado</option>
            <option value="arrojado">Arrojado</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="username">Nome de usuário</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div className="form-group">
          <label htmlFor="nascimento">Data de nascimento</label>
          <input type="date" id="nascimento" name="nascimento" required />
        </div>
        <div className="form-group">
          <label htmlFor="saldo">Saldo</label>
          <input type="text" id="saldo" name="saldo" required />
        </div>
        <button type="submit">Atualizar dados</button>
      </form>
    </div>
  );
};

export default AreaUsuario;
