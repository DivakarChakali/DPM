// Toggle the mobile menu on and off
document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.navbar-toggle');
    const menuLinks = document.querySelector('.navbar-links');

    menuToggle.addEventListener('click', function () {
        menuLinks.classList.toggle('active');
    });
});