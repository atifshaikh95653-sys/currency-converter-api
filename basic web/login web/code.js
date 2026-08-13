const container = document.querySelector(".container");
const goSignup = document.getElementById("goSignup");
const goLogin = document.getElementById("goLogin");

goSignup.onclick = () => {
  container.classList.add("active");
};

goLogin.onclick = () => {
  container.classList.remove("active");
};