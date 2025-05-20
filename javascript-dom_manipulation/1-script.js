// Select the element with id 'red_header'
const redHeader = document.querySelector('#red_header');

// Select the header element
const header = document.querySelector('header');

// Add a click event listener to red_header
redHeader.addEventListener('click', () => {
    // Set header's text color to red
    header.style.color = 'red';
});