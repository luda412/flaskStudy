document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("hello-btn");

  if (btn) {
    btn.addEventListener("click", () => {
      alert("Hello from JavaScript!");
    });
  }
});
