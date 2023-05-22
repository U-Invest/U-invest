import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import "./ModuloCurso1.css";

const Modulo1 = () => {
  return (
    <div className="modulo">
      <h2>Módulo 1</h2>
      <p>Descrição do Módulo 1</p>
    </div>
  );
};

const ModuloCurso2 = () => {
  const [activeAccordion, setActiveAccordion] = useState(null);
  const navigate = useNavigate();
  const sessionEmail = sessionStorage.getItem("sessao");

  useEffect(() => {
    if (!sessionEmail) {
      navigate("/login");
    }
  }, [navigate, sessionEmail]);

  const handleAccordionClick = (index) => {
    setActiveAccordion((prevAccordion) =>
      prevAccordion === index ? null : index
    );
  };

  return (
    <div className="pagina-modulos">
      <br />
      <br />
      <br />
      <br />

      <div className="title">
        <h1>Módulos do Curso</h1>
      </div>
      <ul className="lista-modulos">
        <li>
          <div className="modulo-link">
            <br />
            <br />

            <div
              className={`modulo ${activeAccordion === 0 ? "active" : ""}`}
              onClick={() => handleAccordionClick(0)}
            >
              <h2>Módulo 1</h2>
            </div>

            {activeAccordion === 0 && (
              <div className="modulo-conteudo">
                <p>Descrição do Módulo 1</p>
                <p>• Aula 1/6 - Entenda, o que é IPO?</p>
                <p>• Aula 2/6 - Como é feito um IPO?</p>
                <p>• Aula 3/6 - Vale a pena comprar ações em um IPO?</p>
                <p>
                  • Aula 4/6 - Empresas de Capital Aberto, vantagens e
                  desvantagens
                </p>
                <p>• Aula 5/6 - Por que as empresas abrem o capital?</p>
                <p>• Aula 6/6 - Retrospectiva IPOs 2021 e Perspectivas 2022</p>
                <br />
                <Link className="modulo-botao" to="/curso/4">
                  Acessar Curso
                </Link>
              </div>
            )}
          </div>
        </li>
      </ul>
    </div>
  );
};

export default ModuloCurso2;
