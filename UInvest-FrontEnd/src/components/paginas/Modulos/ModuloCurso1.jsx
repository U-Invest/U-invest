import React, { useEffect, useState } from "react";
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

const Modulo2 = () => {
  return (
    <div className="modulo">
      <h2>Módulo 2</h2>
      <p>Descrição do Módulo 2</p>
    </div>
  );
};

const Modulo3 = () => {
  return (
    <div className="modulo">
      <h2>Módulo 3</h2>
      <p>Descrição do Módulo 3</p>
    </div>
  );
};

const ModuloCurso1 = () => {
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
      <div className="title">
        <h1>Módulos do Curso</h1>
      </div>
      <ul className="lista-modulos">
        <li>
          <div className="modulo-link">
            <div
              className={`modulo ${activeAccordion === 0 ? "active" : ""}`}
              onClick={() => handleAccordionClick(0)}
            >
              <h2>Módulo 1</h2>
            </div>
            {activeAccordion === 0 && (
              <div className="modulo-conteudo">
                <p>Descrição do Módulo 1</p>
                <p>• Aula 1/18 - Introdução</p>
                <p>• Aula 2/18 - Mudança de Mentalidade</p>
                <p>• Aula 3/18 - Renda Fixa e Renda Variável</p>
                <p>• Aula 4/18 - Planejamento Financeiro</p>
                <p>• Aula 5/18 - Abrir conta na corretora </p>
                <p>• Aula 6/18 - Indicadores Financeiros (IPCA, Selic, CDI)</p>
                <br />
                <Link className="modulo-botao" to="/curso/1">
                  Acessar Curso
                </Link>
              </div>
            )}
          </div>
        </li>
        <li>
          <div className="modulo-link">
            <div
              className={`modulo ${activeAccordion === 1 ? "active" : ""}`}
              onClick={() => handleAccordionClick(1)}
            >
              <h2>Módulo 2</h2>
            </div>
            {activeAccordion === 1 && (
              <div className="modulo-conteudo">
                <p>Descrição do Módulo 2</p>
                <p>• Aula 7/18 - Investir no Tesouro Direto</p>
                <p>• Aula 8/18 - Investir em CDB's</p>
                <p>• Aula 9/18 - Investir em LCI's e LCA's</p>
                <p>• Aula 10/18 - Contas Digitais </p>
                <p>• Aula 11/18 - Investir em Ações</p>
                <p>• Aula 12/18 - Analisando ações na prática</p>
                <br />
                <Link className="modulo-botao" to="/curso/2">
                  Acessar Curso
                </Link>
              </div>
            )}
          </div>
        </li>
        <li>
          <div className="modulo-link">
            <div
              className={`modulo ${activeAccordion === 2 ? "active" : ""}`}
              onClick={() => handleAccordionClick(2)}
            >
              <h2>Módulo 3</h2>
            </div>
            {activeAccordion === 2 && (
              <div className="modulo-conteudo">
                <p>Descrição do Módulo 3</p>
                <p>• Aula 13/18 - Como investir em Fundos Imobiliários (FII)</p>
                <p>• Aula 14/18 - Fundos de Investimento</p>
                <p>• Aula 15/18 - ETFs</p>
                <p>
                  • Aula 16/18 - Investimentos recomendados para o investidor
                  iniciante
                </p>
                <p>• Aula 17/18 - Declaração de Imposto de Renda</p>
                <p>
                  • Aula 18/18 - Estratégias de investimento e próximos passos
                </p>
                <br />
                <Link className="modulo-botao" to="/curso/3">
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

export default ModuloCurso1;
