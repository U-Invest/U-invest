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
        <h1>Curso - Módulo 3</h1>
      </div>
      <VideoAccordion
        title="Aula 13 - Como investir em Fundos Imobiliários(FII)"
        videoId="jvul47FNGdw"
        description="Quem nunca sonhou em viver de aluguéis né? Pra isso você não precisa comprar 1 imóvel físico e arcar com todas as barreiras e burocracia na aquisição. Com alguns cliques você pode se tornar dona ou dono de vários imóveis. Acompanhe essa aula!"
      />
      <VideoAccordion
        title="Aula 14 - Fundos de Investimento"
        videoId="QJXAQ13a7eU"
        description="Seguimos em pé no curso! Eai? O que achou de Fundos de Investimentos?"
      />
      <VideoAccordion
        title="Aula 15 - ETFs"
        videoId="JaiLnwvlWpA"
        description="O vídeo em questão é uma aula sobre ETFs (Exchange-Traded Funds). ETFs são fundos de investimento que são negociados na bolsa de valores, assim como ações. No vídeo, provavelmente é abordado o funcionamento dos ETFs, suas vantagens e características, e como investir nesse tipo de fundo. Os ETFs são populares por oferecerem diversificação, baixo custo e facilidade de negociação. Eles podem ser uma opção interessante para investidores que desejam obter exposição a um conjunto diversificado de ativos, como ações, títulos, commodities, entre outros."
      />
      <VideoAccordion
        title="Aula 16 - Investimentos recomendados para o investidor iniciante"
        videoId="zg2gYAijm-g"
        description="O vídeo é uma videoaula que aborda os investimentos recomendados para o investidor iniciante."
      />
      <VideoAccordion
        title="Aula 17 - Declaração de Imposto de Renda"
        videoId="NY2WSQXWh2w"
        description="O vídeo é uma videoaula que explora os principais aspectos relacionados aos impostos de renda. Ele aborda conceitos fundamentais, como a declaração de imposto de renda, categorias de rendimentos, deduções permitidas, alíquotas aplicáveis e prazos importantes. A videoaula tem como objetivo fornecer informações e orientações úteis para que os espectadores compreendam melhor o processo de declaração e o impacto dos impostos de renda em suas finanças pessoais."
      />
      <VideoAccordion
        title="Aula 18 - Estratégias de investimento e próximos passos"
        videoId="UFkC0n4CSgk"
        description="Foi um prazer te acompanhar até aqui, até mais! Ou até nosso próximo curso rs."
      />
    </div>
  );
};

export default Cursos;
