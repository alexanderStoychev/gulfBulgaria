(() => {
  const toc = document.querySelector('.legal-toc');
  if (!toc) return;
  const links = [...toc.querySelectorAll('a')];
  const secs = links.map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);

  // contents list: always open on desktop, collapsed on small screens
  const wide = window.matchMedia('(min-width: 1001px)');
  const sync = () => { toc.open = wide.matches; };
  sync();
  wide.addEventListener('change', sync);
  toc.querySelector('summary').addEventListener('click', (e) => { if (wide.matches) e.preventDefault(); });

  // highlight the section being read
  let ticking = false;
  const update = () => {
    ticking = false;
    const line = window.innerHeight * 0.3;
    let cur = secs[0];
    for (const s of secs) { if (s.getBoundingClientRect().top <= line) cur = s; else break; }
    links.forEach((a) => a.classList.toggle('is-active', cur && a.getAttribute('href') === '#' + cur.id));
  };
  window.addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(update); ticking = true; } }, { passive: true });
  update();
})();
