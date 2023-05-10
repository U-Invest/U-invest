import React, { useState, useEffect } from "react";
import { categories } from "../../../Data";
import Categories from "./Categories";
import Course from "./Course";
import { motion } from "framer-motion";
import { getDadosCursos } from "../../../Data";

const Courses = () => {
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
        staggerChildren: 0.2,
      },
    },
  };

  const [cursos, setCursos] = useState([]);

  useEffect(() => {
    async function fetchCursos() {
      try {
        const data = await getDadosCursos();
        setCursos(data);
      } catch (error) {
        console.error(error);
      }
    }

    fetchCursos();
  }, []);

  return (
    <div className="section" id="cursos">
      <div className="text-center">
        <div className="sm:text-3xl text-2xl font-bold mb-5">
          As nossas principais <span className="text-Teal">Categorias</span>
        </div>
        <p className="text-sm text-gray leading-7 max-w-[700px] mx-auto">
          Sim! A U Invest possui diversas categorias, que se profundam no assunto investimento, segue as principais categorias que abordamos.
        </p>
      </div>
      <motion.div
        variants={container}
        initial="hidden"
        whileInView="visible"
        className="grid md:grid-cols-4 sm:grid-cols-2 mt-12 gap-8"
      >
        {categories.map((category) => {
          return <Categories key={category.id} {...category} />;
        })}
      </motion.div>
      <div className="text-xl font-bold mt-32">Nossos cursos</div>
      <div className="mt-12 overflow-x-hidden w-full  relative">
        <div className="flex gap-8 md:w-full sm:w-[170%] xs:w-[340%] w-[480%] animate-slide">
          {cursos.map((curso) => {
            return <Course key={curso.idCarrosel} {...curso} />;
          })}
        </div>
      </div>
    </div>
  );
};

export default Courses;