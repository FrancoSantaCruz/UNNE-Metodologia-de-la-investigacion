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

document.addEventListener("DOMContentLoaded", function() {
    const modals = document.querySelectorAll(".modal");
    const modalCards = document.querySelectorAll(".modal-card");
    const closeButtons = document.querySelectorAll(".close");

    // Abrir modal
    modalCards.forEach(card => {
        card.addEventListener("click", function() {
            const modalId = this.getAttribute("data-modal");
            document.getElementById(modalId).style.display = "flex";
        });
    });

    // Cerrar modal
    closeButtons.forEach(button => {
        button.addEventListener("click", function() {
            this.closest(".modal").style.display = "none";
        });
    });

    // Cerrar modal al hacer clic fuera del contenido
    window.addEventListener("click", function(event) {
        modals.forEach(modal => {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const headers = document.querySelectorAll(".accordion-header");

    headers.forEach(header => {
        header.addEventListener("click", function() {
            const contentId = header.getAttribute("data-target");
            const content = document.getElementById(contentId);
            const item = header.parentElement;

            // Alterna la clase activa en el elemento actual
            item.classList.toggle("active");

            // Cierra el resto de los acordeones
            document.querySelectorAll(".accordion-item").forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove("active");
                }
            });
        });
    });
});