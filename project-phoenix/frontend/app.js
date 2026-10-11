const statusElement = document.querySelector("#service-status");

fetch("/api/health")
  .then((response) => response.json())
  .then((data) => {
    statusElement.textContent = data.status === "ok" ? "Service is ready." : "Service is unavailable.";
  })
  .catch(() => {
    statusElement.textContent = "Service is unavailable.";
  });
