import React from "react";
import { Link } from "react-router-dom";
import { cursos } from "../../../Data";
import "./CatalogoCursos.css";

const CatalogoCursos = () => {
  return (
    <div className="course-catalog">

      <h1>Catálogo de Cursos</h1>

      {cursos.map((cursos) => (
  <Link to={`/curso/${cursos.id}`} key={cursos.id} className="course-link">
    <div className="course-card">
      <img src={cursos.image} alt={cursos.title} />
      <h2>{cursos.title}</h2>
      <p>{cursos.description}</p>
    </div>
  </Link>
))}

    </div>
  );
};

export default CatalogoCursos;

