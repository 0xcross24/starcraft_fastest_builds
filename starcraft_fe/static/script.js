document.addEventListener('DOMContentLoaded', function () {
  // Function to add hover effect to card and image
  function addHoverEffect(card) {
    const image = card.querySelector('.hover-image');
    const hoverImageSrc = "static/" + card.getAttribute('data-hover-image');
    const defaultImageSrc = "static/" + card.getAttribute('data-default-image');

    card.addEventListener('mouseover', function () {
      image.src = hoverImageSrc;
    });

    card.addEventListener('mouseout', function () {
      image.src = defaultImageSrc;
    });
  }

  // Apply hover effect to all cards with the 'hover-card' class
  const cards = document.querySelectorAll('.hover-card');
  cards.forEach(addHoverEffect);
});

$(window).on('load', function() {
  $(".hidden").each(function() {
    if ($(this).hasClass('post-container')) {
      $(this).fadeIn(500).css('display', 'block');
    } else {
      $(this).fadeIn(500).css('display', '-webkit-box');
    }
  });
});

$(document).ready(function() {
  // Select the audio elements
  var audio_enter = $("#enter")[0];
  var audio_click = $("#click")[0];
  var audio_swishout = $("#swishout")[0];
  var audio_swishin = $("#swishin")[0];
  
  // Add event listener for mouse enter
  $(".hovering-items").mouseenter(function() {
    // Reset and play the audio
    audio_enter.currentTime = 0; // Reset playback position
    audio_enter.volume = 0.5; // Set volume to 50%
    audio_enter.play();
  });
  
  // Add event listener for mouse leave
  $(".hovering-items").mouseleave(function() {
    // Optionally pause the audio when the mouse leaves
    audio_enter.pause();
    // Optionally reset playback position when mouse leaves (if you want to restart from beginning next time)
    audio_enter.currentTime = 0;
  });

  $(".hovering-items").on('click', function(event) {
    event.preventDefault();
    audio_click.currentTime = 0; // Reset playback position
    audio_click.play().catch(function(error) {
      console.error('Playback error:', error);
    });

    var targetUrl = $(this).attr('href');
  });

  $(".clicked").on('click', function(event) {
    // Prevent the default action to ensure the fade-out occurs first
    event.preventDefault();

    // Ensure that the click event triggers the audio
    audio_click.currentTime = 0; // Reset playback position
    audio_click.play().catch(function(error) {
      console.error('Playback error:', error);
    });

    // Get clicked on URL
    var targetUrl = $(this).attr('href');
    audio_swishin.volume = 0.2; // Set volume to 50%

    audio_swishin.play()
    $(".hidden").fadeOut(500, function() {
      window.location.href = targetUrl;
    });

        // Check if the element with class 'hidden' is not present
  if ($(".hidden").length) {
    // Play the audio effect
    audio_swishin.play()

    $(".hidden").fadeOut(500, function() {
        window.location.href = targetUrl;
    });

  } else {
    setTimeout(function() {
        window.location.href = targetUrl;
      }, 500); // Adjust the delay time (in milliseconds) as needed
    }
  });
  
  $(".back").on('click', function(event) {
    // Prevent the default action to ensure the fade-out occurs first
    event.preventDefault();

    // Ensure that the click event triggers the audio
    audio_click.currentTime = 0; // Reset playback position
    audio_click.play().catch(function(error) {
      console.error('Playback error:', error);
    });

    audio_swishin.volume = 0.2; // Set volume to 50%

    audio_swishin.play()
    $(".hidden").fadeOut(500, function() {
      history.back();
    });
  });
});
