// Sticky nav scroll effect
const nav = document.getElementById('main-nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
});

// Scroll reveal
const revealEls = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });

revealEls.forEach(el => observer.observe(el));

// Hero background parallax on scroll
const heroBg = document.querySelector('.hero-bg');
if (heroBg) {
  let heroTicking = false;
  const updateHeroParallax = () => {
    const offset = window.scrollY * 0.35;
    heroBg.style.transform = `scale(1.3) translateY(${offset}px)`;
    heroTicking = false;
  };
  window.addEventListener('scroll', () => {
    if (!heroTicking) {
      requestAnimationFrame(updateHeroParallax);
      heroTicking = true;
    }
  });
  updateHeroParallax();
}

// Videos marked data-autoplay-view play (muted) while on screen and pause when scrolled away
const autoVideos = document.querySelectorAll('video[data-autoplay-view]');
if (autoVideos.length) {
  const videoObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const v = entry.target;
      if (entry.isIntersecting && entry.intersectionRatio >= 0.35) {
        if (v.dataset.userPaused !== '1') {
          const p = v.play();
          if (p) p.catch(() => {});
        }
      } else if (!entry.isIntersecting || entry.intersectionRatio < 0.1) {
        v._autoPause = true;
        v.pause();
        v.dataset.userPaused = '';
      }
    });
  }, { threshold: [0, 0.1, 0.35, 0.6] });
  autoVideos.forEach((v) => {
    v.muted = true;
    v.addEventListener('pause', () => {
      if (v._autoPause) { v._autoPause = false; return; }
      v.dataset.userPaused = '1';
    });
    v.addEventListener('play', () => { v.dataset.userPaused = ''; });
    videoObserver.observe(v);
  });
}
