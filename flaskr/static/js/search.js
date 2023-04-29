const search_menu = document.querySelector('#search_menu');
const search_button = document.querySelector('#search_button');

search_button.addEventListener('click', () => {
    console.log(search_menu.value);
    window.location.href = '/search_order/' + search_menu.value;
});

