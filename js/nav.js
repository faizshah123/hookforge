(function () {
  const path = location.pathname.replace(/index\.html$/, "").replace(/\/+$/, "") || "/";
  document.querySelectorAll(".nav a").forEach((a) => {
    const href = a.getAttribute("href").replace(/index\.html$/, "").replace(/\/+$/, "") || "/";
    if (href === path || (href !== "/" && path.startsWith(href))) a.setAttribute("aria-current", "page");
  });
  const y = document.getElementById("y");
  if (y) y.textContent = String(new Date().getFullYear());
})();
