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
            if(link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = 'navLinkFade 1.5s ease 0.3s 1 normal forwards';
            }
        });

        // Burger Animation
        burger.classList.toggle('tBurg');
    });
}


// Function to call all functions
const app = () => {
    // Update as more functions are added
    navSlide();
}

// Run function to run all others
app();