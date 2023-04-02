import React, { useState } from "react";
import "./Modal.css";

export default function Modal() {
  const [modal, setModal] = useState(false);

  const toggleModal = () => {
    setModal(!modal);
  };

  if(modal) {
    document.body.classList.add('active-modal')
  } else {
    document.body.classList.remove('active-modal')
  }

  return (
    <>
      <button onClick={toggleModal} className="btn-modal py-3 px-6 font-bold text-sm border border-solid rounded-lg border-gray">
        Cadastre-se
      </button>

      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay"></div>
          <div className="modal-content">
            <h2>Cadastro</h2>
            <form action="">
                <label htmlFor="nome">Nome:</label>
                <input type="text" id="name" name="nome" placeholder="*Digite seu nome..."  required/>
                <label htmlFor="email">Email: </label>
                <input type="email" id="email" name="email" placeholder="*Digite seu email..." required/>
                <label htmlFor="nickName">Nickname: </label>
                <input type="text" id="nickName" name="nickName" placeholder="*Digite seu user..." required/>
                <label htmlFor="celular">Celular: </label>
                <input type="tel" id="celular" name="celular" placeholder="*11 999999999" required/>
                <label htmlFor="cpf">CPF: </label>
                <input type="text" id="cpf" name="cpf" placeholder="*Digite seu cpf..." required/>
                <label htmlFor="dataNasc">Data de Nascimento: </label>
                <input type="date" id="dataNasc" name="dataNasc" required/>
                <label htmlFor="perfilInvestidor">Perfil de Investidor: </label>
                <input type="text" id="perfilInvestidor" name="perfilInvestidor" placeholder="*Digite seu perfil de investidor..." required/>
                <label htmlFor="senha">Senha: </label>
                <input type="password" id="senha" name="senha" placeholder="*Digite sua senha..." required/>
                <button type="submit" class="btn-cadastrar">Cadastrar</button>
            </form>
            <button class="btn-fechar" onClick={toggleModal}>Fechar</button>
          </div>
        </div>
      )}
    </>
  );
}