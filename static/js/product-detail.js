// static/js/product-detail.js
(function () {
  const gallery = document.querySelector('#pd-gallery');
  if (!gallery || typeof Swiper === 'undefined') return;
  if (gallery.dataset.inited) return; // prevent double init
  gallery.dataset.inited = '1';

  // Thumbnails
  const thumbsSwiper = new Swiper('.thumbs-swiper', {
    slidesPerView: 'auto',
    spaceBetween: 8,
    freeMode: true,
    watchSlidesProgress: false
  });

  // Main swiper
  const mainSwiper = new Swiper('.main-swiper', {
    slidesPerView: 1,
    spaceBetween: 0,
    centeredSlides: false,
    autoHeight: false,
    watchOverflow: true,
    thumbs: { swiper: thumbsSwiper }
  });

  // Click main image to go to next slide
  document.querySelectorAll('.main-swiper .swiper-slide').forEach(slide => {
    slide.addEventListener('click', () => {
      mainSwiper.slideNext();
    });
  });

  // PhotoSwipe lightbox
  if (window.PhotoSwipeLightbox && window.PhotoSwipe) {
    const lightbox = new PhotoSwipeLightbox({
      gallery: '#pd-gallery',
      children: 'a.pswp-trigger',
      pswpModule: PhotoSwipe,
      loop: true,
      padding: { top: 20, right: 20, bottom: 20, left: 20 }
    });
    lightbox.init();
  }

  // Ensure Swiper recalculates after layout
  const update = () => {
    try { mainSwiper.update(); thumbsSwiper.update(); } catch (e) {}
  };
  window.addEventListener('load', update);
  setTimeout(update, 100);
})();
