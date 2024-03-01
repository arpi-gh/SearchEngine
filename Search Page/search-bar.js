document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('search-form');
    const input = document.querySelector('.search-bar input[type="text"]');

    input.value = '';

    const savedSearchTerm = localStorage.getItem('searchTerm');
    if (savedSearchTerm) {
        input.value = savedSearchTerm;
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const searchTerm = input.value;
        localStorage.setItem('searchTerm', searchTerm);

        window.location.href = 'search_results.html?search=' + encodeURIComponent(searchTerm);
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.querySelector('.hamburger-menu');
    const menuContent = document.querySelector('.menu-content');

    menuButton.addEventListener('click', function() {
        // Toggle the display of the menu content
        if (menuContent.style.display === 'block') {
            menuContent.style.display = 'none';
        } else {
            menuContent.style.display = 'block';
        }
    });
});
