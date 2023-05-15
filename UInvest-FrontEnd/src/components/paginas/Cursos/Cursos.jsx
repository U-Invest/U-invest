import React, { useState } from 'react';
import './Cursos.css';

const Accordion = ({ title, children }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="accordion">
      <div className="accordion-header" onClick={() => setIsOpen(!isOpen)}>
        <h3>{title}</h3>
        <span>{isOpen ? '-' : '+'}</span>
      </div>
      {isOpen && <div className="accordion-content">{children}</div>}
    </div>
  );
};

const VideoAccordion = ({ title, videoId, description }) => {
  return (
    <Accordion title={title}>
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
  return (

      <div className="inpage">
        <VideoAccordion
          title="Aula 01 - Introdução ao mercado de ações"
          videoId="yHuNhkntc-I"
          description="Descrição do vídeo 1."
        />
        <VideoAccordion
          title="Aula 02"
          videoId="7SK8R0obmu0"
          description="Descrição do vídeo 2."
        />
        <VideoAccordion
          title="Aula 03"
          videoId="pRpeEdMmmQ0"
          description="Descrição do vídeo 3."
        />
        <VideoAccordion
          title="Aula 04"
          videoId="u9Dg-g7t2l4"
          description="Descrição do vídeo 4."
        />
        <VideoAccordion
          title="Aula 05"
          videoId="RgKAFK5djSk"
          description="Descrição do vídeo 5."
        />
        <VideoAccordion
          title="Aula 06"
          videoId="zNcPql2KwDA"
          description="Descrição do vídeo 6."
        />
      </div>

    
  );
};

export default Cursos;
