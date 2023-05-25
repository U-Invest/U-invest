import React from "react";
import about from "../../assets/cursos-onlinecerto.jpg";

const About = () => {
  return (
    <div className="section" id="sobre">
      <div className="grid md:grid-cols-2 gap-8 place-items-center">
        <div className="border-[3px] border-solid border-Teal rounded-lg">
          <img src={about} alt="" className="p-4" />
        </div>
        <div>
          <div className="font-bold sm:text-[1.875rem] text-[1.5rem] mb-5">
            Vamos proporcionar os
            <br /> melhores <span className="text-Teal">cursos online!</span>
          </div>
          <p className="text-sm text-gray leading-7 mb-4">
            A U Invest chegou no mercado para mudar o cenário de investimento.
            Com uma proposta inovadora unindo tecnnologia e investimento, com a
            proposta de multiplicar os acionistas brasileiros, venha nos
            conhecer melhor! Veja nossos cursos do catálogo ou até mesmo
            converse com o “Droid” nosso chatbot inteligente pronto pra sanar as
            suas dúvidas, e te ensinar muito, vale a pena ver. Eai, Bora
            Investir?
          </p>
          <button className="py-3 px-6 text-sm border border-solid border-gray rounded-lg font-bold">
            Saiba mais
          </button>
        </div>
      </div>
    </div>
  );
};

export default About;
