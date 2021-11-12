const flagsElement = document.getElementById("flags");

const changeLanguage = async language => {
    const requestJson = await fetch(`./languages/${language}.json`)
    const text = await requestJson.json()
}

flagsElement.addEventListener("click", (e) => {
    changeLanguage(e.target.parentElement.dataset.language);
});