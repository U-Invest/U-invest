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
const wrapper = document.querySelector(".wrapperLogin");

signUpBtnLink.addEventListener("click", () => {
  wrapper.classList.toggle("active");
});

signInBtnLink.addEventListener("click", () => {
  wrapper.classList.toggle("active");
});

// let username = document.getElementById("username");
// let email = document.getElementById("email");
// let password = document.getElementById("password");
// let terms = document.getElementById("terms");

// function cadastraUsuario() {
//   if (username && email && password && terms) {
//     let listaUser = JSON.parse(localStorage.getItem("listaUser") || "[]");

//     listaUser.push({
//       usernameCad: username.value,
//       emailCad: email.value,
//       passwordCad: password.value,
//       termsCad: terms.value,
//     });

//     localStorage.setItem("listaUser", JSON.stringify(listaUser));
//   } else {
//     console.log("Algo deu errado");
//   }
// }

// let usernameDefined = document.getElementById("usernameDefined");
// let passwordDefined = document.getElementById("passwordDefined");

// function logarUsuario() {
//   let listaUser = [];

//   let userValid = {
//     username: "",
//     password: "",
//   };

//   listaUser = JSON.parse(localStorage.getItem("listaUser"));

//   listaUser.forEach((item) => {
//     if (
//       usernameDefined.value == item.usernameCad &&
//       passwordDefined.value == item.passwordCad
//     ) {
//       userValid = {
//         username: item.usernameCad,
//         password: item.passwordCad,
//       };
//     } else {
//       console.log("Deu erro aqui (Primeiro If)");
//       console.log(usernameDefined.value, item.usernameCad);
//       console.log(usernameDefined.value, item.usernameCad);
//     }
//   });

//   if (
//     usernameDefined.value == userValid.username &&
//     passwordDefined.value == userValid.password
//   ) {
//     let mathRandom = Math.random().toString(16).substr(2);
//     let token = mathRandom + mathRandom;
//     localStorage.setItem("token", token);
//     localStorage.setItem("userLogado", JSON.stringify(userValid));
//     console.log("Você logou! Sua sessão foi criada com sucesso.");
//     window.alert("Você logou! Sua sessão foi criada com sucesso.");
//   } else {
//     console.log("Usuário ou senha incorretos");
//     window.alert("Usuário ou senha incorretos");
//   }
// }
