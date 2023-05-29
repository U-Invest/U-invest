import { Home, About, Courses, Teacher, Contact, Droid } from "../index";

function MainHome() {
  return (
    <>
      <div className="font-Poppins bg-Solitude">
        <Droid />
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
