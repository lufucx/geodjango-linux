// Scroll para as seções
let navBtn = $('.nav-link');

let homeSection = $('#home-area');
let teamSection = $('#team-area');
let aboutSection = $('#about-area'); // Assuming there's an element with this ID
let contactSection = $('#contact-area');

let scrollTo = '';

$(navBtn).click(function() {
    let btnId = $(this).attr('id');

    console.log(btnId);

    if (btnId === 'team-menu') {
        scrollTo = teamSection;
    } else if (btnId === 'about-menu') {
        scrollTo = aboutSection; // Fixed typo from aboutSectopm
    } else if (btnId === 'contact-menu') {
        scrollTo = contactSection;
    } else {
        scrollTo = homeSection;
    }

    // Check if scrollTo is defined
    if (scrollTo.length) {
        $([document.documentElement, document.body]).animate({
            scrollTop: $(scrollTo).offset().top - 180
        }, 800); // Adjust duration for desired speed
    }
});
