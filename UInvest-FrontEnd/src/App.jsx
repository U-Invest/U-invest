import { BrowserRouter, Route, Routes } from 'react-router-dom';
import {
  Navbar,
  MainHome,
  Footer,
  Cursos,
  Login,
  Cadastro,
  AreaUsuario,

} from "./components/index";





function App() {

  return (
    <div className="font-Poppins bg-Solitude">
      <Navbar />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainHome />} />
          <Route path="/cursos" element={<Cursos />} />
          <Route path="/login" element={<Login />} />
          <Route path="/cadastro" element={<Cadastro />} />
          <Route path="/areausuario" element={<AreaUsuario />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;



