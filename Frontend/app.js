function load() {
  fetch("/api/messages")
    .then(res => res.json())
    .then(data => {
      document.getElementById("list").innerHTML =
        data.map(m => `<li>${m.text}</li>`).join("");
    });
}
