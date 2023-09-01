function toggleMenu() {
    var menu = document.getElementById("nav-menu");
    var burger = document.querySelector(".burger");
    var body = document.querySelector("body");

    menu.classList.toggle("show");
    burger.classList.toggle("burger-active");
    body.classList.toggle("no-scroll");
}

function switchTheme() {
  var body = document.getElementsByTagName('body')[0];
  var checkbox = document.getElementsByTagName('input')[0];
  var header = document.getElementById('page-header');
  var skillsSection = document.querySelector('.special-skills-container');
  var experienceSection = document.querySelector('.experience-container');

  if (checkbox.checked) {
      body.setAttribute('data-theme', 'dark');
  } else {
      body.setAttribute('data-theme', 'light');
  }
}

// Función para inicializar las animaciones
function initAnimations() {
  const clipPathContainer = document.querySelector('.clip-path-container');
  clipPathContainer.classList.add('animate');
}

// Llama a initAnimations cuando se carga la página y en el evento resize si el ancho es menor o igual a 768px
window.addEventListener('load', () => {
  initAnimations();
});

window.addEventListener('resize', () => {
  if (window.innerWidth <= 768) {
    initAnimations();
  }
});

window.addEventListener('load', function() {
    const clipPathContainer = document.querySelector('.clip-path-container');
    clipPathContainer.classList.add('animate');
   });

document.addEventListener("DOMContentLoaded", function() {
  // Obtenemos los elementos de los logos de las redes sociales
  const linkedinLogo = document.querySelector(".social-link[data-profile='linkedin']");
  const githubLogo = document.querySelector(".social-link[data-profile='github']");
  const socialLinks = document.querySelectorAll(".social-link");
  
  // Eventos de escucha para los eventos 'mouseover', 'mouseout', 'touchstart' y 'touchend' de los logos
  linkedinLogo.addEventListener("mouseover", showProfileTooltip);
  linkedinLogo.addEventListener("mouseout", hideProfileTooltip);

  githubLogo.addEventListener("mouseover", showProfileTooltip);
  githubLogo.addEventListener("mouseout", hideProfileTooltip);

   // Función para mostrar el tooltip del perfil
   function showProfileTooltip(event) {
    // Obtenemos el enlace padre del elemento img
    const socialLink = event.currentTarget.closest(".social-link");
  
    // Obtenemos la red social correspondiente y la información del perfil
    const social = socialLink.getAttribute("data-profile");
    const profileData = getProfileData(social);
  
    // Creamos el tooltip y establecemos su contenido
    const tooltip = document.createElement("div");
    tooltip.classList.add("profile-tooltip");
    tooltip.innerHTML = `
      <img src="${profileData.photo}" alt="${social} profile photo">
      <p>${profileData.info}</p>
    `;
  
    // Establecemos la posición del tooltip debajo del logo de la red social
    const logoRect = socialLink.getBoundingClientRect();
    tooltip.style.top = `${logoRect.bottom}px`;
    tooltip.style.left = `${logoRect.left}px`;
  
    // Agregamos el tooltip al documento
    document.body.appendChild(tooltip);
  }
  
  // Función para ocultar el tooltip del perfil
  function hideProfileTooltip(event) {
    const tooltip = document.querySelector(".profile-tooltip");
    if (tooltip) {
      document.body.removeChild(tooltip);
    }
  }
  
  // Función para obtener la información del perfil según la red social
  function getProfileData(social) {
    const profiles = {
      linkedin: {
        photo: "https://media.licdn.com/dms/image/D4D35AQGWTLcQ5UjJ_A/profile-framedphoto-shrink_400_400/0/1687451409358?e=1688115600&v=beta&t=MXu6lO08hessKpoOpFQ5lizh4OeBesQtHztOPDtNCZE",
        info: "https://www.linkedin.com/in/francisco-antu-almonacid-cammarata-543119267/opportunities/job-opportunities/details?profileUrn=urn%3Ali%3Afs_normalized_profile%3AACoAAEFVzMMBP0xOzrB1QPHq4oE2lDHYeBhaU84&trk=opento_sprofile_details&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B4EC%2FuIPlR%2Fei3Br%2BxhBovA%3D%3D"
      },
      github: {
        photo: "https://avatars.githubusercontent.com/u/102919566?v=4",
        info: "https://github.com/antu2809?tab=repositories"
      }
    };
  
    return profiles[social];
  }

  // Agregar evento de clic a cada logo en dispositivos moviles
  socialLinks.forEach(socialLink => {
    socialLink.addEventListener("click", handleSocialLinkClick);
  });

  // Función para manejar el clic en los logos en dispositivos moviles
  function handleSocialLinkClick(event) {
    const socialLink = event.currentTarget;
    const profile = socialLink.getAttribute("data-profile");
    const profileData = getProfileData(profile);

    const userWantsToRedirect = confirm(`Do you want to visit ${profile} page?`);
    
    if (userWantsToRedirect) {
      window.location.href = profileData.info;
    }
  }


// Obtener todos los elementos del acordeón
const accordionItems = document.querySelectorAll('.accordionItem');

  accordionItems.forEach((item) => {
    const title = item.querySelector('.accordionItem_title');
    const content = item.querySelector('.accordionItem_content');

    title.addEventListener('click', () => {
      content.classList.toggle('collapsed');
      title.classList.toggle('active');

      if (content.classList.contains('collapsed')) {
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });

    content.style.maxHeight = 0;
    content.classList.add('collapsed');
  });
  const educationCarousel = $(".education-carousel");
  if (educationCarousel.length) {
    initializeSlickCarousel(educationCarousel);
  }

  // Función para agregar la funcionalidad del acordeón
  function toggleAccordion() {
    const accordionTitles = document.querySelectorAll('.accordionItem_title');
    const accordionContents = document.querySelectorAll('.accordionItem_content');
    
    accordionTitles.forEach((title) => {
      title.addEventListener('click', () => {
        const content = title.nextElementSibling;
        
        title.classList.toggle('active');
        content.classList.toggle('collapsed');
        
        if (content.classList.contains('collapsed')) {
          content.style.maxHeight = null;
        } else {
          content.style.maxHeight = content.scrollHeight + 'px';
        }
      });
    });

    accordionContents.forEach((content) => {
      content.style.maxHeight = 0;
      content.classList.add('collapsed');
    });
  }

  // Llama a la función para agregar la funcionalidad del acordeón
  toggleAccordion();
});

// main.js
function toggleContent() {
  const experienceList = document.querySelector('.experience-list');
  const accordion = document.querySelector('.ohio-accordion-sс');

  if (window.innerWidth <= 768) {
    experienceList.style.display = 'block';
    accordion.style.display = 'none';
  } else {
    experienceList.style.display = 'none';
    accordion.style.display = 'block';
  }
}

// Ejecutar al cargar la página y cuando se cambie el tamaño de la ventana
toggleContent();
window.addEventListener('resize', toggleContent);

function initializeSlickCarousel(carouselElement) {
  carouselElement.slick({
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
    // Otras opciones adicionales
  });
}



