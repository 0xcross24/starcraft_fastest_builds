document.addEventListener('DOMContentLoaded', function () {
// Function to add hover effect to card and image
  function addHoverEffect(card) {
    const image = card.querySelector('.hover-image');
    const hoverImageSrc = "static/" + card.getAttribute('data-hover-image');
    const defaultImageSrc = "static/" + card.getAttribute('data-default-image');

    card.addEventListener('mouseover', function () {
      image.src = hoverImageSrc;
      console.log("hovering");
    });

    card.addEventListener('mouseout', function () {
      image.src = defaultImageSrc;
    });
  }

  // Apply hover effect to all cards with the 'hover-card' class
  const cards = document.querySelectorAll('.hover-card');
  cards.forEach(addHoverEffect);
});