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
        <h1>Curso - Módulo 1</h1>
      </div>
      <VideoAccordion
        title="Aula 01 - Introdução"
        videoId="BdVlty5wQ5Y"
        description="Esse curso de investimentos foi montado com o objetivo de te ensinar a investir de forma independente. Aqui teremos 18 aulas abordando os conceitos e práticas que te auxiliarão a entrar no mundo dos investimentos. Qualquer dúvida estou à disposição."
      />
      <VideoAccordion
        title="Aula 02 - Mudança de Mentalidade"
        videoId="G3aHNaR-BeM"
        description="A mudança de mentalidade é muito importante pra que você se torne um investidor de sucesso. Existem algumas ideias preconcebidas que muitas vezes temos sobre investimentos, que precisam ser repensadas por nós. Você se identificou com alguma dessas falas que mencionei na aula de hoje?"
      />
      <VideoAccordion
        title="Aula 03 - Renda Fixa e Renda Variável"
        videoId="8xWPEdW6-vo"
        description="Na nossa terceira aula serão abordados os tipos de investimentos e a importância de se investir. O que é renda fixa? O que é renda variável? Mecanismo da poupança. Confira tudo isso na aula de hoje.."
      />
      <VideoAccordion
        title="Aula 04 - Planejamento Financeiro"
        videoId="elBjWsdZSDo"
        description="Se planejar financeiramente é crucial pra que você tenha sucesso nos investimentos. Qualquer dúvida estou à disposição!"
      />
      <VideoAccordion
        title="Aula 05 - Abrir conta na corretora"
        videoId="ZajUwcv05R0"
        description="As corretoras são como pontes que ligam o investidor ao investimento. É através das corretoras que você será capaz de investir nos ativos que serão tratados ao longo desse curso. Atenção às taxas, existem ótimas corretoras que ofertam serviços de qualidade gratuitamente."
      />
      <VideoAccordion
        title="Aula 06 - Indicadores Financeiros (IPCA, Selic, CDI)"
        videoId="Gn_wgRTG-b0"
        description="Você sabe como esses indicadores financeiros influenciam nos seus investimentos? Ao investir, precisamos descontar os efeitos inflacionários, o ganho real, de forma simples, pode ser obtido pela fórmula rendimento - inflação. Suponha que o seu investimento rendeu 5%, mas a inflação do período foi de 3%, logo o seu ganho real foi de 2%. Essa é a fórmula rápida e simples de saber o ganho real, porém, a rentabilidade real do investimento se dá pela fórmula (((1+rendimento/(1+inflação))-1)*100, ou seja, a rentabilidade real, no exemplo acima, seria de ((1,05/1,03)-1)*100 = 1,94%."
      />
    </div>
  );
};

export default Cursos;
