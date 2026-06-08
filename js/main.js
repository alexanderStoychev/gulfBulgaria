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
    heroBg.style.transform = `scale(1.08) translateY(${offset}px)`;
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
