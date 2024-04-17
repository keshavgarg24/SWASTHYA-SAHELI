

$(document).ready(function(){
    $('.feedback-slider').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        items: 1,
        autoplay: true,
        navText: ["<i class = 'fas fa-arrow-left'></i>", "<i class = 'fas fa-arrow-right'></i>"]
    });

    // stop animation on resize
    let resizeTimer;
    $(window).resize(function(){
        $(document.body).addClass('resize-animation-stopper');
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            $(document.body).removeClass('resize-animation-stopper');
        }, 400);
    });

    $('.navbar-show-btn').click(function(){
        $('.navbar-box').addClass('navbar-box-show');
    });

    $('.navbar-hide-btn').click(function(){
        $('.navbar-box').removeClass("navbar-box-show");
    })
});

const therapeuticTexts = [
    "You are capable of amazing things.",
    "Your strength is greater than any challenge.",
    "You are enough just as you are.",
    "Remember to take care of yourself. You deserve it.",
    "Your dreams are within reach. Keep striving.",
    "You are a beautiful soul, inside and out.",
    "Believe in yourself, and anything is possible.",
    "Your presence makes a difference in the world.",
    "You are worthy of love and respect.",
    "Trust yourself. You know more than you think.",
    "Embrace your uniqueness. It's what makes you special.",
    "Take one step at a time. Progress is progress, no matter how small.",
    "You have the power to create the life you want.",
    "Challenges are opportunities for growth. You've got this.",
    "Your inner strength is a force to be reckoned with.",
    "You are not alone. Reach out for support when you need it.",
    "You radiate positivity and kindness.",
    "Your potential is limitless.",
    "You are a beacon of light in the lives of those around you.",
    "Every obstacle you overcome makes you stronger.",
    "Your resilience knows no bounds.",
    "You are worthy of all the good things life has to offer.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Your journey is unique and beautiful.",
    "You are loved, cherished, and valued.",
  ];
  
  function generateText() {
    const randomIndex = Math.floor(Math.random() * therapeuticTexts.length);
    const text = therapeuticTexts[randomIndex];
    document.getElementById("therapeutic-text").innerText = text;
  }
  