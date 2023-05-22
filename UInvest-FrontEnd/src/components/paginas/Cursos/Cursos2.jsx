import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Cursos1.css";

const Accordion = ({ title, children }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="accordion">
      <div className="accordion-header" onClick={() => setIsOpen(!isOpen)}>
        <h3>{title}</h3>
        <span>{isOpen ? "-" : "+"}</span>
      </div>
      {isOpen && <div className="accordion-content">{children}</div>}
    </div>
  );
};

const VideoAccordion = ({ title, videoId, description }) => {
  return (
    <Accordion title={title}>
      <h2>{title}</h2>
      <div className="video-wrapper">
        <iframe
          title={title}
          src={`https://www.youtube.com/embed/${videoId}`}
          allowFullScreen
        />
      </div>
      <p className="video-description">{description}</p>
    </Accordion>
  );
};

const Cursos = () => {
  const navigate = useNavigate();
  const sessionEmail = sessionStorage.getItem("sessao");

  useEffect(() => {
    if (!sessionEmail) {
      navigate("/login");
    }
  }, [navigate, sessionEmail]);

  return (
    <div className="inpage">
      <div className="title">
        <h1>Curso - Módulo 2</h1>
      </div>
      <VideoAccordion
        title="Aula 07 - Investir no Tesouro Direto"
        videoId="1fHQilQjj9E"
        description="Investir no Tesouro Direto é uma alternativa interessante pra quem está começando a investir e ainda não conhece o mundo dos investimentos. Infelizmente atualmente estamos passando por momentos delicados na Economia, devido à pandemia do coronavírus, grau arriscado dos países emergentes como o Brasil instabilidade política dentre outros fatores. Tudo isso em conjunto com o contexto macroeconômico, levaram o Banco Central a cortar a Taxa Selic a níveis baíssimos, de 2% ao ano. por conta disso os investimentos de renda fixa estão pouco atrativos. Dessa forma nunca foi tão necessário retirar o dinheiro das poupanças, que já estão perdendo pra inflação. A a ideia aqui é instigá-lo a refletir sobre a possibilidade de alocação do seu dinheiro no Tesouro Direto."
      />
      <VideoAccordion
        title="Aula 08 - Investir em CDB's"
        videoId="QwSK8IH_Azc"
        description="CDB's são os investimentos de renda fixa mais conhecidos pelos brasileiros, você sabe como investir?"
      />
      <VideoAccordion
        title="Aula 09 - Investir em LCI's e LCA's"
        videoId="98bR4gmTkc8"
        description="LCI's e LCA's são investimentos de renda fixa bem atrativos uma que contam com o benefício de isenção de imposto de renda!"
      />
      <VideoAccordion
        title="Aula 10 - Contas Digitais"
        videoId="6djsLAU-TT0"
        description="Você ja possui uma conta em bancos digitais?"
      />
      <VideoAccordion
        title="Aula 11 - Investir em Ações"
        videoId="ktS9vYq4x4E"
        description="Investir em ações é sem dúvidas uma ótima estratégia pra crescimento de patrimônio no Longo Prazo. Seguindo as estratégias corretas e fazendo boas escolhas, de boas empresas, o investidor tende a obter sucesso. Mas se você ainda não sabe o que são ações de uma olhada na aula de hoje!"
      />
      <VideoAccordion
        title="Aula 12 - Analisando ações na prática"
        videoId="CYem7f4y-3M"
        description="A análise fundamentalista é a principal metodologia que o investidor de longo prazo deve aderir. É através dela que o investidor vai conhecer a saúde financeira da empresa, alocando o seu capital da melhor forma."
      />
    </div>
  );
};

export default Cursos;
