const navbarToggler = document.querySelector(".navbar-toggler");
const navbarMenu = document.querySelector(".navbar ur");

navbarToggler.addEventListener("click", navbarTogglerClick);

function navbarTogglerClick () {
    navbarToggler.classList.toggle("open-navbar-togglar")
}