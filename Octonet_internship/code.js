// script.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
        const email = document.querySelector('#email').value;
        if (!email) {
            alert('Please enter a valid email address.');
            event.preventDefault();
        }
    });
});
