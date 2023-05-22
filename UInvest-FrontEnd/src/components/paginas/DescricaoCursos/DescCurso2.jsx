import React from 'react';
import curso2 from "../../../assets/curso-2-photo.webp"
import moedasImg from "../../../assets/ucoin tentativa.png"
import "./DescCurso2.css"
import { Link } from 'react-router-dom';

function DescCurso2() {
  const course = {
    title: 'Curso de Investimento',
    description: 'O curso sobre IPOs oferece uma visão abrangente do processo de abertura de capital. Os participantes aprenderão sobre os fundamentos, requisitos regulatórios e etapas envolvidas. O curso abordará a preparação, seleção de instituições financeiras, elaboração do prospecto e execução da oferta pública. Também serão explorados casos reais, tendências e desafios do mercado de capitais relacionados aos IPOs. Ao concluir o curso, os alunos terão um conhecimento aprofundado sobre IPOs e estarão mais bem preparados para tomar decisões informadas nesse contexto.',
    duration: '40 horas',
    balance: '1500',
  };

  return (
    <div className="course-card-container">
      <div className="course-card">
      <img className="course-card__cover" src={curso2} alt={course.title} />
        <div className="course-card__content">
          <h1 className="course-card__title">{course.title}</h1>
          <p className="course-card__description">{course.description}</p>
          <div className="course-card__details">
            <div className="course-card__detail">
              <p className="course-card__detail-label">Duração do curso:</p>
              <p className="course-card__detail-value">{course.duration}</p>
            </div>
            <div className="course-card__detail">
              <p className="course-card__detail-label">Saldo:</p>
              <div className="course-card__balance">
                <img className="course-card__balance-icon" src={moedasImg} alt="Moedas" />
                <p className="course-card__balance-value">{course.balance}</p>
              </div>
            </div>
          </div>
          <div className="course-card__buttons">
            <Link to="/catalogocursos" className="course-card__button">
              Voltar
            </Link>
            <Link to="/modulocurso2" className="course-card__button">
              Acessar Curso
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default DescCurso2;
