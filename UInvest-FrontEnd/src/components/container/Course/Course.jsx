import React, { useState, useEffect } from "react";
import { AiOutlineUser, AiOutlineStar } from "react-icons/ai";
import { getDadosCursos } from "../../../Data";

import courses0 from "../../../assets/courses0.jpg";
import courses1 from "../../../assets/courses1.jpg";
import courses2 from "../../../assets/courses2.jpg";
import courses3 from "../../../assets/courses3.jpg";
import courses4 from "../../../assets/courses4.jpg";
import courses5 from "../../../assets/courses5.jpg";
import courses6 from "../../../assets/courses6.jpg";
import courses7 from "../../../assets/courses7.jpg";
import courses8 from "../../../assets/courses8.jpg";

const images = {
  0: courses0,
  1: courses1,
  2: courses2,
  3: courses3,
  4: courses4,
  5: courses5,
  6: courses6,
  7: courses7,
  8: courses8,
};

const Course = ({ idCarrosel }) => {

  const [curso, setCurso] = useState({});

  useEffect(() => {
    async function fetchData() {
      const dadosCursos = await getDadosCursos();
      const cursoEncontrado = dadosCursos.find(curso => curso.idCarrosel === idCarrosel);
      setCurso(cursoEncontrado || {});
    }

    fetchData();
  }, [idCarrosel]);

  return (
    <div className="p-2 shadow-lg min-w-[15rem] bg-white rounded-md">
      <img src={images[idCarrosel]} alt="" />
      <div className="mt-2 text-xs text-Teal">{curso.resumo}</div>
      <div className="text-sm mt-2 font-bold">{curso.nome}</div>
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="bg-Solitude p-1 rounded-full">
            <AiOutlineUser className="text-Teal" />
          </div>
          <div className="text-sm font-bold">{curso.pontuacao}</div>
        </div>
        <div className="flex items-center gap-2">
          <div className="bg-Solitude p-1 rounded-full">
            <AiOutlineStar className="text-yellow" />
          </div>
          <div className="text-sm font-bold">{curso.avaliacao}</div>
        </div>
      </div>
    </div>
  );
};

export default Course;