import {
    Navbar,
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
        <Navbar />
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