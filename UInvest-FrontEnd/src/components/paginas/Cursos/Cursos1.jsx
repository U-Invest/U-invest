import React, { useState } from 'react';
import './Cursos1.css';

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
          title="Aula 01 - Introdução"
          videoId="BdVlty5wQ5Y"
          description="Intrudução ao curso de investimentos"
        />
        <VideoAccordion
          title="Aula 02 - Mudança de Mentalidade"
          videoId="G3aHNaR-BeM"
          description="Segundo vídeo do curso, voltado para uma área mais mental"
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
