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

const Curso4 = () => {
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
        <h1>Curso - Módulo 1</h1>
      </div>
      <VideoAccordion
        title="Aula 01 - Entenda, o que é IPO?"
        videoId="ln2w2zFjq-g"
        description="Você já deve ter visto por aí várias análises e notícias sobre uma tal sigla do setor de finanças que tem a ver com o mercado de ações: IPO. Ela volta e meia aparece em textos e vídeos sobre gigantes da tecnologia ou startups, e é um passo muito importante na vida dessas marcas. Mas o que exatamente é uma IPO? Descubra agora, no Entenda!"
      />
      <VideoAccordion
        title="Aula 02 - Como é feito um IPO?"
        videoId="rGoEcCapePA"
        description="Praticamente todos os dias recebo perguntas a respeito de IPO das empresas e uma recorrente pergunta é a respeito de como o processo ocorre e quais são os requisitos necessários para abrir capital na bolsa de valores! Este ano ocorrerão mais alguns, não deixe de acompanhar os relatórios da Suno!"
      />
      <VideoAccordion
        title="Aula 03 - Vale a pena comprar ações em um IPO?"
        videoId="aPTkMwZNbyg"
        description="O vídeo fala sobre se há vantagens em comprar ações de empresas em um IPO - Initial Public Offering - A oferta inicial de ações, quando uma empresa abre seu capital na bolsa de valores."
      />
      <VideoAccordion
        title="Aula 04 - Empresas de Capital Aberto, vantagens e desvantagens"
        videoId="4WWBhLMQ3eo"
        description="Você já se perguntou, quais são as vantagens e desvantagens de um IPO numa empresa?"
      />
      <VideoAccordion
        title="Aula 05 - Por que as empresas abrem o capital?"
        videoId="GjiMgAfsp_I"
        description="Por que empresas abrem o capital? O que leva uma grande empresa a querer sócios? Neste vídeo, você vai entender por que muitas empresas (inclusive grandes empresas que, presumivelmente, não estão precisando de dinheiro) recorrem às bolsas de valores e abrem seu capital para o público, permitindo que pessoas comuns sejam suas sócias."
      />
      <VideoAccordion
        title="Aula 06 - Retrospectiva IPOs 2021 e Perspectivas 2022"
        videoId="PSmstWfBuDY"
        description="Retrospectiva dos IPOs em 2021. Aborda também as perspectivas para 2022, além de alternativas de oportunidades de captação."
      />
    </div>
  );
};

export default Curso4;
