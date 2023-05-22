import React from "react";
import { Link } from "react-router-dom";
import { cursos } from "../../../Data";
import "./CatalogoCursos.css";

const CatalogoCursos = () => {
  return (
    <div className="course-catalog">
      <div className="titlee">
        <h1>Catálogo de Cursos</h1>
      </div>

      {cursos.map((curso) => (
        <Link to={`/descricaocurso/${curso.id}`} key={curso.id} className="course-link">
          <div className="course-card">
            <img src={curso.image} alt={curso.title} />
            <h2>{curso.title}</h2>
            <p>{curso.description}</p>
            <div className="button-container">
              <button className="course-button">Ver detalhes</button>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default CatalogoCursos;
