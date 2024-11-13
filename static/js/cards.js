function flipCard() {
    document.querySelector('.card').classList.toggle('flipped');
}

document.addEventListener("DOMContentLoaded", function() {
    const navbar = document.querySelector('.theory-nav');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('small');
        } else {
            navbar.classList.remove('small');
        }
    });
});