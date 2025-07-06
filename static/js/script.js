$(document).ready(function() {

  var currentIndex = 0;
  var images = $('.carousel img');
  var imageCount = images.length;

  $('.carousel-next').click(function() {
    currentIndex++;
    if (currentIndex >= imageCount) {
      currentIndex = 0;
    }
    updateCarousel();
  });

  $('.carousel-prev').click(function() {
    currentIndex--;
    if (currentIndex < 0) {
      currentIndex = imageCount - 1;
    }
    updateCarousel();
  });

  function updateCarousel() {
    images.hide();
    images.eq(currentIndex).show();
  }


  // updateCarousel();
  setInterval(() => {currentIndex++;
    if (currentIndex >= imageCount) {
      currentIndex = 0;
    }
    updateCarousel();}, 2500)



});

