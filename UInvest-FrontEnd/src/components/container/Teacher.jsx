import React from "react";
import droid from "../../assets/droid.png";
import { accordions } from "../../Data";
import Accordion from "./Accordion";
const Teacher = () => {
  return (
    <div className="section" id="droid">
      <div className="grid sm:grid-cols-2 place-items-center gap-8">
        <div className="pl-5">
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />

          <div className="font-bold sm:text-[1.875rem] text-[1.5rem] mb-5">
            Conheça <span className="text-Teal">um instrutor</span> <br /> diferente
            em nossa plataforma... <span className="text-Teal">DROID!</span> 
          </div>
          <p className="text-sm leading-7 text-black mb-5">
            O droid será seu novo guia investidor! Pronto para tirar suas dúvidas relacionadas ao mercado do investimento.
            Sua principal funcionalidade de filtrar um prospecto de mercado, logo dismistificando IPOS.
            
          </p>
          <button className="py-3 px-4 bg-Teal text-white rounded-lg text-sm font-bold ">
            Tire suas dúvidas!
          </button>
        </div>
        <div className="p-4 md:w-3/4 sm:row-start-1">
          <img src={droid} alt="" />
        </div>
      </div>
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      

      <div className="text-center my-8 font-bold sm:text-[1.875rem] text-[1.5rem]">
        <span className="text-Teal"> Perguntas </span> Frequentes
      </div>
      <div className="mt-12 max-w-[700px] mx-auto">
        {accordions.map((accordion) => {
          return <Accordion key={accordion.id} {...accordion} />;
        })}
      </div>
    </div>
  );
};

export default Teacher;
