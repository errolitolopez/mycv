// Paper size for the one page CV: A4 or short bond (US Letter). It sets the preview width and the PDF link.

const SIZES = {
  a4: { width: "210mm" },
  letter: { width: "8.5in" },
};
const STORAGE_KEY = "mycv-paper-size";

// Remembers the choice; storage can be blocked (private window), so failing is fine.
const readSaved = () => {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved in SIZES ? saved : "a4";
  } catch (error) {
    return "a4";
  }
};

const save = (size) => {
  try {
    localStorage.setItem(STORAGE_KEY, size);
  } catch (error) {
    // Not remembered; the page still works.
  }
};

// applySize("letter") -> the PDF link asks for Letter, the preview sheet is 8.5in wide, that button is active.
const applySize = (size) => {
  const { width } = SIZES[size];
  // Each size button carries its PDF address (data-pdf), so this works under any site prefix.
  document.getElementById("download-pdf").href = document.querySelector(`[data-size="${size}"]`).dataset.pdf;
  document.getElementById("sheet").style.maxWidth = width;
  document.querySelectorAll("[data-size]").forEach((button) => {
    const active = button.dataset.size === size;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  save(size);
};

document.querySelectorAll("[data-size]").forEach((button) => {
  button.addEventListener("click", () => applySize(button.dataset.size));
});
applySize(readSaved());
