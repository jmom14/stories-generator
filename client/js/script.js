const wordInput = document.getElementById('wordInput');
const createStoryForm = document.getElementById('createStoryForm');
const wordsContainer = document.getElementById('wordsContainer');
const loader = document.getElementById('loader');
const submitStory = document.getElementById('submitStory');

let words = [];

function addLoader() {
    submitStory.innerHTML = '';
    const loaderDiv = document.createElement('div');
    loaderDiv.className = 'loader';
    loaderDiv.id = 'loader';
    submitStory.appendChild(loaderDiv);

}

function removeLoader() {
    submitStory.innerHTML = 'Submit';
    const loader = document.getElementById('loader');
    if (loader) {
        loader.remove();
    }
}

createStoryForm.addEventListener('submit', (e) => {
    addLoader();
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    let fileName = '';
    const params = {
        "language": data.language,
        "words": words,
        "format": data.format,
    }
    fetch('http://localhost:8000/stories/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    }).then((response) => {
        const xFileName = response.headers.get('X-File-Name');
        fileName = xFileName
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.blob();
    }).then(data => {
        words = [];
        renderWords();
        const url = window.URL.createObjectURL(data);
        const anchor = document.createElement('a');
        anchor.style = 'display: none';
        anchor.href = url;
        anchor.download = fileName;
        document.body.appendChild(anchor);
        anchor.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(anchor);
    }).catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    }).finally(() => {
        removeLoader();
    });
});

wordInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        addWord();
    }
});

function addWord() {
    const word = wordInput.value;
    if (word) {
        words.push(word);
        renderWords();
        wordInput.value = '';
    }
}

function renderWords() {
    wordsContainer.innerHTML = '';
    words.forEach(word => {
        const wordElement = document.createElement('span');
        wordElement.className = 'badge badge-pill badge-info';
        wordElement.innerHTML = word;
        wordsContainer.appendChild(wordElement);
    });
}