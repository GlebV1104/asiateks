// static/js/product-detail.js
(function () {
  function init() {
    const gallery = document.querySelector('#pd-gallery');
    if (!gallery || typeof Swiper === 'undefined') return;
    if (gallery.dataset.inited) return; // prevent double init
    gallery.dataset.inited = '1';

    // Thumbnails
    const thumbsSwiper = new Swiper('.thumbs-swiper', {
      slidesPerView: 'auto',
      spaceBetween: 8,
      freeMode: true,
      watchSlidesProgress: true,     // important for thumbs sync
      slideToClickedSlide: true
    });

    // Main swiper
    const mainSwiper = new Swiper('.main-swiper', {
      slidesPerView: 1,
      spaceBetween: 0,
      centeredSlides: false,
      autoHeight: false,
      watchOverflow: true,
      thumbs: { swiper: thumbsSwiper },
      // Let links be clickable even inside a slide
      preventClicks: false,
      preventClicksPropagation: false
    });

    // Click *empty* slide area to go next (but don't steal <a> clicks)
    document.querySelectorAll('.main-swiper .swiper-slide').forEach(slide => {
      slide.addEventListener('click', (e) => {
        if (e.target.closest('a')) return; // let anchor open PhotoSwipe
        mainSwiper.slideNext();
      });
    });

    // PhotoSwipe lightbox (init when available)
    function initLightbox() {
      if (!window.PhotoSwipeLightbox || !window.PhotoSwipe) return;
      if (gallery.dataset.lbInited) return;
      gallery.dataset.lbInited = '1';

      const lightbox = new PhotoSwipeLightbox({
        gallery: '#pd-gallery',
        children: 'a.pswp-trigger',
        pswpModule: PhotoSwipe,
        loop: true,
        padding: { top: 20, right: 20, bottom: 20, left: 20 }
      });
      lightbox.init();

      // Optional: button to open first image
      const zoomBtn = document.querySelector('.zoom-trigger');
      if (zoomBtn) {
        zoomBtn.addEventListener('click', () => {
          const firstA = document.querySelector('#pd-gallery a.pswp-trigger');
          if (firstA) firstA.click();
        });
      }
    }

    // Try now and also after load (covers any late script execution)
    initLightbox();
    window.addEventListener('DOMContentLoaded', initLightbox);
    window.addEventListener('load', initLightbox);

    // Ensure Swiper recalculates after layout
    const update = () => {
      try { mainSwiper.update(); thumbsSwiper.update(); } catch (e) {}
    };
    window.addEventListener('load', update);
    setTimeout(update, 100);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
