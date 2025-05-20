// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
    // Select the element with id 'hello'
    const helloDiv = document.querySelector('#hello');
    // Fetch data from the URL
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            // Update helloDiv with the 'hello' value
            helloDiv.textContent = data.hello;
        });
});