// Home page: highlight the nav link of the section in view, and fade sections in as they scroll into view.

const setupScrollSpy = () => {
  // Bootstrap's ScrollSpy marks the nav link of the section in view as active.
  new bootstrap.ScrollSpy(document.body, { target: "#topnav", rootMargin: "-35% 0px -60% 0px" });
};

const setupReveal = () => {
  const items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    items.forEach((item) => item.classList.add("in"));
    return;
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("in");
      observer.unobserve(entry.target); // reveal once, not every time it scrolls past
    });
  }, { threshold: 0.12 });
  items.forEach((item) => observer.observe(item));
};

setupScrollSpy();
setupReveal();
