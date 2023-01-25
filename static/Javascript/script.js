// Function to have the navSlide set up on burger click
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {

        // Toggle Nav
        nav.classList.toggle('nav-active');

        // Animate Links
        navLinks.forEach((link, index) => {
            const newLocal = 'navLinkFade 0.5s ease forwards ${index / 7}s';
            link.style.animation = newLocal;
        });
    });
}


// Function to call all functions
const app = () => {
    // Update as more functions are added
    navSlide();
}

// Run function to run all others
app();