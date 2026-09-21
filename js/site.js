// Weston Broadrick Studio — the small bits of behavior the site needs.
(function () {
  var body = document.body;
  var header = document.querySelector(".site-header");

  // 1. Header turns solid once you scroll past the top of the page
  function onScroll() {
    var solidAt = body.classList.contains("has-hero") ? window.innerHeight * 0.7 : 10;
    header.classList.toggle("is-solid", window.scrollY > solidAt);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // 2. Phone menu open/close
  var btn = document.querySelector(".menu-btn");
  if (btn) {
    btn.addEventListener("click", function () {
      var open = body.classList.toggle("menu-open");
      btn.setAttribute("aria-expanded", open);
      btn.textContent = open ? "Close" : "Menu";
    });
  }

  // 3. Fade sections up as they scroll into view
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // 4. Lightbox: tap any gallery photo to see it full-screen, arrows/swipe to move
  var photos = Array.prototype.slice.call(document.querySelectorAll(".gallery img"));
  if (!photos.length) return;

  var box = document.createElement("div");
  box.className = "lightbox";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-label", "Photo viewer");
  box.innerHTML =
    '<img alt="">' +
    '<button class="lb-close" type="button">Close</button>' +
    '<button class="lb-prev" type="button">Prev</button>' +
    '<button class="lb-next" type="button">Next</button>' +
    '<div class="lb-count eyebrow"></div>';
  body.appendChild(box);
  var big = box.querySelector("img");
  var count = box.querySelector(".lb-count");
  var current = 0;

  function show(i) {
    current = (i + photos.length) % photos.length;
    big.src = photos[current].getAttribute("data-full") || photos[current].currentSrc || photos[current].src;
    big.alt = photos[current].alt;
    count.textContent = (current + 1) + " / " + photos.length;
  }
  function open(i) { show(i); box.classList.add("open"); box.querySelector(".lb-close").focus(); }
  function close() { box.classList.remove("open"); photos[current].focus && photos[current].focus(); }

  photos.forEach(function (img, i) {
    img.tabIndex = 0;
    img.addEventListener("click", function () { open(i); });
    img.addEventListener("keydown", function (e) { if (e.key === "Enter") open(i); });
  });
  box.querySelector(".lb-close").addEventListener("click", close);
  box.querySelector(".lb-prev").addEventListener("click", function () { show(current - 1); });
  box.querySelector(".lb-next").addEventListener("click", function () { show(current + 1); });
  box.addEventListener("click", function (e) { if (e.target === box) close(); });
  document.addEventListener("keydown", function (e) {
    if (!box.classList.contains("open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "ArrowRight") show(current + 1);
  });
  // swipe on phones
  var startX = null;
  box.addEventListener("touchstart", function (e) { startX = e.touches[0].clientX; }, { passive: true });
  box.addEventListener("touchend", function (e) {
    if (startX === null) return;
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
    startX = null;
  });
})();
