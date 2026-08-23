// Gemeinsames Skript für Filter (Startseite) und Ablauf-Stepper (Detailseiten)

document.addEventListener("DOMContentLoaded", () => {

  // --- Kategorie-Filter auf der Startseite ---
  const filterButtons = document.querySelectorAll(".filter-btn");
  const karten = document.querySelectorAll(".projekt-karte");

  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("aktiv"));
      btn.classList.add("aktiv");

      const filter = btn.dataset.filter;
      karten.forEach((karte) => {
        const zeigen = filter === "alle" || karte.dataset.kategorie === filter;
        karte.classList.toggle("versteckt", !zeigen);
      });
    });
  });

  // --- Ablauf-Stepper auf den Detailseiten ---
  const schrittButtons = document.querySelectorAll(".schritt-button");

  schrittButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const schritt = btn.closest(".schritt");
      const istOffen = schritt.classList.contains("offen");
      btn.setAttribute("aria-expanded", String(!istOffen));
      schritt.classList.toggle("offen");
    });
  });

  // Ersten Schritt beim Laden der Detailseite standardmäßig aufklappen
  const ersterSchritt = document.querySelector(".stepper .schritt");
  if (ersterSchritt) {
    ersterSchritt.classList.add("offen");
    ersterSchritt.querySelector(".schritt-button").setAttribute("aria-expanded", "true");
  }

  // --- Leseleiste: Scroll-Fortschritt der aktuellen Seite im Header ---
  const header = document.querySelector("header.site-header");
  if (header) {
    const leseleiste = document.createElement("div");
    leseleiste.className = "leseleiste";
    const fill = document.createElement("div");
    fill.className = "leseleiste-fill";
    leseleiste.appendChild(fill);
    header.appendChild(leseleiste);

    const updateLeseleiste = () => {
      const hoehe = document.documentElement.scrollHeight - window.innerHeight;
      const prozent = hoehe > 0 ? (window.scrollY / hoehe) * 100 : 0;
      fill.style.width = Math.min(100, Math.max(0, prozent)) + "%";
    };
    updateLeseleiste();
    window.addEventListener("scroll", updateLeseleiste, { passive: true });
    window.addEventListener("resize", updateLeseleiste);
  }

  // --- Abschnitte beim Einscrollen sanft einblenden ---
  const abschnitte = document.querySelectorAll(".projekt-detail > section");
  if (abschnitte.length && "IntersectionObserver" in window) {
    abschnitte.forEach((a) => a.classList.add("reveal"));
    const beobachter = new IntersectionObserver(
      (eintraege) => {
        eintraege.forEach((eintrag) => {
          if (eintrag.isIntersecting) {
            eintrag.target.classList.add("sichtbar");
            beobachter.unobserve(eintrag.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.05 }
    );
    abschnitte.forEach((a) => beobachter.observe(a));
  }

  // --- Schwebende Vor/Zurück-Buttons aus der vorhandenen Projekt-Navigation erzeugen ---
  const projektNav = document.querySelector(".projekt-nav");
  if (projektNav) {
    const links = projektNav.querySelectorAll("a");
    const zurueckLink = links[0];
    const weiterLink = projektNav.querySelector(".naechste") || links[1];

    const schwebeNav = document.createElement("div");
    schwebeNav.className = "floating-nav";

    const macheButton = (link, symbol, label) => {
      const a = document.createElement("a");
      if (link) {
        a.href = link.href;
        a.title = label + ": " + link.textContent.replace(/\s+/g, " ").trim();
      } else {
        a.classList.add("deaktiviert");
        a.href = "#";
      }
      a.innerHTML = symbol;
      a.setAttribute("aria-label", label);
      return a;
    };

    schwebeNav.appendChild(macheButton(zurueckLink, "&larr;", "Vorherige Seite"));
    schwebeNav.appendChild(macheButton(weiterLink, "&rarr;", "Nächste Seite"));
    document.body.appendChild(schwebeNav);

    // --- Pfeiltasten-Navigation zwischen den Seiten ---
    document.addEventListener("keydown", (e) => {
      const zielTag = (e.target.tagName || "").toLowerCase();
      if (zielTag === "input" || zielTag === "textarea" || e.metaKey || e.ctrlKey || e.altKey) return;
      if (e.key === "ArrowRight" && weiterLink) window.location.href = weiterLink.href;
      if (e.key === "ArrowLeft" && zurueckLink) window.location.href = zurueckLink.href;
    });
  }

  // --- "Alle Seiten"-Menü schließen, wenn ein Link angeklickt wird ---
  const seitenMenu = document.querySelector(".seiten-menu");
  if (seitenMenu) {
    seitenMenu.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", () => seitenMenu.removeAttribute("open"));
    });
    document.addEventListener("click", (e) => {
      if (seitenMenu.hasAttribute("open") && !seitenMenu.contains(e.target)) {
        seitenMenu.removeAttribute("open");
      }
    });
  }

});
