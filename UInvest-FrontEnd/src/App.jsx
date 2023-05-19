import { BrowserRouter, Route, Routes } from "react-router-dom";
import {
  Navbar,
  MainHome,
  Cursos,
  Login,
  Teacher,
  Cadastro,
  AreaUsuario,
  CatalogoCursos,
  Contato,
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
            <Route path="/curso/1" element={<Cursos />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
