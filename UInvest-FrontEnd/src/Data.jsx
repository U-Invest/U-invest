import { AiFillBank } from "react-icons/ai";
import { AiFillGold } from "react-icons/ai";
import { BsBarChartLine } from "react-icons/bs";
import { AiFillReconciliation } from "react-icons/ai";


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

export const courses = [
  {
    id: 1,
    image: courses1,
    category: "Criptoativos",
    title: "Criptomoedas: tudo o que você precisa saber sobre elas",
    rating: 4.9,
    participants: 500,
  },
  {
    id: 2,
    image: courses2,
    category: "Fundos de Investimento",
    title: "Investindo em Fundos Imobiliários - Do Básico ao Avançado",
    rating: 4.8,
    participants: 700,
  },
  {
    id: 3,
    image: courses3,
    category: "Ações",
    title: "Aprenda a investir em ações",
    rating: 4.9,
    participants: 300,
  },
  {
    id: 4,
    image: courses4,
    category: "Criptoativos",
    title: "Criptomoedas - O básico",
    rating: 4.7,
    participants: 600,
  },
  {
    id: 5,
    image: courses5,
    category: "Câmbio",
    title: "Como investir em euro, dólar e outras moedas internacionais?",
    rating: 4.9,
    participants: 500,
  },
  {
    id: 6,
    image: courses6,
    category: "Ações",
    title: "Bolsa de Valores - Iniciantes",
    rating: 4.9,
    participants: 500,
  },
  {
    id: 7,
    image: courses7,
    category: "Ações",
    title: "Aprenda a Investir o seu Dinheiro",
    rating: 4.9,
    participants: 500,
  },
  {
    id: 8,
    image: courses8,
    category: "Fundos de Investimento",
    title: "Investindo em FIIs na bolsa!",
    rating: 4.9,
    participants: 500,
  },
];

export const logos = [logo1, logo2, logo3, logo4, logo5, logo6];

export const accordions = [
  {
    id: 1,
    title: "O que é a U Invest?",
  },
  {
    id: 2,
    title: "Como faço para aprender com a U Invest?",
  },
  {
    id: 3,
    title: "O que é o Droid?",
  },
  {
    id: 4,
    title: "Posso fazer parte da U Invest?",
  },
];
