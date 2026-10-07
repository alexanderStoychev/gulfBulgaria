(() => {
  const items = [...document.querySelectorAll('.hs-item')];
  const lis = [...document.querySelectorAll('.hs-years li')];
  const nav = document.querySelector('.hs-nav');
  const years = document.querySelector('.hs-years');
  if (!items.length || !lis.length) return;

  const reveal = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('is-in');
        reveal.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.05 });
  items.forEach((it) => reveal.observe(it));

  const isRow = () => window.matchMedia('(max-width: 900px)').matches;
  let activeYear = null;

  function setActive(year) {
    if (year === activeYear) return;
    activeYear = year;
    let seen = false;
    lis.forEach((li) => {
      const on = li.dataset.year === year;
      li.classList.toggle('is-active', on);
      li.classList.toggle('is-past', !seen && !on);
      if (on) seen = true;
    });
    const li = lis.find((l) => l.dataset.year === year);
    if (!li) return;
    years.style.setProperty('--hs-progress', `${li.offsetTop + li.offsetHeight / 2}px`);
    if (isRow()) {
      nav.scrollTo({ left: years.offsetLeft + li.offsetLeft - (nav.clientWidth - li.offsetWidth) / 2, behavior: 'smooth' });
    } else {
      nav.scrollTo({ top: years.offsetTop + li.offsetTop - (nav.clientHeight - li.offsetHeight) / 2, behavior: 'smooth' });
    }
  }

  let ticking = false;
  function update() {
    ticking = false;
    const line = window.innerHeight * 0.42;
    let cur = items[0];
    for (const it of items) {
      if (it.getBoundingClientRect().top <= line) cur = it;
      else break;
    }
    setActive(cur.dataset.group);
  }
  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
  window.addEventListener('resize', () => { activeYear = null; update(); });

  lis.forEach((li) => {
    li.querySelector('a').addEventListener('click', (ev) => {
      ev.preventDefault();
      const target = items.find((it) => it.dataset.group === li.dataset.year);
      if (!target) return;
      const offset = isRow() ? 150 : 120;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset, behavior: 'smooth' });
    });
  });

  update();
})();
