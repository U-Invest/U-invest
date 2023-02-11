function lightMode() {
  let checkbox = document.getElementById("checkbox");
  let backgroundDark = document.querySelectorAll(".bg-dark");
  let textDark = document.querySelectorAll(".text-light");
  let backgroundLight = document.querySelectorAll(".bg-light");
  let textLight = document.querySelectorAll(".text-dark");

  if (checkbox.checked) {
    for (i = 0; i < backgroundDark.length; i++) {
      backgroundDark[i].classList.remove("bg-dark");
      backgroundDark[i].classList.add("bg-light");
    }
    for (i = 0; i < textDark.length; i++) {
      textDark[i].classList.remove("text-light");
      textDark[i].classList.add("text-dark");
    }
  } else {
    for (i = 0; i < backgroundLight.length; i++) {
      backgroundLight[i].classList.remove("bg-light");
      backgroundLight[i].classList.add("bg-dark");
    }
    for (i = 0; i < textLight.length; i++) {
      textLight[i].classList.remove("text-dark");
      textLight[i].classList.add("text-light");
    }
  }
}

const signUpBtnLink = document.querySelector(".signUpBtn-link");
const signInBtnLink = document.querySelector(".signInBtn-link");
const wrapper = document.querySelector(".wrapper");

signUpBtnLink.addEventListener("click", () => {
  wrapper.classList.toggle("active");
});

signInBtnLink.addEventListener("click", () => {
  wrapper.classList.toggle("active");
});
