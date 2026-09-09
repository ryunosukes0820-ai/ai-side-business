(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ============================
     FAQ accordion
  ============================ */
  var faqQuestions = document.querySelectorAll(".faq-question");

  faqQuestions.forEach(function (button) {
    var answer = document.getElementById(button.getAttribute("aria-controls"));
    if (!answer) return;

    var isOpen = button.getAttribute("aria-expanded") === "true";
    answer.style.maxHeight = isOpen ? answer.scrollHeight + "px" : "0px";

    button.addEventListener("click", function () {
      var expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
      answer.style.maxHeight = expanded ? "0px" : answer.scrollHeight + "px";
    });
  });

  window.addEventListener("resize", function () {
    faqQuestions.forEach(function (button) {
      var answer = document.getElementById(button.getAttribute("aria-controls"));
      if (!answer) return;
      if (button.getAttribute("aria-expanded") === "true") {
        answer.style.maxHeight = answer.scrollHeight + "px";
      }
    });
  });

  /* ============================
     Scroll reveal
  ============================ */
  var revealTargets = document.querySelectorAll(".reveal");

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealTargets.forEach(function (el) {
      el.classList.add("is-visible");
    });
  } else {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );

    revealTargets.forEach(function (el) {
      observer.observe(el);
    });
  }
})();
