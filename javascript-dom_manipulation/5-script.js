// Select the element with id 'update_header'
const updateHeader = document.querySelector('#update_header');

// Select the header element
const header = document.querySelector('header');

// Add a click event listener to update_header
updateHeader.addEventListener('click', () => {

    // Update header text to 'New Header!!!'
    header.textContent = 'New Header!!!';
});