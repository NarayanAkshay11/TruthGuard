document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.burger');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    burger.addEventListener('click', function() {
        dropdownMenu.classList.toggle('show-dropdown');
    });

    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            target.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Form submission
    const form = document.querySelector('form');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        // Add your form submission logic here
        alert('Form submitted successfully!');
        form.reset();
    });
});
