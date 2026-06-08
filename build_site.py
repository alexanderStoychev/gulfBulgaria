#!/usr/bin/env python3
"""Generates all HTML pages for the Gulf Oil Bulgaria site from shared templates.
Run with: python3 build_site.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300&family=Barlow+Condensed:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
"""

TOPBAR = """<!-- TOP BAR -->
<div class="top-bar">
  <div class="top-bar-inner">
    <a href="#">Вход за клиенти</a>
    <div class="top-bar-divider"></div>
    <a href="#">Gulf Extranet</a>
    <div class="top-bar-divider"></div>
    <a href="#">Смяна на страна</a>
  </div>
</div>
"""

NAV = """<!-- NAV -->
<div class="nav-wrapper">
  <nav id="main-nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo">
        <img src="images/gulf-logo.png" alt="Gulf Oil">
      </a>

      <ul class="nav-links">

        <li>
          <span>Продукти <span class="chevron">▾</span></span>
          <div class="dropdown dropdown-wide">
            <div class="dropdown-col">
              <div class="dropdown-label">Автомобилни</div>
              <a href="product-auto-passenger.html">Леки автомобили</a>
              <a href="product-auto-motorcycle.html">Мотоциклетни масла</a>
              <a href="product-auto-commercial.html">Търговски превозни средства</a>
            </div>
            <div class="dropdown-col">
              <div class="dropdown-label">Земеделие</div>
              <a href="product-agri-engine-oil.html">Моторни масла</a>
              <a href="product-agri-transmission.html">Трансмисионни течности</a>
              <a href="product-agri-hydraulic.html">Хидравлични масла</a>
              <a href="product-agri-stou.html">STOU масла</a>
              <a href="product-agri-chain.html">Верижни масла</a>
            </div>
            <div class="dropdown-col">
              <div class="dropdown-label">Индустрия и море</div>
              <a href="product-ind-industrial.html">Индустриални масла</a>
              <a href="product-ind-hydraulic.html">Хидравлични масла</a>
              <a href="product-ind-heat-transfer.html">Масла за топлопренос</a>
              <a href="product-marine-lubricants.html">Морски смазочни материали</a>
              <div class="dropdown-label" style="margin-top:12px;">Инструменти</div>
              <a href="https://europe.gulfoilltd.com/lubricantadvisor" target="_blank">Съветник за смазочни материали</a>
              <a href="#">Намиране на продукт</a>
            </div>
          </div>
        </li>

        <li>
          <span>Услуги <span class="chevron">▾</span></span>
          <div class="dropdown">
            <div class="dropdown-section">
              <a href="services.html">Горивна търговия</a>
              <a href="dealer-locator.html">Намиране на дилър</a>
            </div>
          </div>
        </li>

        <li>
          <span>Партньорства <span class="chevron">▾</span></span>
          <div class="dropdown">
            <div class="dropdown-section">
              <a href="partnerships.html#williams">Williams Racing</a>
              <a href="partnerships.html#trackhouse">Trackhouse / MotoGP</a>
              <a href="partnerships.html#mclaren">McLaren Automotive</a>
              <a href="partnerships.html#everrati">Everrati</a>
              <a href="partnerships.html#rofgo">ROFGO</a>
              <a href="partnerships.html#tagheuer">TAG Heuer</a>
            </div>
          </div>
        </li>

        <li><a href="motorsport.html">Мотоспорт</a></li>

        <li>
          <span>Новини <span class="chevron">▾</span></span>
          <div class="dropdown">
            <div class="dropdown-section">
              <a href="news.html">Всички новини</a>
              <a href="news.html#press">Прес съобщения</a>
            </div>
          </div>
        </li>

        <li>
          <span>За нас <span class="chevron">▾</span></span>
          <div class="dropdown">
            <div class="dropdown-section">
              <a href="about.html">Кои сме ние</a>
              <a href="about.html#history">Нашата история</a>
              <a href="about.html#culture">Култура и ценности</a>
              <a href="about.html#leadership">Ръководство</a>
              <a href="about.html#sustainability">Устойчивост</a>
            </div>
          </div>
        </li>

        <li>
          <span>Контакт <span class="chevron">▾</span></span>
          <div class="dropdown">
            <div class="dropdown-section">
              <a href="contact.html">Свържете се с нас</a>
              <a href="contact.html#distributor">Станете дистрибутор</a>
            </div>
          </div>
        </li>

      </ul>

      <div class="nav-actions">
        <button class="nav-mobile-btn" aria-label="Меню">
          <span></span><span></span><span></span>
        </button>
      </div>

    </div>
  </nav>
</div>
"""

FOOTER = """<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="images/logo-gulf-disc.png" alt="Gulf Oil" class="footer-logo">
        <p class="footer-tagline">Водещ световен доставчик на смазочни материали с над 120 години опит.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a>
          <a href="#" class="social-btn">in</a>
          <a href="#" class="social-btn">YT</a>
          <a href="#" class="social-btn">X</a>
        </div>
      </div>

      <div>
        <div class="footer-col-title">Продукти</div>
        <ul class="footer-links">
          <li><a href="product-auto-passenger.html">Леки автомобили</a></li>
          <li><a href="product-auto-motorcycle.html">Мотоциклетни масла</a></li>
          <li><a href="product-auto-commercial.html">Търговски превозни средства</a></li>
          <li><a href="products-agriculture.html">Земеделска техника</a></li>
          <li><a href="product-ind-industrial.html">Индустриални масла</a></li>
          <li><a href="product-marine-lubricants.html">Морски смазочни материали</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-col-title">Компания</div>
        <ul class="footer-links">
          <li><a href="about.html">Кои сме ние</a></li>
          <li><a href="about.html#history">Нашата история</a></li>
          <li><a href="motorsport.html">Мотоспорт</a></li>
          <li><a href="partnerships.html">Партньорства</a></li>
          <li><a href="about.html#sustainability">Устойчивост</a></li>
          <li><a href="news.html">Новини</a></li>
        </ul>
      </div>

      <div>
        <div class="footer-col-title">Услуги</div>
        <ul class="footer-links">
          <li><a href="dealer-locator.html">Намери дилър</a></li>
          <li><a href="https://europe.gulfoilltd.com/lubricantadvisor" target="_blank">Съветник за масла</a></li>
          <li><a href="services.html">Горивна търговия</a></li>
          <li><a href="contact.html#distributor">Станете дистрибутор</a></li>
          <li><a href="#">Вход за клиенти</a></li>
          <li><a href="contact.html">Контакт</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="footer-copy">© 2026 Gulf Oil България. Всички права запазени.</div>
      <div class="footer-legal">
        <a href="#">Политика за поверителност</a>
        <a href="#">Условия за ползване</a>
        <a href="#">Управление на бисквитки</a>
      </div>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""

PAGE_HERO_CSS_NOTE = ""  # placeholder, styles live in style.css


def make_page(filename, title, description, body):
    html = HEAD.format(title=title, description=description) + TOPBAR + NAV + body + FOOTER
    path = os.path.join(ROOT, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Wrote {filename} ({len(html)} bytes)")


# ============================================================
# Page bodies are defined in companion module page_content.py
# ============================================================
from page_content import PAGES

for fname, (title, desc, body) in PAGES.items():
    make_page(fname, title, desc, body)

print("Done.")
