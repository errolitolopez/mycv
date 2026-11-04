// Light/dark theme. Runs in <head> so the right theme is set before the page paints (no flash).
(() => {
  const KEY = "mycv-theme";
  const root = document.documentElement;
  root.classList.add("js", "preload"); // "js" lets CSS hide things until they scroll in; "preload" stops first-load animation

  // Saved choice, else the system preference. Storage can be blocked, so reading is wrapped.
  const initial = () => {
    try {
      const saved = localStorage.getItem(KEY);
      if (saved === "light" || saved === "dark") return saved;
    } catch (error) {
      // Fall through to the system preference.
    }
    return matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  };

  // setTheme("light") -> <html data-bs-theme="light">; remembered for next visit
  const setTheme = (theme) => {
    root.setAttribute("data-bs-theme", theme);
    try {
      localStorage.setItem(KEY, theme);
    } catch (error) {
      // Not remembered; the page still works.
    }
  };

  root.setAttribute("data-bs-theme", initial());

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.addEventListener("click", () => {
        setTheme(root.getAttribute("data-bs-theme") === "dark" ? "light" : "dark");
      });
    });
    // Two frames later the first paint is done, so transitions can switch on.
    requestAnimationFrame(() => requestAnimationFrame(() => root.classList.remove("preload")));
  });
})();
