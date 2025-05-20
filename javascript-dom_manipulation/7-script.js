// Select the ul with id 'list_movies'
const listMovies = document.querySelector('#list_movies');

// Fetch data from the URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json)
    .then(data => {
        // Loop through data.results
        // Create an li for each movie title
        // Append each li to listMovies
        data.results.forEach(movie => {
            const movieTitle = document.createElement('li');
            movieTitle.textContent = movie.title;
            listMovies.appendChild(movieTitle);
        });
    });