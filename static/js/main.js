/**
* Template Name: Gp
* Updated: Sep 18 2023 with Bootstrap v5.3.2
* Template URL: https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
    "use strict";
  
    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
      el = el.trim()
      if (all) {
        return [...document.querySelectorAll(el)]
      } else {
        return document.querySelector(el)
      }
    }
  
    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
      let selectEl = select(el, all)
      if (selectEl) {
        if (all) {
          selectEl.forEach(e => e.addEventListener(type, listener))
        } else {
          selectEl.addEventListener(type, listener)
        }
      }
    }
  
    /**
     * Easy on scroll event listener 
     */
    const onscroll = (el, listener) => {
      el.addEventListener('scroll', listener)
    }
  
    /**
     * Navbar links active state on scroll
     */
    let navbarlinks = select('#navbar .scrollto', true)
    const navbarlinksActive = () => {
      let position = window.scrollY + 200
      navbarlinks.forEach(navbarlink => {
        if (!navbarlink.hash) return
        let section = select(navbarlink.hash)
        if (!section) return
        if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
          navbarlink.classList.add('active')
        } else {
          navbarlink.classList.remove('active')
        }
      })
    }
    window.addEventListener('load', navbarlinksActive)
    onscroll(document, navbarlinksActive)
  
    /**
     * Scrolls to an element with header offset
     */
    const scrollto = (el) => {
      let header = select('#header')
      let offset = header.offsetHeight
  
      let elementPos = select(el).offsetTop
      window.scrollTo({
        top: elementPos - offset,
        behavior: 'smooth'
      })
    }
  
    /**
     * Toggle .header-scrolled class to #header when page is scrolled
     */
    let selectHeader = select('#header')
    if (selectHeader) {
      const headerScrolled = () => {
        if (window.scrollY > 100) {
          selectHeader.classList.add('header-scrolled')
        } else {
          selectHeader.classList.remove('header-scrolled')
        }
      }
      window.addEventListener('load', headerScrolled)
      onscroll(document, headerScrolled)
    }
  
    /**
     * Back to top button
     */
    let backtotop = select('.back-to-top')
    if (backtotop) {
      const toggleBacktotop = () => {
        if (window.scrollY > 100) {
          backtotop.classList.add('active')
        } else {
          backtotop.classList.remove('active')
        }
      }
      window.addEventListener('load', toggleBacktotop)
      onscroll(document, toggleBacktotop)
    }
  
    /**
     * Mobile nav toggle
     */
    on('click', '.mobile-nav-toggle', function(e) {
      select('#navbar').classList.toggle('navbar-mobile')
      this.classList.toggle('bi-list')
      this.classList.toggle('bi-x')
    })
  
    /**
     * Mobile nav dropdowns activate
     */
    on('click', '.navbar .dropdown > a', function(e) {
      if (select('#navbar').classList.contains('navbar-mobile')) {
        e.preventDefault()
        this.nextElementSibling.classList.toggle('dropdown-active')
      }
    }, true)
  
    /**
     * Scrool with ofset on links with a class name .scrollto
     */
    on('click', '.scrollto', function(e) {
      if (select(this.hash)) {
        e.preventDefault()
  
        let navbar = select('#navbar')
        if (navbar.classList.contains('navbar-mobile')) {
          navbar.classList.remove('navbar-mobile')
          let navbarToggle = select('.mobile-nav-toggle')
          navbarToggle.classList.toggle('bi-list')
          navbarToggle.classList.toggle('bi-x')
        }
        scrollto(this.hash)
      }
    }, true)
  
    /**
     * Scroll with ofset on page load with hash links in the url
     */
    window.addEventListener('load', () => {
      if (window.location.hash) {
        if (select(window.location.hash)) {
          scrollto(window.location.hash)
        }
      }
    });
  
    /**
     * Preloader
     */
    let preloader = select('#preloader');
    if (preloader) {
      window.addEventListener('load', () => {
        preloader.remove()
      });
    }
  
    /**
     * Clients Slider
     */
    new Swiper('.clients-slider', {
      speed: 400,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false
      },
      slidesPerView: 'auto',
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
      },
      breakpoints: {
        320: {
          slidesPerView: 2,
          spaceBetween: 40
        },
        480: {
          slidesPerView: 3,
          spaceBetween: 60
        },
        640: {
          slidesPerView: 4,
          spaceBetween: 80
        },
        992: {
          slidesPerView: 6,
          spaceBetween: 120
        }
      }
    });
  
    /**
     * Porfolio isotope and filter
     */
    window.addEventListener('load', () => {
      let portfolioContainer = select('.portfolio-container');
      if (portfolioContainer) {
        let portfolioIsotope = new Isotope(portfolioContainer, {
          itemSelector: '.portfolio-item'
        });
  
        let portfolioFilters = select('#portfolio-flters li', true);
  
        on('click', '#portfolio-flters li', function(e) {
          e.preventDefault();
          portfolioFilters.forEach(function(el) {
            el.classList.remove('filter-active');
          });
          this.classList.add('filter-active');
  
          portfolioIsotope.arrange({
            filter: this.getAttribute('data-filter')
          });
          portfolioIsotope.on('arrangeComplete', function() {
            AOS.refresh()
          });
        }, true);
      }
  
    });
  
    /**
     * Initiate portfolio lightbox 
     */
    const portfolioLightbox = GLightbox({
      selector: '.portfolio-lightbox'
    });
  
    /**
     * Portfolio details slider
     */
    new Swiper('.portfolio-details-slider', {
      speed: 400,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false
      },
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
      }
    });
  
    /**
     * Testimonials slider
     */
    new Swiper('.testimonials-slider', {
      speed: 600,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false
      },
      slidesPerView: 'auto',
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
      }
    });
  
    /**
     * Animation on scroll
     */
    window.addEventListener('load', () => {
      AOS.init({
        duration: 1000,
        easing: "ease-in-out",
        once: true,
        mirror: false
      });
    });
    
  
    /**
     * Initiate Pure Counter 
     */
    new PureCounter();
  
  })()
  //Map
let currentStartIndexClimatology = 0;
let currentStartIndexBiodiversity = 0;
let currentStartIndexMolecular = 0;
let currentStartIndexDisease = 0;

const cardsPerPage = 4;
const climatologyCards = document.querySelectorAll('#slider-container-climatology .my-card');
const biodiversityCards = document.querySelectorAll('#slider-container-biodiversity .my-card');
const molecularCards = document.querySelectorAll('#slider-container-Molecular .my-card');
const diseaseCards = document.querySelectorAll('#slider-container-Disease .my-card');

const totalClimatologyCards = climatologyCards.length;
const totalBiodiversityCards = biodiversityCards.length;
const totalMolecularCards = molecularCards.length;
const totalDiseaseCards = diseaseCards.length;

function navigateCards(direction, category) {
  let currentStartIndex;
  let totalCards;
  let cards;

  switch (category) {
    case 'Climatology':
      currentStartIndex = currentStartIndexClimatology;
      totalCards = totalClimatologyCards;
      cards = climatologyCards;
      break;
    case 'Biodiversity':
      currentStartIndex = currentStartIndexBiodiversity;
      totalCards = totalBiodiversityCards;
      cards = biodiversityCards;
      break;
    case 'Molecular':
      currentStartIndex = currentStartIndexMolecular;
      totalCards = totalMolecularCards;
      cards = molecularCards;
      break;
    case 'Disease':
      currentStartIndex = currentStartIndexDisease;
      totalCards = totalDiseaseCards;
      cards = diseaseCards;
      break;
    default:
      return; // Unknown category
  }

  if (direction === 'left') {
    currentStartIndex = Math.max(currentStartIndex - cardsPerPage, 0);
  } else if (direction === 'right') {
    currentStartIndex = Math.min(currentStartIndex + cardsPerPage, totalCards - cardsPerPage);
  }

  switch (category) {
    case 'Climatology':
      currentStartIndexClimatology = currentStartIndex;
      updateCardVisibility(category, currentStartIndexClimatology, cards);
      break;
    case 'Biodiversity':
      currentStartIndexBiodiversity = currentStartIndex;
      updateCardVisibility(category, currentStartIndexBiodiversity, cards);
      break;
    case 'Molecular':
      currentStartIndexMolecular = currentStartIndex;
      updateCardVisibility(category, currentStartIndexMolecular, cards);
      break;
    case 'Disease':
      currentStartIndexDisease = currentStartIndex;
      updateCardVisibility(category, currentStartIndexDisease, cards);
      break;
    default:
      return;
  }
}

function updateCardVisibility(category, startIndex, cards) {
  cards.forEach((card, index) => {
    const isVisible = index >= startIndex && index < startIndex + cardsPerPage;
    card.style.display = isVisible ? 'block' : 'none';
  });
}

// Show the initial set of cards for all categories
updateCardVisibility('Climatology', currentStartIndexClimatology, climatologyCards);
updateCardVisibility('Biodiversity', currentStartIndexBiodiversity, biodiversityCards);
updateCardVisibility('Molecular', currentStartIndexMolecular, molecularCards);
updateCardVisibility('Disease', currentStartIndexDisease, diseaseCards);

// auto copy
document.getElementById('citation').addEventListener('click', function() {
  // Create a temporary textarea to hold the text
  var textArea = document.createElement('textarea');
  textArea.value = "Citation: Barry, Tom. “Arctic Species Trend Index (ASTI) : Freshwater.” Www.gbif.org, www.gbif.org/dataset/ebc62d60-afa9-4396-9e93-a0354d448b83/metrics, https://doi.org/10.15468/dtfeld. Accessed 4 Feb. 2024";

  // Append the textarea to the document
  document.body.appendChild(textArea);

  // Select the text in the textarea
  textArea.select();
  textArea.setSelectionRange(0, 99999); // For mobile devices

  // Copy the text to the clipboard
  document.execCommand('copy');

  // Remove the temporary textarea
  document.body.removeChild(textArea);

  alert('Citation copied to clipboard!');
});  

