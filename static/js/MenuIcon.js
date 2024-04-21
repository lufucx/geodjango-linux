let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navbar');

menu.onclick = () => {
  menu.classList.toggle('menu-icon');
  navlist.classList.toggle('open');
};

document.addEventListener("DOMContentLoaded", function () {
  const sr = ScrollReveal({
    distance: '65px',
    duration: 2100,
    reset: false
  });

  sr.reveal('.legenda-titulo', {
    delay: 200,
    opacity: 0,
    origin: 'top',
  })
  sr.reveal('.pin', {
    delay: 300,
    opacity: 0,
    interval: 300,
    origin: 'left'
  });

  sr.reveal('.card', {
    delay: 200,
    opacity: 0,
    interval: 300,
    origin: 'bottom'
  });

});
