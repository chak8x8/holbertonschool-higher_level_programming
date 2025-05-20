// Select the element with id 'character'
const characterDiv = document.querySelector('#character');

// Fetch data from the URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json)
    .then(data => {
        // Update characterDiv with the 'name' from data
        characterDiv.textContent = data.name;
    })