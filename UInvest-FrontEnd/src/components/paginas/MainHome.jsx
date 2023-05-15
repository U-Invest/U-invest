import {
    Home,
    About,
    Courses,
    Teacher,
    Contact,
    Footer,
  } from "../index";
  
  
  function MainHome() {
    return (
      <>
      <div className="font-Poppins bg-Solitude">
        <Home />
        <About />
        <Courses/>
        <Teacher />
        <Contact />
        <Footer />
      </div>
      </>
    );
  }
  
  export default MainHome;