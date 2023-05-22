import { BrowserRouter, Route, Routes } from "react-router-dom";
import {
  Navbar,
  MainHome,
  Cursos1,
  Cursos2,
  Cursos3,
  Curso4,
  Login,
  Teacher,
  Footer,
  Cadastro,
  AreaUsuario,
  CatalogoCursos,
  Contato,
  DescCurso1,
  DescCurso2,
  ModuloCurso1,
  ModuloCurso2,
  About
} from "./components/index";
import { AuthProvider } from "./components/Navbar/AuthContext";

function App() {
  return (
    <div className="font-Poppins bg-Solitude">
      <BrowserRouter>
        <AuthProvider>
          <Navbar />
          <Routes>
            <Route path="/" element={<MainHome />} />
            <Route path="/login" element={<Login />} />
            <Route path="/cadastro" element={<Cadastro />} />
            <Route path="/teacher" element={<Teacher />} />
            <Route path="/contato" element={<Contato />} />
            <Route path="/areausuario" element={<AreaUsuario />} />
            <Route path="/catalogocursos" element={<CatalogoCursos />} />
            <Route path="/descricaocurso/1" element={<DescCurso1 />} />
            <Route path="/descricaocurso/2" element={<DescCurso2 />} />
            <Route path="/curso/1" element={<Cursos1 />} />
            <Route path="/curso/2" element={<Cursos2 />} />
            <Route path="/curso/3" element={<Cursos3 />} /> 
            <Route path="/curso/4" element={<Curso4 />} />
            <Route path="/modulocurso1" element={<ModuloCurso1 />} />
            <Route path="/modulocurso2" element={<ModuloCurso2 />} />
            <Route path="/about" element={<About/>} />
          </Routes>
          <Footer/>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
