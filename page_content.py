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
  <div class="hero-bg" style="background-image:url('images/hero-bg.jpg');"></div>
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
      <a href="products-automotive.html#cars" class="product-card reveal reveal-delay-1">
        <div class="product-card-img">
          <img src="images/product-automotive.jpg" alt="Автомобилни масла">
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Автомобилни</div>
          <div class="product-card-title">Леки автомобили</div>
          <div class="product-card-desc">Пълна гама от синтетични и полусинтетични масла за леки автомобили с бензинови и дизелови двигатели.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>

      <a href="products-automotive.html#commercial" class="product-card reveal reveal-delay-2">
        <div class="product-card-img">
          <img src="images/williams-helmets.jpg" alt="Търговски превозни средства">
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Автомобилни</div>
          <div class="product-card-title">Търговски превозни средства</div>
          <div class="product-card-desc">Специализирани продукти за камиони, автобуси и тежкотоварни превозни средства.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>

      <a href="products-agriculture.html" class="product-card reveal reveal-delay-3">
        <div class="product-card-img">
          <img src="images/agri-hero.jpg" alt="Земеделска техника">
        </div>
        <div class="product-card-body">
          <div class="product-card-tag">Земеделие</div>
          <div class="product-card-title">Земеделска техника</div>
          <div class="product-card-desc">Масла и трансмисионни течности, разработени за тежките условия на земеделска работа.</div>
          <div class="product-card-link">Виж продуктите →</div>
        </div>
      </a>

      <a href="products-industrial-marine.html#marine" class="product-card reveal reveal-delay-4">
        <div class="product-card-img">
          <img src="images/product-marine.jpg" alt="Морски смазочни материали">
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
          <img src="images/motorsport-stack-1.jpg" alt="Gulf Racing"><span class="partner-caption">McLaren Automotive</span>
        </div>
        <div class="ms-img">
          <img src="images/motorsport-stack-2.jpg" alt="Gulf Motorsport"><span class="partner-caption">TAG Heuer × Gulf</span>
        </div>
        <div class="ms-img">
          <img src="images/everrati-1.jpg" alt="Everrati електрическо Porsche">
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
      <div class="sector-bg" style="background-image: url('images/sector-marine.jpg'); background-position: center 40%;"></div>
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

<!-- DEALER CTA -->
<div class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="cta-title">Намерете Gulf дилър<br>близо до вас</div>
      <div class="cta-sub">Мрежа от сертифицирани дистрибутори в цяла България</div>
    </div>
    <a href="dealer-locator.html" class="btn-white">Намери дилър →</a>
  </div>
</div>
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
          <img src="images/partner-livery.jpg" alt="Историческа Gulf ливрея"><span class="partner-caption">ROFGO Collection</span>
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
      <div class="value-grid" style="grid-template-columns:1fr 1fr;margin-top:0;">
        <div class="value-card">
          <div class="value-card-icon">""" + icon("Re") + """</div>
          <div class="value-card-title">Рециклиране</div>
          <div class="value-card-text">Насърчаваме правилното събиране и обработка на отработени масла.</div>
        </div>
        <div class="value-card">
          <div class="value-card-icon">""" + icon("Ec") + """</div>
          <div class="value-card-title">По-чисти формули</div>
          <div class="value-card-text">Разработваме продукти с фокус върху ефективност и намалени емисии.</div>
        </div>
        <div class="value-card">
          <div class="value-card-icon">""" + icon("Pk") + """</div>
          <div class="value-card-title">Опаковки</div>
          <div class="value-card-text">Работим към по-устойчиви решения за опаковане и логистика.</div>
        </div>
        <div class="value-card">
          <div class="value-card-icon">""" + icon("Cm") + """</div>
          <div class="value-card-title">Общности</div>
          <div class="value-card-text">Подкрепяме инициативи на местните общности, в които оперираме.</div>
        </div>
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
          <div class="ms-img ms-img-tall"><img src="images/motorsport-stack-1.jpg" alt="Gulf Racing"><span class="partner-caption">McLaren Automotive</span></div>
          <div class="ms-img"><img src="images/motorsport-stack-2.jpg" alt="Gulf Motorsport"><span class="partner-caption">TAG Heuer × Gulf</span></div>
          <div class="ms-img"><img src="images/williams-helmets.jpg" alt="Williams Racing каски"></div>
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
        <img src="images/trackhouse-1.jpg" alt="Trackhouse MotoGP">
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
        <img src="images/motorsport-stack-1.jpg" alt="McLaren Automotive">
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
        <img src="images/everrati-2.jpg" alt="Everrati">
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
        <img src="images/partner-livery.jpg" alt="ROFGO Collection">
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
        <img src="images/motorsport-stack-2.jpg" alt="TAG Heuer">
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
        <div class="news-list-thumb"><img src="images/trackhouse-1.jpg" alt="Trackhouse MotoGP"><span class="partner-caption">Trackhouse Racing — MotoGP</span></div>
        <div>
          <span class="news-card-tag">Мотоспорт</span>
          <div class="news-card-title">Trackhouse MotoGP стартира сезона с цветовете на Gulf</div>
          <div class="news-card-excerpt">Леджендарните бои в синьо и оранжево се завръщат на пистата — този път в света на MotoGP.</div>
          <div class="news-card-date">Февруари 2026</div>
        </div>
      </a>

      <a href="#" class="news-list-item reveal">
        <div class="news-list-thumb"><img src="images/everrati-1.jpg" alt="Съветник за смазочни материали"></div>
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
        <div style="margin-top:20px;"><a href="https://europe.gulfoilltd.com/lubricantadvisor" target="_blank" class="btn-primary">Намерете продукт за вашия автомобил →</a></div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="motorcycle">
      <div class="partner-media"><img src="images/everrati-1.jpg" alt="Мотоциклетни масла"><span class="partner-caption">Изпитани в условията на пистата</span></div>
      <div>
        <div class="partner-tag">Мотоциклети</div>
        <h2 class="partner-title">Мотоциклетни масла</h2>
        <p class="partner-text">Специализирани формули за двутактови и четиритактови мотоциклетни двигатели — осигуряващи защита при високи обороти, плавно превключване и дълготрайна издръжливост на двигателя и съединителя.</p>
        <p class="partner-text">Технологиите от партньорството ни с Trackhouse MotoGP пряко се пренасят в продуктите от тази гама — изпитани в най-екстремните условия на пистата.</p>
        <div class="partner-highlight">Подкрепени от наследството ни в MotoGP</div>
      </div>
    </div>

    <div class="partner-block anchor-offset reveal" id="commercial">
      <div class="partner-media"><img src="images/williams-helmets.jpg" alt="Търговски превозни средства"><span class="partner-caption">Търговски флоти — Gulf продукти</span></div>
      <div>
        <div class="partner-tag">Търговски флоти</div>
        <h2 class="partner-title">Търговски превозни средства</h2>
        <p class="partner-text">Продукти, разработени за камиони, автобуси и тежкотоварни превозни средства — намаляващи разходите за поддръжка и удължаващи живота на двигателя при интензивна експлоатация.</p>
        <p class="partner-text">Гамата включва моторни масла, трансмисионни и хидравлични течности, отговарящи на изискванията на водещите производители на двигатели.</p>
        <div class="partner-highlight">Издържливост при тежки и продължителни натоварвания</div>
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
    <div class="value-grid" style="margin-top:0;">
      <div class="value-card anchor-offset reveal reveal-delay-1" id="engine">
        <div class="value-card-icon">""" + icon("En") + """</div>
        <div class="value-card-title">Моторни масла</div>
        <div class="value-card-text">Защита на двигателя при продължителна работа с високо натоварване и в прашна среда.</div>
      </div>
      <div class="value-card anchor-offset reveal reveal-delay-2" id="transmission">
        <div class="value-card-icon">""" + icon("Tr") + """</div>
        <div class="value-card-title">Трансмисионни течности</div>
        <div class="value-card-text">Плавна работа на трансмисията и удължен живот на компонентите при тежки условия.</div>
      </div>
      <div class="value-card anchor-offset reveal reveal-delay-3" id="hydraulic">
        <div class="value-card-icon">""" + icon("Hy") + """</div>
        <div class="value-card-title">Хидравлични масла</div>
        <div class="value-card-text">Надеждна работа на хидравличните системи — от навесно оборудване до товарачи.</div>
      </div>
      <div class="value-card anchor-offset reveal reveal-delay-4" id="stou">
        <div class="value-card-icon">""" + icon("St") + """</div>
        <div class="value-card-title">STOU масла</div>
        <div class="value-card-text">Универсални формули за двигател, трансмисия и хидравлика в едно решение — опростяващи поддръжката.</div>
      </div>
      <div class="value-card anchor-offset reveal reveal-delay-1" id="chain">
        <div class="value-card-icon">""" + icon("Ch") + """</div>
        <div class="value-card-title">Верижни масла</div>
        <div class="value-card-text">Специализирана защита срещу износване на вериги и движещи се части на техниката.</div>
      </div>
      <div class="value-card reveal reveal-delay-2">
        <div class="value-card-icon">""" + icon("Sp") + """</div>
        <div class="value-card-title">Спомагателни продукти</div>
        <div class="value-card-text">Грес, добавки и поддържащи продукти за пълна грижа за вашата техника.</div>
      </div>
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
    <div class="value-grid" style="margin-top:0;">
      <div class="value-card reveal reveal-delay-1">
        <div class="value-card-icon">""" + icon("In") + """</div>
        <div class="value-card-title">Индустриални масла</div>
        <div class="value-card-text">Решения за редуктори, компресори и общо производствено оборудване.</div>
      </div>
      <div class="value-card reveal reveal-delay-2 anchor-offset" id="hydraulic">
        <div class="value-card-icon">""" + icon("Hy") + """</div>
        <div class="value-card-title">Хидравлични масла</div>
        <div class="value-card-text">Надеждна работа на хидравличните системи в производствена среда.</div>
      </div>
      <div class="value-card reveal reveal-delay-3 anchor-offset" id="heat-transfer">
        <div class="value-card-icon">""" + icon("Ht") + """</div>
        <div class="value-card-title">Масла за топлопренос</div>
        <div class="value-card-text">Стабилност при високи температури за процеси, изискващи прецизен контрол на топлината.</div>
      </div>
      <div class="value-card reveal reveal-delay-4">
        <div class="value-card-icon">""" + icon("Gr") + """</div>
        <div class="value-card-title">Смазки</div>
        <div class="value-card-text">Дълготрайна защита на лагери и движещи се части при тежки условия.</div>
      </div>
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
        <div style="margin-top:24px;"><a href="dealer-locator.html" class="btn-primary">Намери дилър →</a></div>
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
