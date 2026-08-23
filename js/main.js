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

});
