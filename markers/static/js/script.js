  
  // scroll para as seções
  let navBtn = $('.nav-link');

  let homeSection = $('#home-area');
  let teamSection = $('#team-area');
  let contactSection = $('#contact-area');


  let scrollTo = '';

  $(navBtn).click(function() {

    let btnId = $(this).attr('id');

    console.log(btnId);

    if(btnId == 'team-menu') {
      scrollTo = teamSection;
    } else if(btnId == 'about-menu') {
      scrollTo = aboutSectopm;
    } else if(btnId == 'contact-menu') {
      scrollTo = contactSection;
    } else {
      scrollTo = homeSection;
    }

    $([document.documentElement, document.body]).animate({
        scrollTop: $(scrollTo).offset().top - 180
    }, 200);
  });
