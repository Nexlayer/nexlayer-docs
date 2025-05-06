document.addEventListener("DOMContentLoaded", function () {
    const iconMap = {
        "Docs": `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
             width="1em" height="1em" class="nav-icon">
          <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
        </svg>`,
        "API & SDK": `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
             width="1em" height="1em" class="nav-icon">
  <path d="M12.89,3L14.85,3.4L11.11,21L9.15,20.6L12.89,3M19.59,12L16,8.41V5.58L22.42,12L16,18.41V15.58L19.59,12M1.58,12L8,5.58V8.41L4.41,12L8,15.58V18.41L1.58,12Z" />
        </svg>`,
        "CLI": `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d="M9.4 86.6C-3.1 74.1-3.1 53.9 9.4 41.4s32.8-12.5 45.3 0l192 192c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L178.7 256 9.4 86.6zM256 416l288 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-288 0c-17.7 0-32-14.3-32-32s14.3-32 32-32z"/></svg>`

    };

    const tabs = document.querySelectorAll(".md-tabs__link");

    tabs.forEach(tab => {
        const label = tab.textContent.trim();
        if (iconMap[label]) {
            tab.innerHTML = `<span class="nav-combo">${iconMap[label]}${label}</span>`;
        }
    });
});
