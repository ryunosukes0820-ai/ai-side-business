// FAQアコーディオン(JS無効時はmax-heightが適用されず全文表示される)
const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach((item) => {
  const question = item.querySelector(".faq-question");
  const answer = item.querySelector(".faq-answer");
  if (!question || !answer) return;

  const isInitiallyOpen = question.getAttribute("aria-expanded") === "true";
  answer.style.maxHeight = isInitiallyOpen ? answer.scrollHeight + "px" : "0px";

  question.addEventListener("click", () => {
    const isOpen = question.getAttribute("aria-expanded") === "true";
    question.setAttribute("aria-expanded", String(!isOpen));
    answer.style.maxHeight = isOpen ? "0px" : answer.scrollHeight + "px";
  });
});

// 軽いスクロール表示アニメーション
const revealTargets = document.querySelectorAll(".reveal");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (prefersReducedMotion || !("IntersectionObserver" in window)) {
  revealTargets.forEach((target) => target.classList.add("is-visible"));
} else {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealTargets.forEach((target) => observer.observe(target));
}
