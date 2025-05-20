
document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.querySelector('.burger-menu');
    const menu = document.querySelector('.menu');

    burgerMenu.addEventListener('click', function() {
      burgerMenu.classList.toggle('active');
      menu.classList.toggle('active');
    });
  });