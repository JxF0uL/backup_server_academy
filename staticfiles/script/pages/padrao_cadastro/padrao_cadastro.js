document.addEventListener('DOMContentLoaded', (event) => {
    const inputs = document.querySelectorAll('.inputs input');
    const button = document.getElementById('login-button');

    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            button.style.backgroundColor = '#57E0FF'; 
        });

        input.addEventListener('blur', () => {
            button.style.backgroundColor = '#cccccc'; 
        });
    });
});
