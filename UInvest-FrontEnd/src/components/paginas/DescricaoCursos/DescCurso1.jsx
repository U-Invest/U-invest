import React from "react";
import curso1 from "../../../assets/curso-1-photo.webp";
import moedasImg from "../../../assets/ucoin tentativa.png";
import "./DesCurso1.css";
import { Link } from "react-router-dom";

function CourseDescription() {
  const course = {
    title: "Curso de Investimento",
    description:
      "O Curso Completo de Investimento é uma jornada de aprendizado abrangente projetada para ajudar você a se tornar um investidor confiante e bem-sucedido. Composto por 18 vídeos envolventes, este curso abrange todos os aspectos fundamentais do mundo dos investimentos, desde conceitos básicos até estratégias avançadas.",
    duration: "40 horas",
    balance: "500",
  };

  return (
    <div className="course-card-container">
      <div className="course-card">
        <img className="course-card__cover" src={curso1} alt={course.title} />
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
                <img
                  className="course-card__balance-icon"
                  src={moedasImg}
                  alt="Moedas"
                />
                <p className="course-card__balance-value">{course.balance}</p>
              </div>
            </div>
          </div>
          <div className="course-card__buttons">
            <Link to="/catalogocursos" className="course-card__button">
              Voltar
            </Link>
            <Link to="/modulocurso1" className="course-card__button">
              Acessar Curso
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CourseDescription;
