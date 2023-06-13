import { Home, About, Courses, Teacher, Contact} from "../index";

function MainHome() {
  return (
    <>
      <div className="font-Poppins bg-Solitude">
        <Home />
        <About />
        <Courses />
        <Teacher />
        <Contact />
      </div>
    </>
  );
}

export default MainHome;
