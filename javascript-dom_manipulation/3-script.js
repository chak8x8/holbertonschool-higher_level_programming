// Select the element with id 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Select the header element
const header = document.querySelector('header');

// Add a click event listener to toggle_header
toggleHeader.addEventListener('click', () => {

    // Check if header has 'red' class
    if (header.classList.contains('red')) {
        // Remove red, add green
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        // Remove green, add red
        header.classList.remove('green');
        header.classList.add('red');
    }
});
