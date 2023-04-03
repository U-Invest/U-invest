import React from "react";
import { motion } from "framer-motion";
const Contact = () => {
  return (
    <div className="section" id="contato">
      <div className="text-center max-w-[600px] mx-auto">
        <div className="sm:text-3xl text-2xl font-bold mb-5">
          Se inscreva no nosso newsletter
        </div>
        <p className="text-sm leading-7 text-gray">
          Se inscreva no nosso newsletter! Você receberá notícias atualizadas diariamente do mundo do investimento. E aí, ta esperando o que pra se increver?
        </p>
        <motion.form
          initial={{ scale: 0 }}
          whileInView={{ scale: 1 }}
          transition={{ duration: 0.3 }}
          className="mt-5"
        >
          <input
            type="text"
            placeholder="E-Mail"
            className="sm:p-3 p-2 outline-none text-sm shadow-md sm:w-72 w-60"
          />
          <button className="text-sm text-white bg-Teal sm:p-3 p-2 shadow-md font-bold">
            Inscrever-se
          </button>
        </motion.form>
      </div>
    </div>
  );
};

export default Contact;
