const form = document.getElementById("form-cadastro");
const camposCadastro = document.querySelectorAll(".campo-cadastro");
const emailRegex = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;

form.addEventListener("submit", (event) => {
  event.preventDefault();
  nameValidate();
  emailValidate();
  mainPasswordValidate();
  comparePassword();
  termsValidate();
});

function setError(index) {
  alert("Ocorreu um erro");
}

function removeError(index) {
  console.log("Não houve erros recorrentes");
}

function usernameValidate() {
  if (camposCadastro[0].value.length < 3) {
    setError(0);
  } else {
    removeError(0);
  }
}

function emailValidate() {
  if (!emailRegex.test(campos[1].value)) {
    setError(1);
  } else {
    removeError(1);
  }
}

function mainPasswordValidate() {
  if (campos[2].value.length < 8) {
    setError(2);
  } else {
    removeError(2);
    comparePassword();
  }
}

function comparePassword() {
  if (campos[2].value == campos[3].value && campos[3].value.length >= 8) {
    removeError(3);
  } else {
    setError(3);
  }
}

function termsValidate() {}


<script>
      let username = document.getElementById("username");
      let email = document.getElementById("email");
      let password = document.getElementById("password");
      let terms = document.getElementById("terms");

      function cadastraUsuario() {
        if (username && email && password && terms) {
          let listaUser = JSON.parse(localStorage.getItem("listaUser") || "[]");

          listaUser.push({
            usernameCad: username.value,
            emailCad: email.value,
            passwordCad: password.value,
            termsCad: terms.value,
          });

          localStorage.setItem("listaUser", JSON.stringify(listaUser));
        } else {
          console.log("Algo deu errado");
        }
      }

      let usernameDefined = document.getElementById("usernameDefined");
      let passwordDefined = document.getElementById("passwordDefined");

      function logarUsuario() {
        let listaUser = [];

        let userValid = {
          username: "",
          password: "",
        };

        listaUser = JSON.parse(localStorage.getItem("listaUser"));

        listaUser.forEach((item) => {
          if (
            usernameDefined.value == item.usernameCad &&
            passwordDefined.value == item.passwordCad
          ) {
            userValid = {
              username: item.usernameCad,
              password: item.passwordCad,
            };
          } else {
            console.log("Deu erro aqui (Primeiro If)");
            console.log(usernameDefined.value, item.usernameCad);
            console.log(usernameDefined.value, item.usernameCad);
          }
        });

        if (
          usernameDefined.value == userValid.username &&
          passwordDefined.value == userValid.password
        ) {
          let mathRandom = Math.random().toString(16).substr(2);
          let token = mathRandom + mathRandom;
          localStorage.setItem("token", token);
          localStorage.setItem("userLogado", JSON.stringify(userValid));
          console.log("Você logou! Sua sessão foi criada com sucesso.");
          window.alert("Você logou! Sua sessão foi criada com sucesso.");
        } else {
          console.log("Usuário ou senha incorretos");
          window.alert("Usuário ou senha incorretos");
        }
      }
    </script>