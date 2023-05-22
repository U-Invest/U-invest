import React from "react";
import {
  BsFacebook,
  BsInstagram,
  BsTwitter,
  BsLinkedin,
} from "react-icons/bs";
import { motion } from "framer-motion";
import {Link} from "react-router-dom";

const Footer = () => {
  return (
    <motion.div
      initial={{ height: 0 }}
      whileInView={{ height: "auto" }}
      transition={{ duration: 1 }}
      className="bg-Teal p-10"
    >
      <div className="grid md:grid-cols-4 sm:grid-cols-3 xs:grid-cols-2 grid-cols-1 place-items-start gap-8 text-white">
        <div>
          <div className="font-bold mb-6">Vamos Começar!</div>
          <p className="text-sm leading-7">
            Crie sua conta na U Invest para uma imersão no mundo dos investimentos, relaxa, nós te enchaminharemos para o seu perfil de investidor!
          </p>
        </div>
        <div>
          <div className="font-bold mb-6">Serviços</div>
            <ul className="flex flex-col gap-4">
              <li className="text-sm hover:underline">
                <Link to="/teacher">Droid</Link>
              </li>
              <li className="text-sm hover:underline">
                <Link to="/catalogocursos">Cursos</Link>
              </li>
            </ul>
        </div>
        <div>
          <div className="font-bold mb-6">U Invest</div>
            <ul className="flex flex-col gap-4">
              <li className="text-sm hover:underline">
                <Link to="/">Home</Link>
              </li>
              <li className="text-sm hover:underline">
                <Link to="/about">Sobre nós</Link>
              </li>
              <li className="text-sm hover:underline"> 
                <Link to="/">Política de Privacidade</Link>
              </li>
              <li className="text-sm hover:underline">
                <Link to="/">Termos & Condições</Link>
              </li>
            </ul>
        </div>
        <div>
          <div className="font-bold mb-6">Contato</div>
          <div className="text-sm mb-4">u_investbrasil@gmail.com</div>
          <div className="text-sm">(11) 98546-9898</div>
          <div className="flex gap-4 mt-4">
            <a href="" className="hover:scale-110 text-xl">
              <BsFacebook />
            </a>
            <a href="" className="hover:scale-110 text-xl">
              <BsInstagram />
            </a>
            <a href="" className="hover:scale-110 text-xl">
              <BsTwitter />
            </a>
            <a href="" className="hover:scale-110 text-xl">
              <BsLinkedin />
            </a>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default Footer;
