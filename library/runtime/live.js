/* Design Library — live layer.
   Makes any template preview feel alive without touching its markup: scroll reveal, count-up numbers,
   hover lift, scroll progress, parallax, headline reveal, magnetic buttons, card tilt, cursor ring.
   Modules are chosen per template (window.LIVE = ['reveal','count',...]). Respects prefers-reduced-motion. */
(function () {
  var L = window.LIVE || [];
  if (!L.length || !window.IntersectionObserver) return;
  if (matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  var d = document, h = d.documentElement, fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  var has = function (m) { return L.indexOf(m) > -1; };
  var all = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)); };
  h.classList.add('live');

  /* ── reveal: fade/slide content in as it scrolls into view ── */
  if (has('reveal')) {
    var sel = 'main section > .wrap > *, main section > .in > *, main .card, main .art, main .mi, main figure, main .step, main .qcard, main li.row, main .row';
    var targets = all(sel).filter(function (e) { return !e.closest('nav,header,footer') && !e.classList.contains('head'); });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        var t = en.target; io.unobserve(t); t.classList.add('lv-in');
        setTimeout(function () { t.classList.remove('lv-r', 'lv-in'); t.style.removeProperty('--d'); }, 1100);
      });
    }, { threshold: .1, rootMargin: '0px 0px -6% 0px' });
    targets.forEach(function (e, i) {
      var r = e.getBoundingClientRect();
      e.classList.add('lv-r'); e.style.setProperty('--d', ((i % 4) * 70) + 'ms'); io.observe(e);
    });
  }

  /* ── count: numbers that count up the first time they are seen ── */
  if (has('count')) {
    var re = /^(RM\s?|\$|£|€)?(\d[\d,]*\.?\d*)\s?(k|K|m|M|%|\+|x|yrs?|d|g|W|ms|min)?$/;
    var cands = all('main b,main strong,main span,main div,main h3,main h4,main i').filter(function (e) {
      if (e.children.length || !re.test(e.textContent.trim())) return false;
      var fs = parseFloat(getComputedStyle(e).fontSize); return fs >= 26 && !e.closest('form,select,option,.price,.amt,time');
    });
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return; var e = en.target; cio.unobserve(e);
        var m = re.exec(e.textContent.trim()), txt = e.textContent, pre = m[1] || '', suf = m[3] || '';
        var raw = m[2], dec = (raw.split('.')[1] || '').length, target = parseFloat(raw.replace(/,/g, '')), comma = raw.indexOf(',') > -1;
        var t0 = performance.now(), dur = 1100;
        (function tick(t) {
          var p = Math.min(1, (t - t0) / dur), v = target * (1 - Math.pow(1 - p, 3));
          var s = dec ? v.toFixed(dec) : Math.round(v).toString();
          if (comma) s = s.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
          e.textContent = pre + (pre.length > 1 ? '' : '') + s + (suf ? (/^[a-z]/i.test(suf) && suf.length > 1 ? ' ' : '') + suf : '');
          if (p < 1) requestAnimationFrame(tick); else e.textContent = txt;
        })(t0);
      });
    }, { threshold: .6 });
    cands.forEach(function (e) { cio.observe(e); });
  }

  /* ── lift: cards and buttons rise on hover (and on tap via :active) ── */
  if (has('lift')) {
    all('main .card, main .art, main .mi, main figure, main .qcard, main .btn, main .step').forEach(function (e) { e.classList.add('lv-lift'); });
  }

  /* ── progress: thin reading-progress bar at the top ── */
  if (has('progress')) {
    var bar = d.createElement('i'); bar.className = 'lv-bar'; d.body.appendChild(bar);
    var up = function () { var m = h.scrollHeight - innerHeight; bar.style.transform = 'scaleX(' + (m > 0 ? Math.min(1, scrollY / m) : 0) + ')'; };
    addEventListener('scroll', up, { passive: true }); up();
  }

  /* ── parallax: hero imagery drifts slower than the page ── */
  if (has('parallax')) {
    var hp = all('main > section:first-child .ph, main > section:first-child img, main .hero .ph').slice(0, 4), tk = false;
    var ps = function () { tk = false; var y = Math.min(scrollY, 900); hp.forEach(function (e, i) { e.style.transform = 'translate3d(0,' + (y * (.08 + i * .03)) + 'px,0)'; }); };
    addEventListener('scroll', function () { if (!tk) { tk = true; requestAnimationFrame(ps); } }, { passive: true });
  }

  /* ── headline: first h1 reveals word by word ── */
  if (has('headline')) {
    var h1 = d.querySelector('main h1');
    if (h1 && !h1.querySelector('*') && h1.textContent.trim().length < 90) {
      var words = h1.textContent.trim().split(/\s+/);
      h1.setAttribute('aria-label', h1.textContent.trim());
      h1.innerHTML = words.map(function (w, i) { return '<span class="lv-w" aria-hidden="true" style="--i:' + i + '">' + w + '</span>'; }).join(' ');
    }
  }

  /* ── magnetic buttons + card tilt + cursor ring (mouse only) ── */
  if (fine) {
    if (has('magnetic')) {
      all('main .btn, main button.btn, main a.btn, nav .btn, header .btn').forEach(function (b) {
        b.classList.add('lv-mag');
        b.addEventListener('pointermove', function (e) {
          var r = b.getBoundingClientRect(), x = e.clientX - (r.left + r.width / 2), y = e.clientY - (r.top + r.height / 2);
          b.style.transform = 'translate(' + x * .18 + 'px,' + y * .28 + 'px)';
        });
        b.addEventListener('pointerleave', function () { b.style.transform = ''; });
      });
    }
    if (has('tilt')) {
      all('main .card, main .art, main .mi, main figure').slice(0, 24).forEach(function (c) {
        c.classList.add('lv-tilt');
        c.addEventListener('pointermove', function (e) {
          var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
          c.style.transform = 'perspective(800px) rotateY(' + x * 8 + 'deg) rotateX(' + -y * 8 + 'deg) translateY(-4px)';
        });
        c.addEventListener('pointerleave', function () { c.style.transform = ''; });
      });
    }
    if (has('cursor')) {
      var ring = d.createElement('i'); ring.className = 'lv-ring'; d.body.appendChild(ring);
      var tx = -100, ty = -100, rx = -100, ry = -100;
      addEventListener('pointermove', function (e) { tx = e.clientX; ty = e.clientY; ring.classList.toggle('lv-hov', !!(e.target.closest && e.target.closest('a,button,.btn'))); }, { passive: true });
      (function loop() { rx += (tx - rx) * .18; ry += (ty - ry) * .18; ring.style.transform = 'translate3d(' + rx + 'px,' + ry + 'px,0)'; requestAnimationFrame(loop); })();
    }
  }
})();
