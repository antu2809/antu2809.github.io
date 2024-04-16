document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.querySelector('.button-menu');
    const menuContainer = document.getElementById('menu-container');
    const toggleSwitch = document.querySelector('.toggle-switch input[type="checkbox"]');

    menuButton.addEventListener('click', function() {
        console.log("Menu button clicked.");
        menuContainer.classList.toggle('active');
    });

    toggleSwitch.addEventListener('change', switchTheme);

    document.getElementById('menu-button').addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Hace que el desplazamiento sea suave
        });
    });

    function switchTheme() {
        var body = document.getElementsByTagName('body')[0];
        var checkbox = document.querySelector('.toggle-switch input[type="checkbox"]');
        var header = document.getElementById('page-header');
        var skillsSection = document.querySelector('.special-skills-container');
        var experienceSection = document.querySelector('.experience-container');
        var navLinks = document.querySelectorAll('.nav-d a');

        if (checkbox.checked) {
            body.setAttribute('data-theme', 'dark');
        } else {
            body.setAttribute('data-theme', 'light');
        }
    }


    var lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        var menuContainer = document.getElementById('menu-container');
        var currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScrollTop > lastScrollTop) { // Si el usuario se desplaza hacia abajo
            menuContainer.classList.remove('active'); // Quita la clase 'active'
        }

        lastScrollTop = currentScrollTop <= 0 ? 0 : currentScrollTop; // Para manejar el desplazamiento hacia arriba en la parte superior de la página
    });


     // Función ScrollReveal().reveal()
    ScrollReveal().reveal('.dual__content', {
        // Opciones de animación (puedes ajustarlas según tus necesidades)
        origin: 'left', // La animación comenzará desde la izquierda
        distance: '50px', // La distancia de desplazamiento es de 50px
        duration: 1000, // Duración de la animación en milisegundos (1 segundo)
        delay: 0 // No hay retraso antes de que comience la animación
    });
    ScrollReveal().reveal('.dual__inner', {
        // Opciones de animación (puedes ajustarlas según tus necesidades)
        origin: 'bottom', // La animación comenzará desde abajo
        distance: '50px', // La distancia de desplazamiento es de 50px
        duration: 1000, // Duración de la animación en milisegundos (1 segundo)
        delay: 0 // No hay retraso antes de que comience la animación
    });

     // Función ScrollReveal().reveal()
    ScrollReveal().reveal('.content__title--left', {
        // Opciones de animación (puedes ajustarlas según tus necesidades)
        origin: 'bottom', // La animación comenzará desde la izquierda
        distance: '50px', // La distancia de desplazamiento es de 50px
        duration: 1000, // Duración de la animación en milisegundos (1 segundo)
        delay: 0 // No hay retraso antes de que comience la animación
    });
});


