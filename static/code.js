const form = document.getElementById("form");
const textEl = document.getElementById("text");
const ipaEl = document.getElementById("ipa");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    fetch(`/api/ipa?text=${text.value}`).then(async (res) => {
        const body = await res.json();
        ipaEl.innerHTML = body.ipa;
    });
});