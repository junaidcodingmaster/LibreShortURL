function setDarkTheme(enabled) {
  document.cookie = "darktheme=" + enabled + "; path=/";
  document.body.className = enabled ? "dark-theme" : "light-theme";

  const btn = document.getElementById("theme-bnt");
  if (btn) {
    btn.textContent = enabled ? "Switch to Light Mode" : "Switch to Dark Mode";
  }
}

function getDarkTheme() {
  return document.cookie.includes("darktheme=true");
}

function toggleTheme() {
  const isDark = getDarkTheme();
  setDarkTheme(!isDark);
}

window.onload = function () {
  const isDark = getDarkTheme();
  setDarkTheme(isDark);

  const btn = document.getElementById("theme-bnt");
  if (btn) {
    btn.onclick = toggleTheme;
  }
};

async function handleSubmit(event) {
  event.preventDefault();
  const url = document.getElementById("url").value.trim();
  const name = document.getElementById("name").value.trim();
  const notification = document.getElementById("notification");

  const body = { url };
  if (name.length > 0) {
    body.name = name;
  }

  try {
    const response = await fetch("/api/gen-url", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await response.json();
    notification.style.display = "block";
    if (response.ok) {
      notification.style.border = "2px solid green";
      notification.innerHTML = `<strong>${data.message}</strong><br><a href="${data.url}" target="_blank">${data.url}</a>`;
    } else {
      notification.style.border = "2px solid red";
      notification.textContent = data.message || "Error shortening URL.";
    }
  } catch (error) {
    notification.style.display = "block";
    notification.style.border = "2px solid red";
    notification.textContent = "Error connecting to server.";
  }
}

async function checkNameAvailability() {
  const name = document.getElementById("name").value.trim();
  const availabilityDiv = document.getElementById("availability");

  if (!name) {
    availabilityDiv.textContent = "";
    return;
  }

  try {
    const response = await fetch("/api/check-name-availability", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    const data = await response.json();
    if (data.message.includes("Available")) {
      availabilityDiv.className = "availability available";
    } else {
      availabilityDiv.className = "availability unavailable";
    }
    availabilityDiv.textContent = data.message;
  } catch {
    availabilityDiv.className = "availability unavailable";
    availabilityDiv.textContent = "Error checking availability.";
  }
}