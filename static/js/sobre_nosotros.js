document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector('.theory-nav');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 100) {
            navbar.classList.add('small');
        } else {
            navbar.classList.remove('small');
        }
    });
});

window.addEventListener('beforeunload', function () {
    localStorage.setItem('scrollPosition', window.scrollY);
});


window.addEventListener('load', function () {
    const scrollPosition = localStorage.getItem('scrollPosition');
    if (scrollPosition) {
        window.scrollTo(0, parseInt(scrollPosition, 10));
        localStorage.removeItem('scrollPosition');
    }
});
