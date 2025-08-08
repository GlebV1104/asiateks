// Initialize the Mobile Products Swiper (example #1)
var swiper = new Swiper(".mobile-swiper-container", {
  loop: true,
  spaceBetween: 20,
  speed: 300,
  slidesPerView: 1, // default on mobile
  breakpoints: {
    768: { slidesPerView: 2, spaceBetween: 20 },
    1024: { slidesPerView: 4, spaceBetween: 20 }
  },
  navigation: {
    nextEl: ".mobile-swiper-button-next",
    prevEl: ".mobile-swiper-button-prev"
  },
  wrapperClass: "mobile-swiper-wrapper",
  slideClass: "mobile-swiper-slide"
});

// Initialize the second example slider
var swiper2 = new Swiper(".mobile-swiper-container2", {
  loop: true,
  spaceBetween: 20,
  speed: 300,
  slidesPerView: 1,
  breakpoints: {
    768: { slidesPerView: 2, spaceBetween: 20 },
    1024: { slidesPerView: 4, spaceBetween: 20 }
  },
  navigation: {
    nextEl: ".mobile-swiper-button-next2",
    prevEl: ".mobile-swiper-button-prev2"
  },
  wrapperClass: "mobile-swiper-wrapper2",
  slideClass: "mobile-swiper-slide2"
});

// Initialize the third slider
var swiper3 = new Swiper(".mobile-swiper-container3", {
  loop: true,
  spaceBetween: 20,
  speed: 300,
  slidesPerView: 1,
  breakpoints: {
    768: { slidesPerView: 2, spaceBetween: 20 },
    1024: { slidesPerView: 4, spaceBetween: 20 }
  },
  navigation: {
    nextEl: ".mobile-swiper-button-next3",
    prevEl: ".mobile-swiper-button-prev3"
  },
  wrapperClass: "mobile-swiper-wrapper3",
  slideClass: "mobile-swiper-slide3"
});

document.addEventListener('DOMContentLoaded', function(){
  var productDetailSwiper = new Swiper(".product-detail-slider-container", {
    loop: true,
    spaceBetween: 20,
    speed: 300,
    slidesPerView: 2, // Show 2 slides on mobile
    breakpoints: {
      768: { slidesPerView: 3, spaceBetween: 20 },
      1024: { slidesPerView: 4, spaceBetween: 20 }
    },
    // Navigation selectors remain the same as in HTML
    navigation: {
      nextEl: ".product-detail-slider-button-next",
      prevEl: ".product-detail-slider-button-prev"
    },
    pagination: {
      el: ".product-detail-slider-pagination",
      clickable: true,
    }
  });
});

// Store the last scroll position
var lastScrollTop = 0;

window.addEventListener("scroll", function() {
  var navbar = document.querySelector(".navbar");
  var currentScroll = window.pageYOffset || document.documentElement.scrollTop;

  // Check if scrolling down
  if (currentScroll > lastScrollTop) {
    // Scroll down: hide the navbar by moving it off-screen (adjust -100px as needed)
    navbar.style.top = "-100px";
  } else {
    // Scrolling up: show the navbar
    navbar.style.top = "0";
  }
  
  // Update the last scroll position, ensuring it never goes negative
  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});