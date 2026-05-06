document.addEventListener("DOMContentLoaded", () => {
  // --- Index page button ---
  const btn = document.getElementById("btn");
  if (btn) {
    btn.onclick = async () => {
      const res = await fetch("/api/hello");
      const data = await res.json();
      document.getElementById("output").textContent = data.message;
    };
  }

  // --- Form page ---
  const form = document.getElementById("nameForm");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const name = document.getElementById("nameInput").value;

      const res = await fetch("/api/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({ name })
      });

      const data = await res.json();
      document.getElementById("result").textContent = data.message;
    });
  }
});
