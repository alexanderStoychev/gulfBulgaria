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

// Mobile navigation: menu button, tap-to-expand sections, close on link / Esc / outside tap
const navWrapper = document.querySelector('.nav-wrapper');
const menuBtn = document.querySelector('.nav-mobile-btn');
const navLinks = document.querySelector('.nav-links');
if (navWrapper && menuBtn && navLinks) {
  const mobileMq = window.matchMedia('(max-width: 1140px)');
  navLinks.id = navLinks.id || 'nav-menu';
  menuBtn.setAttribute('aria-controls', navLinks.id);
  menuBtn.setAttribute('aria-expanded', 'false');

  const setOpen = (open) => {
    navWrapper.classList.toggle('menu-open', open);
    document.body.classList.toggle('menu-lock', open && mobileMq.matches);
    menuBtn.setAttribute('aria-expanded', String(open));
    if (!open) navLinks.querySelectorAll(':scope > li.open').forEach((li) => {
      li.classList.remove('open');
      li.querySelector(':scope > span')?.setAttribute('aria-expanded', 'false');
    });
  };
  menuBtn.addEventListener('click', () => setOpen(!navWrapper.classList.contains('menu-open')));

  navLinks.querySelectorAll(':scope > li').forEach((li) => {
    const label = li.querySelector(':scope > span');
    if (!label || !li.querySelector('.dropdown')) return;
    label.setAttribute('role', 'button');
    label.setAttribute('tabindex', '0');
    label.setAttribute('aria-expanded', 'false');
    const toggle = () => {
      if (!mobileMq.matches) return;
      const wasOpen = li.classList.contains('open');
      navLinks.querySelectorAll(':scope > li.open').forEach((o) => {
        o.classList.remove('open');
        o.querySelector(':scope > span')?.setAttribute('aria-expanded', 'false');
      });
      li.classList.toggle('open', !wasOpen);
      label.setAttribute('aria-expanded', String(!wasOpen));
    };
    label.addEventListener('click', toggle);
    label.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
    });
  });

  navLinks.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  document.addEventListener('click', (e) => { if (!navWrapper.contains(e.target)) setOpen(false); });
  mobileMq.addEventListener('change', () => setOpen(false));
}
