# Body content (between NAV and FOOTER) for every page.
# title, description, body_html
#
# Design note: no emoji glyphs anywhere. Icons are small CSS badges (letterforms /
# simple shapes) consistent with the Gulf disc brand system, or real photography.

PAGES = {}

def icon(label):
    """Small square brand-style icon badge with a 1-2 letter mark."""
    return f'<span class="icon-badge">{label}</span>'

# ============================================================
# HOMEPAGE
# ============================================================
PAGES['index.html'] = (
"Gulf Oil България — Смазочни материали и горива",
"Gulf Oil България — водещ доставчик на смазочни материали, горива и услуги с над 120 години история.",
"""
<!-- HERO -->
<section class="hero" style="padding:0;">
  <div class="hero-bg" style="background-image:url('images/mclaren-artura-road.jpg');"></div>
  <div class="hero-overlay"></div>
  <div class="hero-overlay-bottom"></div>
  <div class="hero-content">
    <div class="hero-eyebrow">
      <span class="hero-eyebrow-dot"></span>
      От 1901 година
    </div>
    <h1 class="hero-title">
      Заедно сме
      <span>Неудържими</span>
    </h1>
    <p class="hero-subtitle">
      Водещ доставчик на горива, смазочни материали и услуги — изградени върху над 120 години опит и страст.
    </p>
    <div class="hero-actions">
      <a href="products-automotive.html" class="btn-primary">Разгледай продукти ›</a>
      <a href="about.html" class="btn-ghost">За нас</a>
    </div>
  </div>

  <div class="hero-stats">
    <div class="hero-stat">
      <div class="hero-stat-num">120<span>+</span></div>
      <div class="hero-stat-label">Години история</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">100<span>+</span></div>
      <div class="hero-stat-label">Страни в света</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">6<span>k+</span></div>
      <div class="hero-stat-label">Продукта</div>
    </div>
  </div>
</section>

<!-- LUBRICANT ADVISOR BANNER -->
<div class="advisor-banner">
  <div class="advisor-inner">
    <div class="advisor-text">
      <div class="advisor-icon">A</div>
      <div>
        <div class="advisor-label">Съветник за смазочни материали</div>
        <div class="advisor-sub">Намерете правилния продукт за вашето превозно средство за секунди</div>
      </div>
    </div>
    <a href="https://europe.gulfoilltd.com/lubricantadvisor" target="_blank" class="advisor-btn">Намери продукт ›</a>
  </div>
</div>

<!-- PRODUCTS -->
<section class="products-section">
  <div class="products-corner"></div>
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Нашите продукти</div>
        <h2 class="section-title">Смазочни материали<br><span>за всяка нужда</span></h2>
        <p class="section-body">От леки автомобили до тежка индустрия — Gulf предлага решения с доказано качество.</p>
      </div>
      <a href="products-automotive.html" class="view-all">Всички продукти →</a>
    </div>

    <div class="product-grid">
      <a href="products-automotive.html#cars" class="product-card shard-card reveal reveal-delay-1">
        <div class="product-card-img">
          <img src="images/product-automotive.jpg" alt="Автомобилни масла">
          <div class="shard-corner" style="background-image:url('images/gulf-shard-1.jpg');"></div>
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Автомобилни</div>
          <div class="product-card-title">Леки автомобили</div>
          <div class="product-card-desc">Пълна гама от синтетични и полусинтетични масла за леки автомобили с бензинови и дизелови двигатели.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>

      <a href="products-automotive.html#commercial" class="product-card shard-card reveal reveal-delay-2">
        <div class="product-card-img">
          <img src="images/trackhouse-race-3.jpg" alt="Търговски превозни средства">
          <div class="shard-corner" style="background-image:url('images/gulf-shard-2.jpg');"></div>
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Автомобилни</div>
          <div class="product-card-title">Търговски превозни средства</div>
          <div class="product-card-desc">Специализирани продукти за камиони, автобуси и тежкотоварни превозни средства.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>

      <a href="products-agriculture.html" class="product-card shard-card reveal reveal-delay-3">
        <div class="product-card-img">
          <img src="images/agri-hero.jpg" alt="Земеделска техника">
          <div class="shard-corner" style="background-image:url('images/gulf-shard-3.jpg');"></div>
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Земеделие</div>
          <div class="product-card-title">Земеделска техника</div>
          <div class="product-card-desc">Масла и трансмисионни течности, разработени за тежките условия на земеделска работа.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>

      <a href="products-industrial-marine.html#marine" class="product-card shard-card reveal reveal-delay-4">
        <div class="product-card-img">
          <img src="images/product-marine.jpg" alt="Морски смазочни материали" style="object-position: 15% 35%;">
          <div class="shard-corner" style="background-image:url('images/gulf-shard-4.jpg');"></div>
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Море</div>
          <div class="product-card-title">Морски смазочни материали</div>
          <div class="product-card-desc">Продукти, сертифицирани за морска употреба — от рибарски лодки до търговски кораби.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- ABOUT SPLIT -->
<div class="about-section">
  <div class="about-grid">
    <div class="about-image">
      <img src="images/about-team.jpg" alt="Gulf в моторните спортове">
      <div class="about-image-overlay"></div>
    </div>
    <div class="about-content">
      <div class="about-corner"></div>
      <div style="position:relative; z-index:1;">
      <div class="section-label">За нас</div>
      <h2 class="section-title">Над 120 години<br><span>иновации</span></h2>
      <p class="section-body">
        Gulf Oil е една от най-разпознаваемите марки в световната петролна индустрия. Основана през 1901 г., днес Gulf е синоним на качество, надеждност и иновации в над 100 страни по света.
      </p>
      <p class="section-body" style="margin-top:16px;">
        Нашата мрежа в България предлага пълна гама от смазочни материали за автомобилния, земеделския, индустриалния и морския сектор.
      </p>
      <div class="about-stats-row">
        <div>
          <div class="about-stat-num">1901</div>
          <div class="about-stat-label">Година на основаване</div>
        </div>
        <div>
          <div class="about-stat-num">100+</div>
          <div class="about-stat-label">Страни</div>
        </div>
        <div>
          <div class="about-stat-num">6000+</div>
          <div class="about-stat-label">Продукта</div>
        </div>
      </div>
      <div style="margin-top:36px;">
        <a href="about.html#history" class="btn-primary">Нашата история →</a>
      </div>
      </div>
    </div>
  </div>
</div>

<!-- MOTORSPORT -->
<section class="motorsport-section" style="padding:0;">
  <div class="motorsport-bg" style="background-image:url('images/motorsport-bg.jpg');"></div>
  <div class="motorsport-inner">
    <div class="motorsport-grid">
      <div class="motorsport-content reveal">
        <div class="section-label">Мотоспорт</div>
        <h2 class="section-title">Страстта към<br><span>скоростта</span></h2>
        <p class="section-body">
          Gulf е неразривно свързан с motorsport от десетилетия. Нашето наследство на пистата е доказателство за качеството и производителността на продуктите ни.
        </p>
        <a href="motorsport.html" class="btn-primary" style="margin-top:8px;">Открий повече →</a>
        <div class="partnerships-row">
          <a href="partnerships.html#williams" class="partner-chip">Williams F1</a>
          <a href="partnerships.html#mclaren" class="partner-chip">McLaren Automotive</a>
          <a href="partnerships.html#trackhouse" class="partner-chip">Trackhouse MotoGP</a>
          <a href="partnerships.html#rofgo" class="partner-chip">ROFGO</a>
          <a href="partnerships.html#tagheuer" class="partner-chip">TAG Heuer</a>
          <a href="partnerships.html#everrati" class="partner-chip">Everrati</a>
        </div>
      </div>

      <div class="motorsport-image-stack reveal reveal-delay-2">
        <div class="ms-img ms-img-tall">
          <img src="images/mclaren-artura-front.jpg" alt="McLaren Artura"><span class="partner-caption">McLaren Automotive</span>
        </div>
        <div class="ms-img">
          <img src="images/tagheuer-detail.jpg" alt="TAG Heuer Monaco"><span class="partner-caption">TAG Heuer × Gulf</span>
        </div>
        <div class="ms-img">
          <img src="images/everrati-porsche.jpg" alt="Everrati електрическо Porsche">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SECTORS -->
<div class="sectors-section">
  <div class="sectors-grid">
    <a href="products-industrial-marine.html#industrial" class="sector-panel">
      <div class="sector-bg" style="background-image: url('images/sector-industrial.jpg');"></div>
      <div class="sector-overlay"></div>
      <div class="sector-content">
        <div class="sector-tag">Индустрия</div>
        <div class="sector-title">Индустриални<br>смазочни материали</div>
        <div class="sector-desc">Пълна гама от хидравлични масла, масла за редуктори, смазки и специализирани продукти за индустриални приложения.</div>
        <span class="sector-link">Виж продуктите →</span>
      </div>
    </a>
    <a href="products-industrial-marine.html#marine" class="sector-panel">
      <div class="sector-bg" style="background-image: url('images/sector-marine.jpg'); background-position: center 95%;"></div>
      <div class="sector-overlay"></div>
      <div class="sector-content">
        <div class="sector-tag">Море</div>
        <div class="sector-title">Морски<br>смазочни материали</div>
        <div class="sector-desc">Специализирани продукти за морски двигатели и системи, разработени да издържат на най-суровите морски условия.</div>
        <span class="sector-link">Виж продуктите →</span>
      </div>
    </a>
  </div>
</div>

<!-- NEWS -->
<section class="news-section">
  <div class="news-corner-bottom"></div>
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Новини</div>
        <h2 class="section-title">Последни<br><span>новини</span></h2>
      </div>
      <a href="news.html" class="view-all">Всички новини →</a>
    </div>

    <div class="news-grid">
      <a href="news.html#williams-2026" class="news-card featured reveal">
        <div class="news-card-img">
          <img src="images/news-featured.jpg" alt="Gulf Motorsport News">
        </div>
        <div class="news-card-body">
          <span class="news-card-tag">Мотоспорт</span>
          <div class="news-card-title">Gulf и Williams Racing обявяват нов сезон на партньорство</div>
          <div class="news-card-excerpt">Продължаваме нашето пътуване с един от най-емблематичните отбори във Формула 1, засилвайки нашето присъствие на пистата.</div>
          <div class="news-card-date">Юни 2026</div>
        </div>
      </a>

      <a href="news.html#gdi-line" class="news-card reveal reveal-delay-1">
        <div class="news-card-img">
          <img src="images/williams-1.jpg" alt="Продукти на Gulf">
        </div>
        <div class="news-card-body">
          <span class="news-card-tag">Продукти</span>
          <div class="news-card-title">Нова линия синтетични масла за GDI двигатели</div>
          <div class="news-card-excerpt">Gulf Ultrasynth GDI — разработена специално за директно впръскване.</div>
          <div class="news-card-date">Май 2026</div>
        </div>
      </a>

      <a href="news.html#sustainability" class="news-card reveal reveal-delay-2">
        <div class="news-card-img">
          <img src="images/news-secondary.jpg" alt="Устойчивост в Gulf">
        </div>
        <div class="news-card-body">
          <span class="news-card-tag">Устойчивост</span>
          <div class="news-card-title">Gulf ускорява своята програма за устойчивост</div>
          <div class="news-card-excerpt">Нашият ангажимент към по-зелено бъдеще чрез иновативни решения.</div>
          <div class="news-card-date">Април 2026</div>
        </div>
      </a>
    </div>
  </div>
</section>

""")

# ============================================================
# ABOUT
# ============================================================
PAGES['about.html'] = (
"Кои сме ние — Gulf Oil България",
"Научете повече за историята, ценностите, ръководството и ангажимента на Gulf Oil към устойчивост.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.94) 0%, rgba(27,45,107,0.88) 100%), url('images/about-team.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › За нас</div>
    <div class="page-hero-eyebrow">От 1901 година</div>
    <h1 class="page-hero-title">Кои сме <span>ние</span></h1>
    <p class="page-hero-sub">Повече от век по-късно, Gulf продължава да захранва амбициите на хора и индустрии в над 100 държави — със страст към качеството и постоянство в иновациите.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Нашата мисия</div>
        <h2 class="section-title">Заедно сме<br><span>неудържими</span></h2>
        <div class="prose">
          <p>Gulf Oil е сред най-разпознаваемите марки в световната петролна индустрия — име, изградено върху доверие, издръжливост и постоянно усъвършенстване на продукта. Емблематичният оранжев диск присъства по пистите, по магистралите и в сервизите от десетилетия.</p>
          <p>В България екипът ни работи всеки ден, за да достави тази световна експертиза до местния пазар — чрез мрежа от партньори, дистрибутори и сервизи, отговарящи на най-високите стандарти на марката.</p>
        </div>
      </div>
      <div>
        <div class="section-label">Нашият подход</div>
        <h2 class="section-title">Винаги в<br><span>развитие</span></h2>
        <div class="prose">
          <p>Не спираме да се развиваме — нито като продукт, нито като организация. Инвестираме непрекъснато в нови формули, по-чисти процеси и по-добро обслужване, защото клиентите ни го заслужават.</p>
          <p>Всеки продукт, всяко партньорство и всяко решение се вземат с мисъл за хората, които разчитат на нас — от собственика на личен автомобил до операторите на цели флоти.</p>
        </div>
      </div>
    </div>
    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">1901</div><div class="stat-block-label">Основана</div></div>
      <div class="stat-block"><div class="stat-block-num">100+</div><div class="stat-block-label">Държави</div></div>
      <div class="stat-block"><div class="stat-block-num">6000+</div><div class="stat-block-label">Продукта</div></div>
      <div class="stat-block"><div class="stat-block-num">120+</div><div class="stat-block-label">Години опит</div></div>
    </div>
  </div>
</section>

<!-- HISTORY -->
<section class="content-section alt anchor-offset" id="history">
  <div class="section-inner">
    <div class="two-col">
      <div class="section-header reveal" style="margin-bottom:0;display:block;">
        <div class="section-label">Нашата история</div>
        <h2 class="section-title">Над век<br><span>наследство</span></h2>
        <p class="section-body">От първите кладенци до партньорствата с леджендарни отбори във Формула 1 — пътят на Gulf е история на постоянство и страст.</p>
        <div class="history-photo reveal reveal-delay-2">
          <img src="images/trackhouse-podium-duo.jpg" alt="Trackhouse MotoGP подиум"><span class="partner-caption">ROFGO Collection</span>
        </div>
      </div>
      <div class="timeline reveal reveal-delay-1">
        <div class="timeline-item">
          <div class="timeline-year">19<span>01</span></div>
          <div class="timeline-text">Основаването на Gulf бележи началото на едно от най-дълготрайните имена в световната петролна индустрия.</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-year">19<span>20</span></div>
          <div class="timeline-text">Появява се емблематичният оранжев диск — лого, което и днес се разпознава мигновено по целия свят.</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-year">19<span>60</span>-те</div>
          <div class="timeline-text">Раждат се легендарните бои в синьо и оранжево — цветовете, които ще обиколят пистите в Льо Ман и ще останат завинаги свързани с марката.</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-year">19<span>84</span></div>
          <div class="timeline-text">Gulf се присъединява към Hinduja Group — глобален конгломерат с над 200 000 служители — отваряйки нова глава в развитието на марката.</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-year">20<span>20</span>-те</div>
          <div class="timeline-text">Нови партньорства с Williams Racing, McLaren Automotive, Trackhouse MotoGP, Everrati и TAG Heuer затвърждават присъствието на Gulf в моторните спортове и автомобилния лукс.</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-year">20<span>26</span></div>
          <div class="timeline-text">Gulf продължава да разширява присъствието си в България и Югоизточна Европа с нови продукти, партньори и дистрибутори.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CULTURE & VALUES -->
<section class="content-section anchor-offset" id="culture">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Култура и ценности</div>
        <h2 class="section-title">Какво ни<br><span>движи напред</span></h2>
        <p class="section-body">Четири принципа стоят зад всеки продукт, партньорство и решение, които взимаме.</p>
      </div>
    </div>
    <div class="value-grid">
      <div class="value-card reveal reveal-delay-1">
        <div class="value-card-icon">""" + icon("01") + """</div>
        <div class="value-card-title">Качество</div>
        <div class="value-card-text">Всеки продукт преминава през строги изпитания, за да отговори на най-високите стандарти на индустрията.</div>
      </div>
      <div class="value-card reveal reveal-delay-2">
        <div class="value-card-icon">""" + icon("02") + """</div>
        <div class="value-card-title">Доверие</div>
        <div class="value-card-text">Изграждаме дългосрочни отношения с клиенти, дистрибутори и партньори — основани на последователност и почтеност.</div>
      </div>
      <div class="value-card reveal reveal-delay-3">
        <div class="value-card-icon">""" + icon("03") + """</div>
        <div class="value-card-title">Иновации</div>
        <div class="value-card-text">Инвестираме непрекъснато в нови формули и технологии, за да отговорим на променящите се нужди на пазара.</div>
      </div>
      <div class="value-card reveal reveal-delay-4">
        <div class="value-card-icon">""" + icon("04") + """</div>
        <div class="value-card-title">Отговорност</div>
        <div class="value-card-text">Стремим се към по-устойчиво бъдеще — за индустрията, за общностите и за следващите поколения.</div>
      </div>
    </div>
  </div>
</section>

<!-- LEADERSHIP -->
<section class="content-section alt anchor-offset" id="leadership">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Ръководство</div>
        <h2 class="section-title">Екипът зад<br><span>марката</span></h2>
        <p class="section-body">Опитен екип от професионалисти ръководи дейността на Gulf Oil България и развитието на дистрибуторската ни мрежа.</p>
      </div>
    </div>
    <div class="team-grid">
      <div class="team-card reveal reveal-delay-1">
        <div class="team-card-avatar">ГП</div>
        <div class="team-card-name">Управляващ директор</div>
        <div class="team-card-role">Локално ръководство</div>
        <div class="team-card-text">Отговаря за цялостната стратегия и развитието на Gulf на местния пазар.</div>
      </div>
      <div class="team-card reveal reveal-delay-2">
        <div class="team-card-avatar">ТП</div>
        <div class="team-card-name">Търговски директор</div>
        <div class="team-card-role">Продажби и партньорства</div>
        <div class="team-card-text">Развива мрежата от дистрибутори и партньорства с ключови клиенти в страната.</div>
      </div>
      <div class="team-card reveal reveal-delay-3">
        <div class="team-card-avatar">ТД</div>
        <div class="team-card-name">Технически директор</div>
        <div class="team-card-role">Продукт и качество</div>
        <div class="team-card-text">Гарантира съответствие на продуктите със стандартите на Gulf и нуждите на пазара.</div>
      </div>
      <div class="team-card reveal reveal-delay-4">
        <div class="team-card-avatar">МК</div>
        <div class="team-card-name">Маркетинг мениджър</div>
        <div class="team-card-role">Бранд и комуникации</div>
        <div class="team-card-text">Координира комуникацията на марката и партньорствата в моторните спортове.</div>
      </div>
    </div>
  </div>
</section>

<!-- SUSTAINABILITY -->
<section class="content-section anchor-offset" id="sustainability">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Устойчивост</div>
        <h2 class="section-title">Грижа за<br><span>утрешния ден</span></h2>
        <div class="prose">
          <p>Устойчивостта стои в основата на дългосрочната визия на Gulf. От разработването на формули с по-нисък отпечатък до отговорното управление на ресурсите — всяка стъпка е част от по-голям ангажимент към планетата.</p>
          <p>В България работим заедно с партньорите си за насърчаване на отговорна употреба, рециклиране на отработени масла и по-чисти производствени практики в цялата верига на доставки.</p>
        </div>
        <div style="margin-top:28px;">
          <a href="contact.html" class="btn-primary">Свържете се с нас →</a>
        </div>
      </div>
      <div class="prose">
        <p><strong>Рециклиране.</strong> Насърчаваме правилното събиране и обработка на отработени масла чрез мрежа от партньори и сертифицирани пунктове.</p>
        <p><strong>По-чисти формули.</strong> Разработваме продукти с фокус върху ефективност, по-дълъг живот и намалени емисии — за по-малък отпечатък върху околната среда.</p>
        <p><strong>Опаковки.</strong> Работим към по-устойчиви решения за опаковане, транспорт и логистика в цялата верига на доставки.</p>
        <p><strong>Общности.</strong> Подкрепяме инициативи на местните общности, в които оперираме — от образователни програми до партньорства за опазване на околната среда.</p>
      </div>
    </div>
  </div>
</section>
""")

# ============================================================
# MOTORSPORT
# ============================================================
PAGES['motorsport.html'] = (
"Мотоспорт — Gulf Oil България",
"Открийте наследството на Gulf в моторните спортове — от леджендарните бои в синьо и оранжево до днешните партньорства с Williams Racing, McLaren и Trackhouse MotoGP.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.92) 0%, rgba(27,45,107,0.8) 100%), url('images/motorsport-bg.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Мотоспорт</div>
    <div class="page-hero-eyebrow">Наследство на пистата</div>
    <h1 class="page-hero-title">Страстта към<br><span>скоростта</span></h1>
    <p class="page-hero-sub">Моторните спортове са в нашата ДНК. От легендарните бои в синьо и оранжево до най-новите партньорства във Формула 1 и MotoGP — Gulf винаги е там, където скоростта среща прецизността.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Наследство</div>
        <h2 class="section-title">Десетилетия<br><span>на пистата</span></h2>
        <div class="prose">
          <p>Малко марки могат да се похвалят с толкова дълга и емблематична история в моторните спортове, колкото Gulf. Леджендарните бои в светлосиньо и оранжево се превърнаха в синоним на класа и скоростта — разпознаваеми от трибуните на най-великите състезания по света.</p>
          <p>Това наследство не е просто история — то продължава да вдъхновява всеки продукт, който разработваме днес. Условията на пистата са най-суровото изпитание за едно масло, и точно затова продължаваме да инвестираме в света на състезанията.</p>
        </div>
      </div>
      <div>
        <div class="motorsport-image-stack" style="height:380px;">
          <div class="ms-img ms-img-tall"><img src="images/mclaren-artura-road.jpg" alt="McLaren Artura"><span class="partner-caption">McLaren Automotive</span></div>
          <div class="ms-img"><img src="images/tagheuer-watch.jpg" alt="TAG Heuer x Gulf Monaco"><span class="partner-caption">TAG Heuer × Gulf</span></div>
          <div class="ms-img"><img src="images/trackhouse-podium-duo.jpg" alt="Trackhouse MotoGP подиум"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Партньорства</div>
        <h2 class="section-title">Отбори и<br><span>легенди</span></h2>
        <p class="section-body">Gulf застава редом до едни от най-уважаваните имена в света на скоростта.</p>
      </div>
      <a href="partnerships.html" class="view-all">Всички партньорства →</a>
    </div>
    <div class="value-grid">
      <a href="partnerships.html#williams" class="value-card reveal reveal-delay-1" style="text-decoration:none;">
        <div class="value-card-icon">""" + icon("WR") + """</div>
        <div class="value-card-title">Williams Racing</div>
        <div class="value-card-text">Партньорство с един от най-емблематичните отбори във Формула 1.</div>
      </a>
      <a href="partnerships.html#mclaren" class="value-card reveal reveal-delay-2" style="text-decoration:none;">
        <div class="value-card-icon">""" + icon("MC") + """</div>
        <div class="value-card-title">McLaren Automotive</div>
        <div class="value-card-text">Съвместна работа в света на луксозните високопроизводителни автомобили.</div>
      </a>
      <a href="partnerships.html#trackhouse" class="value-card reveal reveal-delay-3" style="text-decoration:none;">
        <div class="value-card-icon">""" + icon("TH") + """</div>
        <div class="value-card-title">Trackhouse MotoGP</div>
        <div class="value-card-text">Присъствие на най-високо ниво в света на мотоциклетните състезания.</div>
      </a>
      <a href="partnerships.html#everrati" class="value-card reveal reveal-delay-4" style="text-decoration:none;">
        <div class="value-card-icon">""" + icon("EV") + """</div>
        <div class="value-card-title">Everrati</div>
        <div class="value-card-text">Подкрепа за бъдещето на класическите автомобили — реинженерирани с електрическо задвижване.</div>
      </a>
    </div>
  </div>
</section>

<!-- DEALER CTA -->
<div class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="cta-title">Открийте продуктите,<br>изковани на пистата</div>
      <div class="cta-sub">Технологии, изпитани в най-екстремните условия — приложени във всеки продукт на Gulf</div>
    </div>
    <a href="products-automotive.html" class="btn-white">Разгледай продукти →</a>
  </div>
</div>
""")

# ============================================================
# PARTNERSHIPS
# ============================================================
PAGES['partnerships.html'] = (
"Партньорства — Gulf Oil България",
"Опознайте партньорствата на Gulf с Williams Racing, McLaren Automotive, Trackhouse MotoGP, Everrati, ROFGO и TAG Heuer.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/williams-1.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Партньорства</div>
    <div class="page-hero-eyebrow">Заедно сме по-силни</div>
    <h1 class="page-hero-title">Нашите<br><span>партньорства</span></h1>
    <p class="page-hero-sub">Gulf избира партньори, които споделят нашата страст към съвършенството — от пистите във Формула 1 и MotoGP до света на луксозните автомобили и часовникарството.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">

    <div class="partner-block anchor-offset reveal" id="williams">
      <div class="partner-media">
        <img src="images/williams-helmets.jpg" alt="Williams Racing">
        <span class="partner-caption">Williams Racing — Формула 1</span>
        <span class="partner-shard-sky"></span>
      </div>
      <div>
        <div class="partner-tag">Формула 1 · от 2024 г.</div>
        <div class="partner-title-wrap"><h2 class="partner-title">Williams Racing</h2></div>
        <p class="partner-text">Gulf е официален партньор на Williams Racing — един от най-старите и емблематични отбори във Формула 1, основан от сър Франк Уилямс през 1977 г. Отборът носи 9 конструкторски и 7 пилотски титли в историята си и днес изгражда нов път към върха с младо поколение пилоти.</p>
        <p class="partner-text">Партньорството обхваща не само логото върху болида и екипировката — то включва съвместна разработка на смазочни материали, изпитани в реални състезателни условия, и пренасяне на тези технологии директно в продуктите на Gulf за ежедневна употреба.</p>
        <div class="partner-stats">
          <div class="partner-stat"><div class="partner-stat-num">1977</div><div class="partner-stat-label">Основан</div></div>
          <div class="partner-stat"><div class="partner-stat-num">9</div><div class="partner-stat-label">Конструкторски титли</div></div>
          <div class="partner-stat"><div class="partner-stat-num">€</div><div class="partner-stat-label">Технологичен трансфер от пистата</div></div>
        </div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="trackhouse">
      <div class="partner-media">
        <img src="images/trackhouse-race-2.jpg" alt="Trackhouse MotoGP">
        <span class="partner-caption">Trackhouse Racing — MotoGP</span>
        <span class="partner-shard-sky"></span>
      </div>
      <div>
        <div class="partner-tag">MotoGP · от 2024 г.</div>
        <div class="partner-title-wrap"><h2 class="partner-title">Trackhouse MotoGP</h2></div>
        <p class="partner-text">Партньорството с Trackhouse Racing бележи влизането на Gulf в света на MotoGP — дисциплина, известна с екстремните скорости, температури и натоварвания, на които са подложени машините и техните течности. Отборът на Trackhouse е сравнително млад, но изключително амбициозен — със състав от едни от най-обещаващите млади пилоти в класа.</p>
        <p class="partner-text">Условията на пистата в MotoGP представляват едно от най-суровите изпитания за смазочен материал — точно затова Gulf избира това партньорство, за да докаже издръжливостта на своите формули в реална, безкомпромисна среда.</p>
        <div class="partner-stats">
          <div class="partner-stat"><div class="partner-stat-num">2024</div><div class="partner-stat-label">Дебют в MotoGP</div></div>
          <div class="partner-stat"><div class="partner-stat-num">2</div><div class="partner-stat-label">Пилоти от младото поколение</div></div>
          <div class="partner-stat"><div class="partner-stat-num">300+</div><div class="partner-stat-label">км/ч връхна скорост</div></div>
        </div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="mclaren">
      <div class="partner-media">
        <img src="images/mclaren-artura-road.jpg" alt="McLaren Automotive">
        <span class="partner-caption">McLaren Automotive</span>
        <span class="partner-shard-sky"></span>
      </div>
      <div>
        <div class="partner-tag">Луксозни автомобили</div>
        <div class="partner-title-wrap"><h2 class="partner-title">McLaren Automotive</h2></div>
        <p class="partner-text">McLaren Automotive произвежда едни от най-високопроизводителните спортни автомобили в света — наследник на десетилетия инженерно майсторство от моторните спортове. Партньорството с Gulf обединява две марки, известни с безкомпромисния си стремеж към прецизност и иновации.</p>
        <p class="partner-text">Заедно работим върху смазочни решения, отговарящи на изключителните изисквания на високопроизводителните двигатели на McLaren — гарантирайки, че всеки модел получава защитата и представянето, достойни за неговия клас.</p>
        <div class="partner-stats">
          <div class="partner-stat"><div class="partner-stat-num">1985</div><div class="partner-stat-label">Основан McLaren Automotive</div></div>
          <div class="partner-stat"><div class="partner-stat-num">800+</div><div class="partner-stat-label">к.с. в най-мощните модели</div></div>
        </div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="everrati">
      <div class="partner-media">
        <img src="images/everrati-porsche.jpg" alt="Everrati">
        <span class="partner-caption">Everrati — електрическо наследство</span>
        <span class="partner-shard-sky"></span>
      </div>
      <div>
        <div class="partner-tag">Електрическо бъдеще</div>
        <div class="partner-title-wrap"><h2 class="partner-title">Everrati</h2></div>
        <p class="partner-text">Everrati реинженерира леджендарни класически автомобили — сред които емблематичният Porsche 911 — с модерно електрическо задвижване, съчетавайки автентичната естетика на миналото с технологиите на бъдещето. Всяко превозно средство преминава през щателен процес на реставрация и трансформация.</p>
        <p class="partner-text">Gulf подкрепя тази визия чрез разработването на нови решения за смазочни материали и течности в света на електромобилността (eFluids) — продукти, които ще съпровождат следващото поколение превозни средства, точно както класическите формули са обслужвали предишните.</p>
        <div class="partner-stats">
          <div class="partner-stat"><div class="partner-stat-num">2019</div><div class="partner-stat-label">Основан Everrati</div></div>
          <div class="partner-stat"><div class="partner-stat-num">eFluids</div><div class="partner-stat-label">Нова продуктова категория</div></div>
        </div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="rofgo">
      <div class="partner-media">
        <img src="images/everrati-2.jpg" alt="ROFGO Collection">
        <span class="partner-caption">ROFGO Collection</span>
        <span class="partner-shard-sky"></span>
      </div>
      <div>
        <div class="partner-tag">Историческо наследство</div>
        <div class="partner-title-wrap"><h2 class="partner-title">ROFGO</h2></div>
        <p class="partner-text">ROFGO Collection е една от най-впечатляващите частни колекции от исторически болиди от Формула 1 в света — над 30 автомобила, обхващащи десетилетия състезателна история. Сред тях са и леджендарни модели, носещи класическите цветове на Gulf в синьо и оранжево.</p>
        <p class="partner-text">Партньорството с ROFGO помага да се съхрани и популяризира това наследство пред нови поколения почитатели — чрез участия в демонстрационни писти, изложения и исторически събития в цяла Европа.</p>
        <div class="partner-stats">
          <div class="partner-stat"><div class="partner-stat-num">30+</div><div class="partner-stat-label">Исторически болиди в колекцията</div></div>
          <div class="partner-stat"><div class="partner-stat-num">5</div><div class="partner-stat-label">Десетилетия F1 история</div></div>
        </div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="tagheuer">
      <div class="partner-media">
        <img src="images/tagheuer-watch.jpg" alt="TAG Heuer x Gulf Monaco">
        <span class="partner-caption">TAG Heuer × Gulf</span>
        <span class="partner-shard-sky"></span>
      </div>
      <div>
        <div class="partner-tag">Часовникарство · от 1971 г.</div>
        <div class="partner-title-wrap"><h2 class="partner-title">TAG Heuer</h2></div>
        <p class="partner-text">Връзката между Gulf и TAG Heuer датира от леджендарния филм "Le Mans" с Стив Маккуин през 1971 г. — момент, който завинаги обвърза двете марки в колективното съзнание на почитателите на автомобилния спорт. И днес партньорството продължава да обединява два символа на прецизността: единият измерва времето, другият захранва машините, които го надбягват.</p>
        <p class="partner-text">Двете марки споделят обща естетика и философия — точност до милисекундата, безкомпромисна издръжливост и страст към представянето в най-високата му форма, независимо дали става дума за хронограф или двигател на 300 км/ч.</p>
        <div class="partner-stats">
          <div class="partner-stat"><div class="partner-stat-num">1971</div><div class="partner-stat-label">Начало на връзката — Le Mans</div></div>
          <div class="partner-stat"><div class="partner-stat-num">50+</div><div class="partner-stat-label">Години обща история</div></div>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- DEALER CTA -->
<div class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="cta-title">Открийте света<br>на Gulf мотоспорт</div>
      <div class="cta-sub">Научете повече за наследството ни на пистата и продуктите, родени от него</div>
    </div>
    <a href="motorsport.html" class="btn-white">Към мотоспорт →</a>
  </div>
</div>
""")

# ============================================================
# NEWS
# ============================================================
PAGES['news.html'] = (
"Новини — Gulf Oil България",
"Последни новини и прес съобщения от Gulf Oil България — продукти, партньорства и инициативи за устойчивост.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/news-secondary.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Новини</div>
    <div class="page-hero-eyebrow">Новинарски център</div>
    <h1 class="page-hero-title">Последни<br><span>новини</span></h1>
    <p class="page-hero-sub">Следете последните продуктови новини, партньорства в моторните спортове и инициативи на Gulf Oil България.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="news-list">

      <a href="#" class="news-list-item reveal anchor-offset" id="williams-2026">
        <div class="news-list-thumb"><img src="images/news-featured.jpg" alt="Williams Racing"></div>
        <div>
          <span class="news-card-tag">Мотоспорт</span>
          <div class="news-card-title">Gulf и Williams Racing обявяват нов сезон на партньорство</div>
          <div class="news-card-excerpt">Продължаваме нашето пътуване с един от най-емблематичните отбори във Формула 1, засилвайки нашето присъствие на пистата и пренасяйки наученото в продуктите за ежедневна употреба.</div>
          <div class="news-card-date">Юни 2026</div>
        </div>
      </a>

      <a href="#" class="news-list-item reveal anchor-offset" id="gdi-line">
        <div class="news-list-thumb"><img src="images/product-automotive.jpg" alt="Нова линия масла"></div>
        <div>
          <span class="news-card-tag">Продукти</span>
          <div class="news-card-title">Нова линия синтетични масла за GDI двигатели</div>
          <div class="news-card-excerpt">Gulf Ultrasynth GDI е разработена специално за съвременните бензинови двигатели с директно впръскване — осигурявайки по-добра защита и по-чисто горене.</div>
          <div class="news-card-date">Май 2026</div>
        </div>
      </a>

      <a href="#" class="news-list-item reveal anchor-offset" id="sustainability">
        <div class="news-list-thumb"><img src="images/agri-secondary.jpg" alt="Устойчивост"></div>
        <div>
          <span class="news-card-tag">Устойчивост</span>
          <div class="news-card-title">Gulf ускорява своята програма за устойчивост</div>
          <div class="news-card-excerpt">Нашият ангажимент към по-зелено бъдеще преминава през иновативни формули, отговорно управление на ресурсите и партньорства за рециклиране на отработени масла.</div>
          <div class="news-card-date">Април 2026</div>
        </div>
      </a>

      <a href="#" class="news-list-item reveal anchor-offset" id="press">
        <div class="news-list-thumb"><img src="images/marine-secondary.jpg" alt="Прес съобщение"></div>
        <div>
          <span class="news-card-tag">Прес съобщение</span>
          <div class="news-card-title">Gulf разширява дистрибуторската си мрежа в България</div>
          <div class="news-card-excerpt">Нови партньорства с регионални дистрибутори правят продуктите на Gulf по-достъпни в цялата страна — от големите градове до малките сервизи.</div>
          <div class="news-card-date">Март 2026</div>
        </div>
      </a>

      <a href="#" class="news-list-item reveal">
        <div class="news-list-thumb"><img src="images/trackhouse-podium-fernandez.jpg" alt="Trackhouse MotoGP подиум"><span class="partner-caption">Trackhouse Racing — MotoGP</span></div>
        <div>
          <span class="news-card-tag">Мотоспорт</span>
          <div class="news-card-title">Trackhouse MotoGP стартира сезона с цветовете на Gulf</div>
          <div class="news-card-excerpt">Леджендарните бои в синьо и оранжево се завръщат на пистата — този път в света на MotoGP.</div>
          <div class="news-card-date">Февруари 2026</div>
        </div>
      </a>

      <a href="#" class="news-list-item reveal">
        <div class="news-list-thumb"><img src="images/product-pour.jpg" alt="Съветник за смазочни материали"></div>
        <div>
          <span class="news-card-tag">Продукти</span>
          <div class="news-card-title">Обновен съветник за смазочни материали вече е достъпен онлайн</div>
          <div class="news-card-excerpt">Намерете правилния продукт за вашето превозно средство само за няколко клика с инструмента на Gulf.</div>
          <div class="news-card-date">Януари 2026</div>
        </div>
      </a>

    </div>
  </div>
</section>
""")

# ============================================================
# CONTACT
# ============================================================
PAGES['contact.html'] = (
"Контакт — Gulf Oil България",
"Свържете се с екипа на Gulf Oil България — изпратете запитване, станете дистрибутор или намерете контактна информация.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/contact-bg.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Контакт</div>
    <div class="page-hero-eyebrow">Свържете се с нас</div>
    <h1 class="page-hero-title">Да говорим<br><span>заедно</span></h1>
    <p class="page-hero-sub">Имате въпрос за продукт, партньорство или искате да станете дистрибутор на Gulf? Екипът ни е насреща да помогне.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="contact-grid">
      <div>
        <div class="section-label">Пишете ни</div>
        <h2 class="section-title">Изпратете<br><span>запитване</span></h2>
        <form class="reveal" style="margin-top:32px;" onsubmit="event.preventDefault(); alert('Благодарим ви! Ще се свържем с вас възможно най-скоро.');">
          <div class="form-row">
            <div class="form-field">
              <label for="c-name">Име</label>
              <input type="text" id="c-name" name="name" placeholder="Вашето име" required>
            </div>
            <div class="form-field">
              <label for="c-company">Компания</label>
              <input type="text" id="c-company" name="company" placeholder="Име на фирма (по желание)">
            </div>
          </div>
          <div class="form-row">
            <div class="form-field">
              <label for="c-phone">Телефон</label>
              <input type="tel" id="c-phone" name="phone" placeholder="+359 ...">
            </div>
            <div class="form-field">
              <label for="c-email">Имейл</label>
              <input type="email" id="c-email" name="email" placeholder="you@example.com" required>
            </div>
          </div>
          <div class="form-field">
            <label for="c-category">Тема на запитването</label>
            <select id="c-category" name="category">
              <option value="">— Изберете —</option>
              <option value="marketing">Маркетинг</option>
              <option value="business">Бизнес развитие</option>
              <option value="careers">Кариери</option>
              <option value="press">Преса</option>
            </select>
          </div>
          <div class="form-field">
            <label for="c-message">Съобщение</label>
            <textarea id="c-message" name="message" placeholder="Как можем да помогнем?" required></textarea>
          </div>
          <button type="submit" class="btn-submit">Изпрати запитване →</button>
        </form>
      </div>

      <div>
        <div class="contact-info-card reveal reveal-delay-1">
          <div class="section-label">Контакти</div>
          <h3 class="section-title" style="font-size:28px;">Gulf Oil<br>България</h3>
          <div class="contact-info-row">
            <div class="contact-info-icon">""" + icon("Ad") + """</div>
            <div>
              <div class="contact-info-label">Адрес</div>
              <div class="contact-info-value">София, България</div>
            </div>
          </div>
          <div class="contact-info-row">
            <div class="contact-info-icon">""" + icon("@") + """</div>
            <div>
              <div class="contact-info-label">Имейл</div>
              <div class="contact-info-value">info@gulfoil.bg</div>
            </div>
          </div>
          <div class="contact-info-row">
            <div class="contact-info-icon">""" + icon("Tl") + """</div>
            <div>
              <div class="contact-info-label">Телефон</div>
              <div class="contact-info-value">+359 2 000 0000</div>
            </div>
          </div>
          <div class="contact-info-row">
            <div class="contact-info-icon">""" + icon("Ч") + """</div>
            <div>
              <div class="contact-info-label">Работно време</div>
              <div class="contact-info-value">Пон – Пет: 09:00 – 18:00</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BECOME A DISTRIBUTOR -->
<section class="content-section alt anchor-offset" id="distributor">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Бизнес възможности</div>
        <h2 class="section-title">Станете<br><span>дистрибутор</span></h2>
        <div class="prose">
          <p>Търсите ли възможност да разширите бизнеса си с продуктите на едно от най-уважаваните имена в петролната индустрия? Gulf разширява дистрибуторската си мрежа в България и региона.</p>
          <p>Свържете се с нас, за да научите повече за условията за партньорство, изискванията и подкрепата, която предлагаме на нашите дистрибутори — от обучения до маркетингови материали.</p>
        </div>
        <div style="margin-top:28px;">
          <a href="#c-name" class="btn-primary">Изпратете запитване →</a>
        </div>
      </div>
      <div class="value-grid" style="grid-template-columns:1fr 1fr;margin-top:0;">
        <div class="value-card">
          <div class="value-card-icon">""" + icon("01") + """</div>
          <div class="value-card-title">Пълна гама</div>
          <div class="value-card-text">Достъп до целия продуктов портфейл на Gulf за всички сектори.</div>
        </div>
        <div class="value-card">
          <div class="value-card-icon">""" + icon("02") + """</div>
          <div class="value-card-title">Обучения</div>
          <div class="value-card-text">Продуктови и търговски обучения за вас и вашия екип.</div>
        </div>
        <div class="value-card">
          <div class="value-card-icon">""" + icon("03") + """</div>
          <div class="value-card-title">Маркетинг</div>
          <div class="value-card-text">Достъп до бранд материали и подкрепа за локални кампании.</div>
        </div>
        <div class="value-card">
          <div class="value-card-icon">""" + icon("04") + """</div>
          <div class="value-card-title">Партньорство</div>
          <div class="value-card-text">Дългосрочна подкрепа от екип, посветен на вашия успех.</div>
        </div>
      </div>
    </div>
  </div>
</section>
""")

# ============================================================
# SERVICES (fuel retail / горивна търговия)
# ============================================================
PAGES['services.html'] = (
"Горивна търговия — Услуги — Gulf Oil България",
"Открийте възможностите за партньорство в горивната търговия с Gulf Oil България.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/services-bg.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Услуги › Горивна търговия</div>
    <div class="page-hero-eyebrow">Услуги</div>
    <h1 class="page-hero-title">Горивна<br><span>търговия</span></h1>
    <p class="page-hero-sub">Освен с водещи смазочни материали, Gulf разполага с дългогодишен опит в горивната търговия и развитието на партньорства на дребно.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво предлагаме</div>
        <h2 class="section-title">Партньорства<br><span>в горивния сектор</span></h2>
        <div class="prose">
          <p>Gulf работи с дистрибутори, оператори на бензиностанции и индустриални клиенти, за да осигури надеждни доставки на горива и свързани услуги — подкрепени от десетилетия опит и глобална експертиза.</p>
          <p>Независимо дали сте оператор на мрежа от бензиностанции или търсите доставчик за индустриални нужди — нашият екип може да изгради решение, съобразено с вашия бизнес.</p>
        </div>
        <div style="margin-top:28px;">
          <a href="contact.html" class="btn-primary">Свържете се с нас →</a>
        </div>
      </div>
      <div>
        <div class="simple-grid" style="grid-template-columns:1fr;margin-top:0;">
          <div class="simple-card">
            <div class="simple-card-icon">""" + icon("01") + """</div>
            <div class="simple-card-title">Доставки на горива</div>
            <div class="simple-card-text">Надеждни и навременни доставки за оператори на дребно и индустриални клиенти.</div>
          </div>
          <div class="simple-card">
            <div class="simple-card-icon">""" + icon("02") + """</div>
            <div class="simple-card-title">Партньорства на дребно</div>
            <div class="simple-card-text">Възможности за брандиране и развитие на обекти под името на Gulf.</div>
          </div>
          <div class="simple-card">
            <div class="simple-card-icon">""" + icon("03") + """</div>
            <div class="simple-card-title">Бизнес подкрепа</div>
            <div class="simple-card-text">Достъп до търговска експертиза, обучения и маркетингова подкрепа.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DEALER CTA -->
<div class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="cta-title">Искате ли да станете<br>част от мрежата на Gulf?</div>
      <div class="cta-sub">Научете повече за възможностите за партньорство и дистрибуция</div>
    </div>
    <a href="contact.html#distributor" class="btn-white">Станете партньор →</a>
  </div>
</div>
""")

# ============================================================
# DEALER LOCATOR
# ============================================================
PAGES['dealer-locator.html'] = (
"Намери дилър — Gulf Oil България",
"Намерете най-близкия сертифициран дилър и сервиз на Gulf Oil във вашия град.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/dealer-bg.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Намери дилър</div>
    <div class="page-hero-eyebrow">Дилърска мрежа</div>
    <h1 class="page-hero-title">Намерете<br><span>Gulf дилър</span></h1>
    <p class="page-hero-sub">Мрежа от сертифицирани дистрибутори и сервизи в цяла България — готови да ви предложат пълната гама продукти на Gulf и експертен съвет.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Търсене на дилър</div>
        <h2 class="section-title">Открийте най-близкия<br><span>до вас обект</span></h2>
        <div class="prose">
          <p>Въведете своя град или район и нашата система ще ви покаже най-близките сертифицирани дилъри и сервизи на Gulf — заедно с информация за контакт и предлаганите продукти.</p>
        </div>
        <form style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap;" onsubmit="event.preventDefault(); alert('Функцията за търсене ще бъде активна скоро. Моля, свържете се с нас за съдействие.');">
          <div class="form-field" style="flex:1;min-width:220px;margin-bottom:0;">
            <input type="text" placeholder="Въведете град или пощенски код" aria-label="Град или пощенски код">
          </div>
          <button type="submit" class="btn-submit">Търси дилър →</button>
        </form>
      </div>
      <div>
        <div class="simple-grid" style="grid-template-columns:1fr;margin-top:0;">
          <div class="simple-card">
            <div class="simple-card-icon">""" + icon("01") + """</div>
            <div class="simple-card-title">Национално покритие</div>
            <div class="simple-card-text">Дилъри и сервизи в големите градове и регионалните центрове на страната.</div>
          </div>
          <div class="simple-card">
            <div class="simple-card-icon">""" + icon("02") + """</div>
            <div class="simple-card-title">Сертифицирани партньори</div>
            <div class="simple-card-text">Всеки дилър е обучен да предлага продуктите на Gulf и компетентен съвет.</div>
          </div>
          <div class="simple-card">
            <div class="simple-card-icon">""" + icon("03") + """</div>
            <div class="simple-card-title">Пълна гама услуги</div>
            <div class="simple-card-text">От смяна на масло до пълно сервизно обслужване с продукти на Gulf.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DEALER CTA -->
<div class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="cta-title">Не намирате дилър<br>във вашия район?</div>
      <div class="cta-sub">Свържете се директно с нас и ще ви насочим към най-близкия партньор</div>
    </div>
    <a href="contact.html" class="btn-white">Свържете се с нас →</a>
  </div>
</div>
""")

# ============================================================
# PRODUCTS — AUTOMOTIVE
# ============================================================
PAGES['products-automotive.html'] = (
"Автомобилни продукти — Gulf Oil България",
"Пълна гама смазочни материали на Gulf за леки автомобили, мотоциклети и търговски превозни средства.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/product-automotive.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Продукти › Автомобилни</div>
    <div class="page-hero-eyebrow">Продукти</div>
    <h1 class="page-hero-title">Автомобилни<br><span>смазочни материали</span></h1>
    <p class="page-hero-sub">От градски автомобили до тежкотоварни флоти — продуктите на Gulf са разработени да защитават двигателя и да оптимизират представянето във всякакви условия.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">

    <div class="partner-block anchor-offset reveal" id="cars">
      <div class="partner-media"><img src="images/product-automotive.jpg" alt="Леки автомобили"><span class="partner-caption">Gulf Formula G — синтетични масла</span></div>
      <div>
        <div class="partner-tag">Леки автомобили</div>
        <h2 class="partner-title">Масла за леки автомобили</h2>
        <p class="partner-text">Пълна гама от синтетични и полусинтетични моторни масла за леки автомобили с бензинови и дизелови двигатели — разработени да осигурят защита, чистота и плавна работа на двигателя при всякакви условия на движение.</p>
        <p class="partner-text">Линията включва продукти за съвременни турбо двигатели с директно впръскване, както и класически формули за по-стари автомобили.</p>
        <div class="partner-highlight">Над 6000 продукта в портфолиото на Gulf</div>
        <div style="margin-top:20px;display:flex;gap:14px;flex-wrap:wrap;">
          <a href="product-auto-passenger.html" class="btn-primary">Разгледай продукта →</a>
          <a href="https://europe.gulfoilltd.com/lubricantadvisor" target="_blank" class="btn-white" style="border:2px solid var(--navy);color:var(--navy);background:transparent;">Намерете продукт за вашия автомобил →</a>
        </div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="motorcycle">
      <div class="partner-media"><img src="images/trackhouse-race-4.jpg" alt="Мотоциклетни масла"><span class="partner-caption">Изпитани в условията на пистата</span></div>
      <div>
        <div class="partner-tag">Мотоциклети</div>
        <h2 class="partner-title">Мотоциклетни масла</h2>
        <p class="partner-text">Специализирани формули за двутактови и четиритактови мотоциклетни двигатели — осигуряващи защита при високи обороти, плавно превключване и дълготрайна издръжливост на двигателя и съединителя.</p>
        <p class="partner-text">Технологиите от партньорството ни с Trackhouse MotoGP пряко се пренасят в продуктите от тази гама — изпитани в най-екстремните условия на пистата.</p>
        <div class="partner-highlight">Подкрепени от наследството ни в MotoGP</div>
        <div style="margin-top:20px;"><a href="product-auto-motorcycle.html" class="btn-primary">Разгледай продукта →</a></div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="commercial">
      <div class="partner-media"><img src="images/mclaren-artura-detail.jpg" alt="Търговски превозни средства"><span class="partner-caption">Търговски флоти — Gulf продукти</span></div>
      <div>
        <div class="partner-tag">Търговски флоти</div>
        <h2 class="partner-title">Търговски превозни средства</h2>
        <p class="partner-text">Продукти, разработени за камиони, автобуси и тежкотоварни превозни средства — намаляващи разходите за поддръжка и удължаващи живота на двигателя при интензивна експлоатация.</p>
        <p class="partner-text">Гамата включва моторни масла, трансмисионни и хидравлични течности, отговарящи на изискванията на водещите производители на двигатели.</p>
        <div class="partner-highlight">Издържливост при тежки и продължителни натоварвания</div>
        <div style="margin-top:20px;"><a href="product-auto-commercial.html" class="btn-primary">Разгледай продукта →</a></div>
      </div>
    </div>

  </div>
</section>

<!-- ADVISOR -->
<div class="advisor-banner">
  <div class="advisor-inner">
    <div class="advisor-text">
      <div class="advisor-icon">A</div>
      <div>
        <div class="advisor-label">Не сте сигурни кой продукт ви трябва?</div>
        <div class="advisor-sub">Използвайте съветника за смазочни материали на Gulf, за да намерите точния продукт за секунди</div>
      </div>
    </div>
    <a href="https://europe.gulfoilltd.com/lubricantadvisor" target="_blank" class="advisor-btn">Отвори съветника ›</a>
  </div>
</div>
""")

# ============================================================
# PRODUCT DETAIL — AGRI ENGINE OIL (template for individual product pages)
# ============================================================
PAGES['product-agri-engine-oil.html'] = (
"Моторни масла за земеделска техника — Gulf Oil България",
"Gulf моторни масла за земеделска техника — формулирани за защита на двигателя при високо натоварване, прах и продължителна работа.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/agri-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-agriculture.html">Земеделие</a> › Моторни масла</div>
    <div class="page-hero-eyebrow">Земеделие · Продукт</div>
    <h1 class="page-hero-title">Моторни <span>масла</span></h1>
    <p class="page-hero-sub">Защита на двигателя при продължителна работа с високо натоварване и в прашна среда — формулирани да удължават интервалите между смените и да намаляват износването на критични компоненти.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Изградени за<br><span>тежки условия</span></h2>
        <div class="prose">
          <p>Земеделската техника работи в едни от най-взискателните условия — продължителни смени, високо натоварване на двигателя, прах и резки промени в температурата. Моторните масла на Gulf са формулирани именно за тази среда, осигурявайки стабилна защита от първото до последното завъртане на двигателя през сезона.</p>
          <p>Гамата покрива нуждите на трактори, комбайни и друга самоходна техника — независимо дали става дума за по-стари дизелови двигатели или съвременни модели с прецизни системи за контрол на емисиите.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/agri-secondary.jpg" alt="Gulf моторни масла за земеделска техника" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">15W-40</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">API CK-4</div><div class="stat-block-label">Стандарт за дизелови двигатели</div></div>
      <div class="stat-block"><div class="stat-block-num">500ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">−30°C</div><div class="stat-block-label">Студен старт</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf моторни масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Удължена защита на двигателя</div>
        <div class="benefit-card-text">Стабилна маслена пленка при високи температури и натоварвания намалява износването на бутала, лагери и разпределителни механизми.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Контрол на саждите и отлаганията</div>
        <div class="benefit-card-text">Усъвършенствани диспергиращи свойства поддържат двигателя чист дори при продължителна работа с нискокачествени горива.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълги интервали между смените</div>
        <div class="benefit-card-text">По-висока устойчивост на окисление позволява по-рядка подмяна на маслото — по-малко престой и по-ниски разходи за поддръжка.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Лесен студен старт</div>
        <div class="benefit-card-text">Подходяща вискозност при ниски температури осигурява бързо подаване на масло към критичните части на двигателя още при първото запалване.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
        <p class="section-body">Gulf моторни масла обслужват широк спектър земеделска и самоходна техника:</p>
      </div>
    </div>
    <div class="prose">
      <p>Трактори и комбайни с дизелови двигатели от различни поколения; самоходни пръскачки и товарo-разтоварна техника; стационарни и преносими генератори и помпени агрегати, използвани в земеделски обекти.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")


# ============================================================
# PRODUCT DETAIL PAGES — generated set
# ============================================================
PAGES['product-agri-transmission.html'] = (
"Трансмисионни течности — Gulf Oil България",
"Gulf трансмисионни течности — Плавна работа на трансмисията и удължен живот на компонентите при тежки условия и продължително натоварване.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/agri-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-agriculture.html">Земеделие</a> › Трансмисионни течности</div>
    <div class="page-hero-eyebrow">Земеделие · Продукт</div>
    <h1 class="page-hero-title">Трансмисионни <span>течности</span></h1>
    <p class="page-hero-sub">Плавна работа на трансмисията и удължен живот на компонентите при тежки условия и продължително натоварване.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Прецизност при<br><span>всяко превключване</span></h2>
        <div class="prose">
          <p>Трансмисиите на земеделската техника понасят постоянни промени в натоварването — от транспортни преходи до прецизна работа на полето. Течностите на Gulf са създадени да поддържат стабилно налягане и плавно зацепване във всеки режим.</p>
          <p>Формулите осигуряват защита на зъбни колела, синхронизатори и хидравлични елементи на трансмисията, намалявайки шума и износването при дългогодишна експлоатация.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/agri-secondary.jpg" alt="Трансмисионни течности" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">80W-90</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">API GL-4</div><div class="stat-block-label">Стандарт за трансмисии</div></div>
      <div class="stat-block"><div class="stat-block-num">1000ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">−25°C</div><div class="stat-block-label">Студен старт</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf трансмисионни течности</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Плавно зацепване</div>
        <div class="benefit-card-text">Стабилна вискозност при различни температури осигурява меко и точно превключване на предавките.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита на зъбните колела</div>
        <div class="benefit-card-text">Усъвършенствани присадки намаляват триенето и предпазват металните повърхности от микро-разрушения.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Устойчивост на пенене</div>
        <div class="benefit-card-text">Контролирано поведение при високи обороти запазва стабилно налягане в системата.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълъг живот на компонентите</div>
        <div class="benefit-card-text">Намалено износване удължава експлоатационния живот на скоростната кутия и редукторите.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Трактори с механични и полу-автоматични трансмисии; комбайни с тежко натоварени редуктори; товарo-разтоварна техника и прикачен инвентар с хидравлично задвижване.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-agri-hydraulic.html'] = (
"Хидравлични масла — Gulf Oil България",
"Gulf хидравлични масла — Стабилна и надеждна работа на хидравличните системи — от навесно оборудване и товарачи до прецизни земеделски машини с високо налягане.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/sector-industrial.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-agriculture.html">Земеделие</a> › Хидравлични масла</div>
    <div class="page-hero-eyebrow">Земеделие · Продукт</div>
    <h1 class="page-hero-title">Хидравлични <span>масла</span></h1>
    <p class="page-hero-sub">Стабилна и надеждна работа на хидравличните системи — от навесно оборудване и товарачи до прецизни земеделски машини с високо налягане.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Сила и прецизност<br><span>под налягане</span></span></h2>
        <div class="prose">
          <p>Хидравличните системи на съвременната земеделска техника изискват течности, които запазват стабилни характеристики при високо налягане, променливи температури и продължителна работа без прекъсване.</p>
          <p>Маслата на Gulf поддържат точен и предвидим отклик на хидравликата — от управлението на навесни устройства до системите за прецизно земеделие.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/marine-hero.jpg" alt="Хидравлични масла" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">ISO 46</div><div class="stat-block-label">Клас на вискозност</div></div>
      <div class="stat-block"><div class="stat-block-num">DIN 51524</div><div class="stat-block-label">Хидравличен стандарт</div></div>
      <div class="stat-block"><div class="stat-block-num">2000ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">−20°C</div><div class="stat-block-label">Студен старт</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf хидравлични масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Стабилно налягане</div>
        <div class="benefit-card-text">Постоянна вискозност гарантира предвидим и точен отклик на хидравличните механизми.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита от износване</div>
        <div class="benefit-card-text">Висококачествени присадки предпазват помпи, клапани и цилиндри от преждевременно износване.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Устойчивост на окисление</div>
        <div class="benefit-card-text">По-дълъг експлоатационен живот на маслото дори при висока работна температура.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Съвместимост с уплътненията</div>
        <div class="benefit-card-text">Формула, съобразена с материалите на съвременните хидравлични системи — без риск от течове.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Челни товарачи и навесни устройства; системи за управление на прикачен инвентар; хидростатични трансмисии и прецизни системи за насочване.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-agri-stou.html'] = (
"STOU масла — Gulf Oil България",
"Gulf STOU масла — Универсална формула, която покрива двигател, трансмисия и хидравлика в едно решение — по-малко продукти за съхранение и по-проста поддръжка на парка машини.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/marine-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-agriculture.html">Земеделие</a> › STOU масла</div>
    <div class="page-hero-eyebrow">Земеделие · Продукт</div>
    <h1 class="page-hero-title">STOU <span>масла</span></h1>
    <p class="page-hero-sub">Универсална формула, която покрива двигател, трансмисия и хидравлика в едно решение — по-малко продукти за съхранение и по-проста поддръжка на парка машини.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Едно масло —<br><span>пълно покритие</span></h2>
        <div class="prose">
          <p>STOU (Super Tractor Oil Universal) маслата на Gulf са създадени за земеделски стопанства и сервизи, които искат да опростят поддръжката си — едно масло, което отговаря на изискванията едновременно на двигател, трансмисия, хидравлика и спирачки, потопени в масло.</p>
          <p>Това намалява риска от грешки при избора на правилния продукт, опростява логистиката на склада и намалява общите разходи за поддръжка на парка машини.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/agri-hero.jpg" alt="STOU масла" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">10W-30</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">API GL-4</div><div class="stat-block-label">Многофункционален стандарт</div></div>
      <div class="stat-block"><div class="stat-block-num">1×</div><div class="stat-block-label">Продукт за всички системи</div></div>
      <div class="stat-block"><div class="stat-block-num">−25°C</div><div class="stat-block-label">Студен старт</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf STOU масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Опростена поддръжка</div>
        <div class="benefit-card-text">Едно масло за двигател, трансмисия и хидравлика — по-малко грешки и по-лесно управление на склада.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Доказана съвместимост</div>
        <div class="benefit-card-text">Подходящо за мокри спирачки и съединители без риск от приплъзване или износване.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Стабилност при смесени системи</div>
        <div class="benefit-card-text">Запазва експлоатационните си характеристики дори при споделена циркулация между компоненти.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-ниски общи разходи</div>
        <div class="benefit-card-text">По-малко складирани продукти и по-лесна логистика означават реални икономии за стопанството.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Универсални трактори с обща хидравлично-трансмисионна система; по-стара техника, използваща споделени резервоари; стопанства, предпочитащи опростена едно-продуктова поддръжка.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-agri-chain.html'] = (
"Верижни масла — Gulf Oil България",
"Gulf верижни масла — Специализирана защита срещу износване на вериги, водачи и движещи се части — устойчивост на прах, влага и резки температурни промени.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/agri-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-agriculture.html">Земеделие</a> › Верижни масла</div>
    <div class="page-hero-eyebrow">Земеделие · Продукт</div>
    <h1 class="page-hero-title">Верижни <span>масла</span></h1>
    <p class="page-hero-sub">Специализирана защита срещу износване на вериги, водачи и движещи се части — устойчивост на прах, влага и резки температурни промени.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Защита там,<br><span>където триенето е най-силно</span></h2>
        <div class="prose">
          <p>Веригите и водещите механизми на земеделската техника работят в постоянен контакт с прах, влага и абразивни частици. Верижните масла на Gulf са формулирани да издържат на тези условия, като се задържат върху повърхността и не се отмиват лесно.</p>
          <p>Резултатът е по-плавна работа, по-малко вибрации и значително удължен живот на скъпите механични компоненти.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/agri-secondary.jpg" alt="Верижни масла" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">ISO 150</div><div class="stat-block-label">Клас на вискозност</div></div>
      <div class="stat-block"><div class="stat-block-num">Адхезив</div><div class="stat-block-label">Тип формула</div></div>
      <div class="stat-block"><div class="stat-block-num">250ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">−15°C</div><div class="stat-block-label">Работна температура</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf верижни масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Висока адхезия</div>
        <div class="benefit-card-text">Маслото остава върху веригата дори при високи скорости и в дъждовни условия.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Намалено триене</div>
        <div class="benefit-card-text">По-плавна работа и по-малко загуба на мощност по веригата на задвижването.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита от корозия</div>
        <div class="benefit-card-text">Бариера срещу влага и абразивни частици, предпазваща металните звена от ръжда.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълъг живот на компонентите</div>
        <div class="benefit-card-text">По-рядка подмяна на вериги и водачи — по-ниски разходи за резервни части.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Комбайни с верижно задвижване и транспортьори; прибиращи машини с подвижни режещи механизми; всякакъв тип прикачен инвентар с открити вериги и водачи.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-agri-supplementary.html'] = (
"Спомагателни продукти — Gulf Oil България",
"Gulf спомагателни продукти — Грес, добавки и поддържащи продукти, които допълват основната гама и осигуряват пълна грижа за вашата техника през целия сезон.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/agri-secondary.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-agriculture.html">Земеделие</a> › Спомагателни продукти</div>
    <div class="page-hero-eyebrow">Земеделие · Продукт</div>
    <h1 class="page-hero-title">Спомагателни <span>продукти</span></h1>
    <p class="page-hero-sub">Грес, добавки и поддържащи продукти, които допълват основната гама и осигуряват пълна грижа за вашата техника през целия сезон.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Завършеност на<br><span>цялостната грижа</span></h2>
        <div class="prose">
          <p>Освен основните масла и течности, поддръжката на земеделска техника изисква и набор от спомагателни продукти — смазки за лагери и шарнири, добавки за гориво и системи за охлаждане, и препарати за почистване на компоненти.</p>
          <p>Гамата на Gulf допълва основните продукти, като осигурява последователна защита на всеки възел от машината — от двигателя до най-малкия шарнирен болт.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/agri-hero.jpg" alt="Спомагателни продукти" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">NLGI 2</div><div class="stat-block-label">Клас на смазките</div></div>
      <div class="stat-block"><div class="stat-block-num">6000+</div><div class="stat-block-label">Продукта в портфолиото</div></div>
      <div class="stat-block"><div class="stat-block-num">−20°C</div><div class="stat-block-label">Работна температура</div></div>
      <div class="stat-block"><div class="stat-block-num">1</div><div class="stat-block-label">Доставчик за цялата гама</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf спомагателни продукти</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Универсална защита</div>
        <div class="benefit-card-text">Смазки и добавки, разработени да работят съвместно с основните масла на Gulf, без компромис в качеството.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълъг живот на лагерите</div>
        <div class="benefit-card-text">Качествени греси предпазват шарнири и лагери от износване в прашна и влажна среда.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-чисти системи</div>
        <div class="benefit-card-text">Препарати за почистване поддържат компонентите в добро състояние между основните обслужвания.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Удобство от един доставчик</div>
        <div class="benefit-card-text">Цялата необходима гама продукти от едно надеждно име — по-лесна поръчка и логистика.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Лагери, шарнири и кръстосани съединения на прикачен инвентар; горивни и охладителни системи на двигателя; обща поддръжка и почистване на машинния парк между сезони.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-auto-passenger.html'] = (
"Масла за леки автомобили — Gulf Oil България",
"Gulf масла за леки автомобили — Синтетични и полусинтетични формули Gulf Formula G — за плавна, ефективна и защитена работа на двигателя във всяко ежедневно пътуване.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/product-automotive.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-automotive.html">Автомобилни</a> › Масла за леки автомобили</div>
    <div class="page-hero-eyebrow">Автомобилни · Продукт</div>
    <h1 class="page-hero-title">Масла за леки <span>автомобили</span></h1>
    <p class="page-hero-sub">Синтетични и полусинтетични формули Gulf Formula G — за плавна, ефективна и защитена работа на двигателя във всяко ежедневно пътуване.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Технология от<br><span>пистата на пътя</span></h2>
        <div class="prose">
          <p>Гамата Gulf Formula G пренася опита на марката от десетилетия в моторните спортове към ежедневните автомобили. Синтетичните основи и съвременните присадки осигуряват защита на двигателя дори при кратки градски пътувания и чести стартирания.</p>
          <p>Формулите отговарят на изискванията на повечето съвременни бензинови и дизелови двигатели, включително такива с турбокомпресори и системи за контрол на емисиите.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/mclaren-artura-detail.jpg" alt="Масла за леки автомобили" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">5W-30</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">ACEA C3</div><div class="stat-block-label">Европейски стандарт</div></div>
      <div class="stat-block"><div class="stat-block-num">15000км</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">100%</div><div class="stat-block-label">Синтетична основа</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf масла за леки автомобили</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Плавно потегляне</div>
        <div class="benefit-card-text">Бързо подаване на масло към критичните части на двигателя още при първото завъртане на ключа.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита на турбокомпресора</div>
        <div class="benefit-card-text">Термична стабилност предпазва от образуване на отлагания при високи обороти и температури.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-ниска консумация на гориво</div>
        <div class="benefit-card-text">Намалено вътрешно триене допринася за по-добра ефективност на двигателя.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Удължен живот на двигателя</div>
        <div class="benefit-card-text">Постоянна защита при градско шофиране, дълги пътувания и всякакви условия на средата.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Леки автомобили с бензинови и дизелови двигатели; модели с турбокомпресор и системи Start-Stop; хибридни автомобили с термичен двигател.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-auto-motorcycle.html'] = (
"Мотоциклетни масла — Gulf Oil България",
"Gulf мотоциклетни масла — Изпитани в условията на пистата чрез партньорството с Trackhouse MotoGP — формули, създадени да издържат на най-високите обороти и температури.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/trackhouse-race-2.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-automotive.html">Автомобилни</a> › Мотоциклетни масла</div>
    <div class="page-hero-eyebrow">Автомобилни · Продукт</div>
    <h1 class="page-hero-title">Мотоциклетни <span>масла</span></h1>
    <p class="page-hero-sub">Изпитани в условията на пистата чрез партньорството с Trackhouse MotoGP — формули, създадени да издържат на най-високите обороти и температури.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Наследство от<br><span>пистите на MotoGP</span></h2>
        <div class="prose">
          <p>Партньорството на Gulf с Trackhouse MotoGP Team не е само маркетингово присъствие — научените уроци от състезателните писти директно влияят върху формулирането на маслата за сериен мотоциклет.</p>
          <p>Гамата покрива нуждите на четиритактови двигатели с общи и разделени системи за смазване на двигател и трансмисия, осигурявайки стабилна защита при високи обороти.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/trackhouse-race-4.jpg" alt="Мотоциклетни масла" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">10W-40</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">JASO MA2</div><div class="stat-block-label">Стандарт за съединители</div></div>
      <div class="stat-block"><div class="stat-block-num">6000км</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">MotoGP</div><div class="stat-block-label">Тествано на пистата</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf мотоциклетни масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Стабилност при високи обороти</div>
        <div class="benefit-card-text">Поддържа защитна пленка дори при продължителна работа близо до червената линия на оборотомера.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Без приплъзване на съединителя</div>
        <div class="benefit-card-text">Формула, съвместима с мокри съединители — точен и предвидим контрол на мощността.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Контрол на температурата</div>
        <div class="benefit-card-text">Термична стабилност при условия на високо натоварване и температури от пистата.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита на трансмисията</div>
        <div class="benefit-card-text">Плавна работа на скоростната кутия дори при агресивно превключване.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Спортни и туристически мотоциклети; модели с мокър съединител и обща система за смазване; мотоциклети, използвани както за ежедневие, така и за писта.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-auto-commercial.html'] = (
"Търговски превозни средства — Gulf Oil България",
"Gulf продукти за търговски превозни средства — Решения за камиони, бусове и търговски флоти — формулирани за дълги пробези, високо натоварване и максимална надеждност.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/trackhouse-race-3.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-automotive.html">Автомобилни</a> › Търговски превозни средства</div>
    <div class="page-hero-eyebrow">Автомобилни · Продукт</div>
    <h1 class="page-hero-title">Търговски превозни <span>средства</span></h1>
    <p class="page-hero-sub">Решения за камиони, бусове и търговски флоти — формулирани за дълги пробези, високо натоварване и максимална надеждност.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Издръжливост за<br><span>дългия път</span></h2>
        <div class="prose">
          <p>Търговските превозни средства прекарват по-голямата част от времето си в експлоатация — дълги пробези, тежки товари и стриктни графици. Маслата на Gulf за този сегмент са създадени да поддържат двигателя защитен между сервизните прегледи.</p>
          <p>Гамата отговаря на съвременните стандарти за дизелови двигатели с ниски емисии, като същевременно остава съвместима с по-стари модели в експлоатация.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/mclaren-artura-front.jpg" alt="Търговски превозни средства" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">10W-40</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">API CK-4</div><div class="stat-block-label">Стандарт за дизелови двигатели</div></div>
      <div class="stat-block"><div class="stat-block-num">50000км</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">Флоти</div><div class="stat-block-label">Решения за паркове</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf продукти за търговски превозни средства</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">По-малко престой</div>
        <div class="benefit-card-text">По-дълги интервали между смените означават повече време на път и по-малко разходи за поддръжка.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита при тежък товар</div>
        <div class="benefit-card-text">Стабилна защита на двигателя дори при максимално натоварване и продължителна работа.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Контрол на саждите</div>
        <div class="benefit-card-text">Поддържа чистотата на филтрите за твърди частици и системите за намаляване на емисиите.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Решения за цели флоти</div>
        <div class="benefit-card-text">Последователна защита и опростена логистика за компании с голям брой превозни средства.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Камиони и влекачи на далечни разстояния; градски и междуградски автобуси; бусове и лекотоварни търговски превозни средства.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-ind-industrial.html'] = (
"Индустриални масла — Gulf Oil България",
"Gulf индустриални масла — Решения за редуктори, компресори, турбини и общо производствено оборудване — формулирани за стабилна работа при продължително натоварване.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/sector-industrial.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-industrial-marine.html">Индустрия</a> › Индустриални масла</div>
    <div class="page-hero-eyebrow">Индустрия · Продукт</div>
    <h1 class="page-hero-title">Индустриални <span>масла</span></h1>
    <p class="page-hero-sub">Решения за редуктори, компресори, турбини и общо производствено оборудване — формулирани за стабилна работа при продължително натоварване.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Надеждност за<br><span>непрекъснато производство</span></h2>
        <div class="prose">
          <p>Индустриалното оборудване често работи денонощно, без прекъсване. Маслата на Gulf за индустриални приложения са създадени да издържат на тези изисквания, поддържайки стабилна защита на компонентите между планираните обслужвания.</p>
          <p>Гамата покрива широк спектър от приложения — от тежко натоварени редуктори до високоскоростни турбини и компресорни системи.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/marine-hero.jpg" alt="Индустриални масла" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">ISO 220</div><div class="stat-block-label">Клас на вискозност</div></div>
      <div class="stat-block"><div class="stat-block-num">DIN 51517</div><div class="stat-block-label">Индустриален стандарт</div></div>
      <div class="stat-block"><div class="stat-block-num">4000ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">24/7</div><div class="stat-block-label">Непрекъсната работа</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf индустриални масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Стабилност при натоварване</div>
        <div class="benefit-card-text">Поддържа защитна маслена пленка дори при високи механични и термични натоварвания.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Удължен живот на оборудването</div>
        <div class="benefit-card-text">Намалено триене и износване на зъбни колела, лагери и уплътнения.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Устойчивост на окисление</div>
        <div class="benefit-card-text">По-дълъг експлоатационен живот на маслото между планираните смени.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-малко непланирани спирания</div>
        <div class="benefit-card-text">Последователна защита намалява риска от аварийни престои на производствени линии.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Промишлени редуктори и трансмисии; компресорни и турбинни системи; общо производствено и поточно оборудване с непрекъснат режим на работа.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-ind-hydraulic.html'] = (
"Хидравлични масла — Gulf Oil България",
"Gulf хидравлични масла — Надеждна и прецизна работа на хидравличните системи в производствена среда — устойчивост на високо налягане и температурни колебания.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/marine-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-industrial-marine.html">Индустрия</a> › Хидравлични масла</div>
    <div class="page-hero-eyebrow">Индустрия · Продукт</div>
    <h1 class="page-hero-title">Хидравлични <span>масла</span></h1>
    <p class="page-hero-sub">Надеждна и прецизна работа на хидравличните системи в производствена среда — устойчивост на високо налягане и температурни колебания.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Прецизност в<br><span>сърцето на системата</span></h2>
        <div class="prose">
          <p>Хидравличните системи в производствена среда изискват течности, способни да поддържат стабилно налягане и точен отклик при променливи условия на работа и температура.</p>
          <p>Маслата на Gulf за индустриална хидравлика осигуряват последователна защита на помпи, клапани и цилиндри — компоненти, чиято подмяна е скъпа и времеемка.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/sector-industrial.jpg" alt="Хидравлични масла" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">ISO 46</div><div class="stat-block-label">Клас на вискозност</div></div>
      <div class="stat-block"><div class="stat-block-num">DIN 51524</div><div class="stat-block-label">Хидравличен стандарт</div></div>
      <div class="stat-block"><div class="stat-block-num">4000ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">±1%</div><div class="stat-block-label">Точност на налягането</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf хидравлични масла</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Точен отклик на системата</div>
        <div class="benefit-card-text">Постоянна вискозност при различни температури осигурява предвидимо поведение на хидравликата.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита на прецизни компоненти</div>
        <div class="benefit-card-text">Намалява износването на помпи и клапани с тесни допуски.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Устойчивост на пенене</div>
        <div class="benefit-card-text">Контролирано поведение при високо налягане запазва стабилността на системата.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълъг живот на маслото</div>
        <div class="benefit-card-text">Висока устойчивост на окисление намалява честотата на подмяна и разходите за поддръжка.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Хидравлични преси и формовъчни машини; системи за управление на производствени линии; мобилна индустриална техника с хидравлично задвижване.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-ind-heat-transfer.html'] = (
"Масла за топлопренос — Gulf Oil България",
"Gulf масла за топлопренос — Термична стабилност при високи температури — за процеси, изискващи прецизен и постоянен контрол на топлинния пренос.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/sector-industrial.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-industrial-marine.html">Индустрия</a> › Масла за топлопренос</div>
    <div class="page-hero-eyebrow">Индустрия · Продукт</div>
    <h1 class="page-hero-title">Масла за <span>топлопренос</span></h1>
    <p class="page-hero-sub">Термична стабилност при високи температури — за процеси, изискващи прецизен и постоянен контрол на топлинния пренос.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Стабилност при<br><span>екстремна топлина</span></h2>
        <div class="prose">
          <p>Системите за топлопренос работят при едни от най-високите температури в индустриална среда. Маслата на Gulf са формулирани да запазват стабилни характеристики продължително време, без да се разграждат термично.</p>
          <p>Това осигурява последователен и предвидим пренос на топлина — критично условие за качеството и безопасността на индустриалните процеси.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/marine-secondary.jpg" alt="Масла за топлопренос" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">320°C</div><div class="stat-block-label">Макс. работна температура</div></div>
      <div class="stat-block"><div class="stat-block-num">ISO 6743-12</div><div class="stat-block-label">Стандарт за топлопренос</div></div>
      <div class="stat-block"><div class="stat-block-num">8000ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">Ниско</div><div class="stat-block-label">Образуване на утайки</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf масла за топлопренос</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Висока термична стабилност</div>
        <div class="benefit-card-text">Запазва свойствата си продължително при работа на горната граница на температурния диапазон.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-малко утайки и нагар</div>
        <div class="benefit-card-text">Чисти системи за топлопренос и по-малко необходимост от почистване на тръбопроводи.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Последователен пренос на топлина</div>
        <div class="benefit-card-text">Стабилни характеристики осигуряват предвидимост на индустриалните процеси.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълъг живот на системата</div>
        <div class="benefit-card-text">Намалена корозия и износване на компонентите на системата за топлопренос.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Системи за индустриално отопление и охлаждане; процеси в химическата и хранително-вкусовата промишленост; централизирани отоплителни инсталации в производствени съоръжения.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-ind-grease.html'] = (
"Смазки — Gulf Oil България",
"Gulf смазки — Дълготрайна защита на лагери, шарнири и движещи се части при тежки условия — намалено триене и удължен експлоатационен живот.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/marine-secondary.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-industrial-marine.html">Индустрия</a> › Смазки</div>
    <div class="page-hero-eyebrow">Индустрия · Продукт</div>
    <h1 class="page-hero-title"><span>Смазки</span></h1>
    <p class="page-hero-sub">Дълготрайна защита на лагери, шарнири и движещи се части при тежки условия — намалено триене и удължен експлоатационен живот.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Защита там,<br><span>където маслото не достига</span></h2>
        <div class="prose">
          <p>Някои възли — лагери, шарнири, водачи — изискват не масло, а смазка: продукт, който остава на място и продължава да защитава дори при вибрации, високо налягане или излагане на влага и прах.</p>
          <p>Гамата смазки на Gulf покрива широк диапазон от индустриални приложения, осигурявайки последователна защита независимо от условията на средата.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/sector-marine.jpg" alt="Смазки" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">NLGI 2</div><div class="stat-block-label">Клас на смазката</div></div>
      <div class="stat-block"><div class="stat-block-num">Литиев комплекс</div><div class="stat-block-label">Тип сгъстител</div></div>
      <div class="stat-block"><div class="stat-block-num">−20°C</div><div class="stat-block-label">Работна температура</div></div>
      <div class="stat-block"><div class="stat-block-num">Високо</div><div class="stat-block-label">Натоварване на лагерите</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf смазки</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Останала на място защита</div>
        <div class="benefit-card-text">Не се отмива лесно от вода или вибрации — продължава да предпазва дори в тежки условия.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Широк температурен диапазон</div>
        <div class="benefit-card-text">Запазва консистенцията си както при ниски, така и при високи работни температури.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Защита от корозия</div>
        <div class="benefit-card-text">Бариера срещу влага и агресивни вещества, предпазваща металните повърхности.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">По-дълги интервали на смазване</div>
        <div class="benefit-card-text">По-малко планирана поддръжка и по-ниски разходи за труд и материали.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Индустриални лагери и електродвигатели; шарнирни съединения и водачи на конвейери; оборудване, изложено на влага, прах или високи натоварвания.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

PAGES['product-marine-lubricants.html'] = (
"Морски смазочни материали — Gulf Oil България",
"Gulf морски смазочни материали — Защита на двигатели и системи в открито море — от малки риболовни лодки до големи търговски кораби, изградени да издържат на солена вода и продължителна работа.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/marine-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › <a href="products-industrial-marine.html">Море</a> › Морски смазочни материали</div>
    <div class="page-hero-eyebrow">Море · Продукт</div>
    <h1 class="page-hero-title">Морски смазочни <span>материали</span></h1>
    <p class="page-hero-sub">Защита на двигатели и системи в открито море — от малки риболовни лодки до големи търговски кораби, изградени да издържат на солена вода и продължителна работа.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal">
      <div>
        <div class="section-label">Какво представлява</div>
        <h2 class="section-title">Издръжливост в<br><span>най-суровата среда</span></h2>
        <div class="prose">
          <p>Морската среда поставя едни от най-тежките изисквания пред смазочните материали — постоянен контакт със солена вода, продължителна непрекъсната работа и резки промени в натоварването на двигателите.</p>
          <p>Продуктите на Gulf за морския сектор са формулирани да устояват именно на тези условия, осигурявайки последователна защита на двигатели, трансмисии и палубно оборудване.</p>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:320px;">
        <img src="images/sector-marine.jpg" alt="Морски смазочни материали" style="border-radius:16px;">
      </div>
    </div>

    <div class="stats-strip reveal reveal-delay-1">
      <div class="stat-block"><div class="stat-block-num">15W-40</div><div class="stat-block-label">Основна спецификация</div></div>
      <div class="stat-block"><div class="stat-block-num">API CF</div><div class="stat-block-label">Морски стандарт</div></div>
      <div class="stat-block"><div class="stat-block-num">500ч</div><div class="stat-block-label">Препоръчителен интервал</div></div>
      <div class="stat-block"><div class="stat-block-num">Соленост</div><div class="stat-block-label">Устойчивост на корозия</div></div>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Предимства</div>
        <h2 class="section-title">Защо да изберете<br><span>Gulf морски смазочни материали</span></h2>
      </div>
    </div>
    <div class="benefit-grid reveal">
      <div class="benefit-card">
        <div class="benefit-card-title">Защита от корозия</div>
        <div class="benefit-card-text">Бариера срещу солена вода и влага, предпазваща метални компоненти от ръжда и разяждане.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Стабилност при продължителна работа</div>
        <div class="benefit-card-text">Поддържа защитни свойства дори при дни наред непрекъсната експлоатация на двигателя.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Контрол на отлаганията</div>
        <div class="benefit-card-text">Поддържа чисти горивни системи и намалява риска от засядане на компоненти.</div>
      </div>
      <div class="benefit-card">
        <div class="benefit-card-title">Надеждност в открито море</div>
        <div class="benefit-card-text">Последователна защита, на която можете да разчитате далеч от брега и сервизната база.</div>
      </div>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="section-header reveal">
      <div>
        <div class="section-label">Подходящо за</div>
        <h2 class="section-title">Гамата<br><span>в действие</span></h2>
      </div>
    </div>
    <div class="prose">
      <p>Риболовни и развлекателни плавателни съдове; търговски кораби и фериботи; палубно оборудване и спомагателни системи на борда.</p>
    </div>
    <div style="margin-top:28px;">
      <a href="contact.html" class="btn-primary">Свържете се с нас за повече информация →</a>
    </div>
  </div>
</section>
""")

# ============================================================
# PRODUCTS — AGRICULTURE
# ============================================================
PAGES['products-agriculture.html'] = (
"Земеделска техника — Продукти — Gulf Oil България",
"Масла, трансмисионни и хидравлични течности на Gulf за земеделска техника и оборудване.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/agri-hero.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Продукти › Земеделие</div>
    <div class="page-hero-eyebrow">Продукти</div>
    <h1 class="page-hero-title">Решения за<br><span>земеделска техника</span></h1>
    <p class="page-hero-sub">Земеделската работа поставя сериозни изисквания към машините — прах, високи натоварвания и продължителна работа. Продуктите на Gulf са разработени именно за тези условия.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">
    <div class="two-col reveal" style="margin-bottom:48px;">
      <div>
        <div class="section-label">Продуктова гама</div>
        <h2 class="section-title">Пълна защита<br><span>във всяко поле</span></h2>
        <p class="section-body">От двигателя до хидравликата — Gulf предлага решения за всеки компонент на вашата техника.</p>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:260px;">
        <img src="images/agri-secondary.jpg" alt="Земеделска работа" style="border-radius:16px;">
      </div>
    </div>
    <div class="product-card-grid">
      <a href="product-agri-engine-oil.html" class="product-card reveal reveal-delay-1">
        <div class="product-card-img"><img src="images/agri-hero.jpg" alt="Моторни масла"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Земеделие</span>
          <div class="product-card-title">Моторни масла</div>
          <div class="product-card-desc">Защита на двигателя при продължителна работа с високо натоварване и в прашна среда.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-agri-transmission.html" class="product-card reveal reveal-delay-2">
        <div class="product-card-img"><img src="images/agri-secondary.jpg" alt="Трансмисионни течности"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Земеделие</span>
          <div class="product-card-title">Трансмисионни течности</div>
          <div class="product-card-desc">Плавно превключване и удължен живот на трансмисията при тежки товари.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-agri-hydraulic.html" class="product-card reveal reveal-delay-3">
        <div class="product-card-img"><img src="images/sector-industrial.jpg" alt="Хидравлични масла"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Земеделие</span>
          <div class="product-card-title">Хидравлични масла</div>
          <div class="product-card-desc">Стабилна работа на хидравличните системи — от навесно оборудване до товарачи.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-agri-stou.html" class="product-card reveal reveal-delay-4">
        <div class="product-card-img"><img src="images/marine-hero.jpg" alt="STOU масла"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Земеделие</span>
          <div class="product-card-title">STOU масла</div>
          <div class="product-card-desc">Универсална формула за двигател, трансмисия и хидравлика в едно решение.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-agri-chain.html" class="product-card reveal reveal-delay-1">
        <div class="product-card-img"><img src="images/agri-hero.jpg" alt="Верижни масла"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Земеделие</span>
          <div class="product-card-title">Верижни масла</div>
          <div class="product-card-desc">Специализирана защита срещу износване на вериги и движещи се части.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-agri-supplementary.html" class="product-card reveal reveal-delay-2">
        <div class="product-card-img"><img src="images/agri-secondary.jpg" alt="Спомагателни продукти"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Земеделие</span>
          <div class="product-card-title">Спомагателни продукти</div>
          <div class="product-card-desc">Грес, добавки и поддържащи продукти за пълна грижа за вашата техника.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- DEALER CTA -->
<div class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="cta-title">Нужна ви е консултация<br>за вашата техника?</div>
      <div class="cta-sub">Нашият екип и дилърската ни мрежа ще ви помогнат да изберете правилния продукт</div>
    </div>
    <a href="dealer-locator.html" class="btn-white">Намери дилър →</a>
  </div>
</div>
""")

# ============================================================
# PRODUCTS — INDUSTRIAL & MARINE
# ============================================================
PAGES['products-industrial-marine.html'] = (
"Индустрия и море — Продукти — Gulf Oil България",
"Индустриални и морски смазочни материали на Gulf — хидравлични масла, масла за топлопренос и решения за морски двигатели.",
"""
<section class="page-hero" style="background-image:linear-gradient(120deg, rgba(17,29,71,0.93) 0%, rgba(27,45,107,0.82) 100%), url('images/sector-marine.jpg');">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="index.html">Начало</a> › Продукти › Индустрия и море</div>
    <div class="page-hero-eyebrow">Продукти</div>
    <h1 class="page-hero-title">Индустрия<br><span>и море</span></h1>
    <p class="page-hero-sub">Когато спирането на машините не е опция, изборът на правилния смазочен материал има значение. Gulf предлага решения, изпитани в най-взискателните индустриални и морски приложения.</p>
  </div>
</section>

<section class="content-section">
  <div class="section-inner">

    <div class="two-col reveal" style="margin-bottom:48px;">
      <div>
        <div class="section-label">Индустрия</div>
        <h2 class="section-title anchor-offset" id="industrial">Индустриални<br><span>смазочни материали</span></h2>
        <p class="section-body">Пълна гама продукти за машини, съоръжения и производствени процеси.</p>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:260px;">
        <img src="images/sector-industrial.jpg" alt="Индустриални смазочни материали" style="border-radius:16px;">
      </div>
    </div>
    <div class="product-card-grid">
      <a href="product-ind-industrial.html" class="product-card reveal reveal-delay-1">
        <div class="product-card-img"><img src="images/sector-industrial.jpg" alt="Индустриални масла"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Индустрия</span>
          <div class="product-card-title">Индустриални масла</div>
          <div class="product-card-desc">Решения за редуктори, компресори, турбини и общо производствено оборудване.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-ind-hydraulic.html" class="product-card reveal reveal-delay-2 anchor-offset" id="hydraulic">
        <div class="product-card-img"><img src="images/marine-hero.jpg" alt="Хидравлични масла"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Индустрия</span>
          <div class="product-card-title">Хидравлични масла</div>
          <div class="product-card-desc">Надеждна и прецизна работа на хидравличните системи в производствена среда.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-ind-heat-transfer.html" class="product-card reveal reveal-delay-3 anchor-offset" id="heat-transfer">
        <div class="product-card-img"><img src="images/marine-secondary.jpg" alt="Масла за топлопренос"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Индустрия</span>
          <div class="product-card-title">Масла за топлопренос</div>
          <div class="product-card-desc">Термична стабилност при високи температури за прецизен контрол на топлината.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
      <a href="product-ind-grease.html" class="product-card reveal reveal-delay-4">
        <div class="product-card-img"><img src="images/sector-marine.jpg" alt="Смазки"></div>
        <div class="product-card-body">
          <span class="product-card-tag">Индустрия</span>
          <div class="product-card-title">Смазки</div>
          <div class="product-card-desc">Дълготрайна защита на лагери и движещи се части при тежки условия.</div>
          <div class="product-card-link">Разгледай продукта →</div>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="content-section alt">
  <div class="section-inner">
    <div class="two-col reveal anchor-offset" id="marine">
      <div>
        <div class="section-label">Море</div>
        <h2 class="section-title">Морски<br><span>смазочни материали</span></h2>
        <div class="prose">
          <p>Морската среда поставя едни от най-тежките изисквания пред смазочните материали — солена вода, продължителна работа и резки промени в натоварването. Продуктите на Gulf за морския сектор са разработени да устояват именно на тези условия.</p>
          <p>Гамата покрива нуждите от малки риболовни лодки до големи търговски кораби — осигурявайки защита на двигателите и системите в открито море.</p>
        </div>
        <div style="margin-top:24px;display:flex;gap:14px;flex-wrap:wrap;">
          <a href="product-marine-lubricants.html" class="btn-primary">Разгледай продукта →</a>
          <a href="dealer-locator.html" class="btn-white" style="border:2px solid var(--navy);color:var(--navy);background:transparent;">Намери дилър →</a>
        </div>
      </div>
      <div class="about-image" style="border-radius:16px;min-height:340px;">
        <img src="images/marine-hero.jpg" alt="Морски смазочни материали" style="border-radius:16px;">
      </div>
    </div>
  </div>
</section>

<!-- ADVISOR -->
<div class="advisor-banner">
  <div class="advisor-inner">
    <div class="advisor-text">
      <div class="advisor-icon">A</div>
      <div>
        <div class="advisor-label">Нуждаете се от съвет за вашето приложение?</div>
        <div class="advisor-sub">Свържете се с нашия екип за индустриални и морски решения</div>
      </div>
    </div>
    <a href="contact.html" class="advisor-btn">Свържете се с нас ›</a>
  </div>
</div>
""")
