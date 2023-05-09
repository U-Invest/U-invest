import React from "react";
import hero from "../../assets/personagem3dCERTO.png";
import { getDadosCursos } from "../../Data";
const Home = () => {
  const container = {
    hidden: {
      opacity: 0,
      scale: 0,
    },
    visible: {
      opacity: 1,
      scale: 1,
      transition: {
        delayChildren: 0.3,
        staggerChildren: 0.1,
      },
    },
  };
  const item = {
    hidden: { y: 20, opacity: 0 },
    visible: { y: 0, opacity: 1 },
  };
  return (
    <div className="section" id="inicio">
      <div className="md:flex items-center justify-center">
        <div>
          <div className="font-bold text-xs text-Teal mb-4">
            {" "}
            A melhor plataforma de aprendizado online
          </div>
          <div className="sm:text-[2.5rem] text-[1.825rem] font-bold">
            Essa é <br /> a nova maneira <br /> de aprender online.
          </div>
          <p className="text-sm leading-7 text-gray max-w-sm">
            Cadastre-se na U Invest, você terá acesso a cursos imperdíveis e muito mais, venha aprender com a gente!
          </p>
          <div className="mt-6">
            <button onClick={getDadosCursos} className="px-6 py-3 font-bold text-white bg-Teal rounded-lg mr-4 text-sm">
              Vamos começar!
            </button>
            <button className="px-6 py-3 font-bold border border-solid border-gray rounded-lg text-sm">
              Descubra
            </button>
          </div>
        </div>
        <div className="md:w-[60%]">
          <img src={hero} alt="" />
        </div>
      </div>
      <div>
        <p className="text-center text-xl">
          Colaboramos com {" "}
          <span className="text-Teal">
            a B3.
          </span>
        </p>
      </div>
    </div>
  );
};

export default Home;
