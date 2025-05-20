// Select the element with id 'add_item'
const add_item = document.querySelector('#add_item');

// Select the ul with class 'my_list'
const my_list = document.querySelector('.my_list');

// Add a click event listener to add_item
add_item.addEventListener('click', () => {
    // Create a new li element
    const new_li = document.createElement('li');

    // Set its text to 'Item'
    new_li.textContent = 'Item';

    // Append it to my_list
    my_list.appendChild(new_li);
})