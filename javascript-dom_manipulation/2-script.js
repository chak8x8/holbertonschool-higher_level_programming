// Select the element with id 'red_header'
const redHeader = document.querySelector('#red_header');

// Select the header element
const header = document.querySelector('header');

// Add a click event listener to red_header
redHeader.addEventListener('click', () => {
    // Add the 'red' class to header
    header.classList.add('red');
});