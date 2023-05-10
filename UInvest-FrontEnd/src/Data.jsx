import { AiFillBank } from "react-icons/ai";
import { AiFillGold } from "react-icons/ai";
import { BsBarChartLine } from "react-icons/bs";
import { AiFillReconciliation } from "react-icons/ai";
import axios from 'axios';

import courses1 from "./assets/courses1.jpg";
import courses2 from "./assets/courses2.jpg";
import courses3 from "./assets/courses3.jpg";
import courses4 from "./assets/courses4.jpg";
import courses5 from "./assets/courses5.jpg";
import courses6 from "./assets/courses6.jpg";
import courses7 from "./assets/courses7.jpg";
import courses8 from "./assets/courses8.jpg";

import logo1 from "./assets/logo1.png";
import logo2 from "./assets/logo2.png";
import logo3 from "./assets/logo3.png";
import logo4 from "./assets/logo4.png";
import logo5 from "./assets/logo5.png";
import logo6 from "./assets/logo6.png";

export const navLinks = [
  {
    id: 1,
    href: "inicio",
    link: "Página Inicial",
  },
  {
    id: 2,
    href: "sobre",
    link: "Sobre",
  },
  {
    id: 3,
    href: "cursos",
    link: "Cursos",
  },
  {
    id: 4,
    href: "droid",
    link: "Droid",
  },
  {
    id: 5,
    href: "contato",
    link: "Contato",
  },
];

export const categories = [
  {
    id: 1,
    icon: <AiFillBank />,
    category: "Ações",
  },
  {
    id: 2,
    icon: <BsBarChartLine />,
    category: "Fundos Imobiliários",
  },
  {
    id: 3,
    icon: <AiFillReconciliation />,
    category: "IPO",
  },
  {
    id: 4,
    icon: <AiFillGold />,
    category: "Criptos",
  },
];

export async function getDadosCursos() {
  try {
    const response = await axios.get('http://localhost:8080/UInvest/cursos');
    const cursosJson = response.data;
    const cursosManipulados = [];
    
    cursosJson.forEach((objeto, index) => {
      const objetoComId = { ...objeto, idCarrosel: index };
      cursosManipulados.push(objetoComId);
    });
    return cursosManipulados
  } catch (error) {
    console.error(error);
  }
}

export const logos = [logo1, logo2, logo3, logo4, logo5, logo6];

export const accordions = [
  {
    id: 1,
    title: "O que é a U Invest?",
    content: "A U Invest é uma plataforma de investimentos online..."
  },
  {
    id: 2,
    title: "Como faço para aprender com a U Invest?",
    content: "Você pode aprender com a U Invest através de nossos cursos online..."
  },
  {
    id: 3,
    title: "O que é o Droid?",
    content: "O Droid é uma ferramenta de investimento automatizada..."
  },
  {
    id: 4,
    title: "Posso fazer parte da U Invest?",
    content: "Sim, você pode fazer parte da U Invest..."
  },
];


