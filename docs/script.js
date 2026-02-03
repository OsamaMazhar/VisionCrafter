// VisionCrafter starter JS
console.log('VisionCrafter webpage loaded.');

document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        root: null, // use the viewport
        rootMargin: '0px',
        threshold: 0.2 // trigger when 20% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once visible if you don't want it to fade out again
                observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);

    const scrollFeatures = document.querySelectorAll('.scroll-feature');
    scrollFeatures.forEach(el => observer.observe(el));
});
