$(document).ready(function() {

	$(window).resize(function() {
        if ($(window).width() < 767) {
        	$('.programming-blocks-wrapper').owlCarousel({
				items: 1,
				margin:0,
				autoHeight: true,
				loop: true
			});
        }
        else {
            $('.programming-blocks-wrapper').owlCarousel('destroy');
        }
    }).trigger('resize');

    $('.projects').owlCarousel({
		items: 5,
		loop:true,
		margin:0,
		responsive:{
		    1400:{
		        items: 5
		    },
		    992:{
		        items: 4
		    },
		    768:{
            items: 3,
            nav: false
		    },
		    0:{
            items: 3,
		        center: true,
		        margin: -20,
		        autoWidth: true
		    }
		}
	});

    // show more
    $(".js-more").click(function(e){

    	var
			$target = $(e.currentTarget),
    		$targetBlock  =$target.closest('.js-section-text').find('.hide')
		;
    	if($targetBlock.is(':visible')){
            $targetBlock.hide();
            $target.html("Read More");

		}else{
            $targetBlock.show();
            $target.html("Hide");
		}

    });


    // window btn
    $('.js-btn-window').on('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var $target = $(e.currentTarget);
        if ($target.hasClass('active')) {
            $target.removeClass('active');
            $($target.attr('href')).removeClass('active');
        } else {
            $target.closest('.js-window').find('js-btn-window').removeClass('active');
            $target.addClass('active');
            $('.js-window.active').removeClass('active');
            $($target.attr('href')).addClass('active');
        }
    })

    $(document).click(function (event) {
		if ($(event.target).closest(".js-window").length) return;
		$('.js-window.active').removeClass("active");
		$('.js-btn-window.active').removeClass("active");
		$('body').removeClass("window-active");
		event.stopPropagation();
	});
	$(".js-window-close, .js-btn-window.active, .link-anchor").click(function (event) {
		$('.js-window.active').removeClass("active");
		$('.js-btn-window.active').removeClass("active");
		$('body').removeClass("is-menu-active");
	});


  // fixed header
    $(window).resize(function() {
        if ($(window).width() >= 0) {
          var $menu = $(".header");
          $(window).scroll(function(){
              if ( $(this).scrollTop() > 37 && $menu.hasClass("default") ){
                  $menu.fadeIn(0,function(){
                      $(this).removeClass("default")
                             .addClass("fixed");
                  });
              } else if($(this).scrollTop() <= 37 && $menu.hasClass("fixed")) {
                  $menu.fadeIn(0,function(){
                      $(this).removeClass("fixed")
                             .addClass("default");
                  });
              }
          });
        }
    }).trigger('resize');

  // slow anchors
  $(function(){
     $('.link-anchor').click(function(){
          var target = $(this).attr('href');
    if (jQuery(window).width() >= 992) {
      var margintop = 67;
    }else{
      var margintop = 64;
    }
          $('html, body').animate({scrollTop: $(target).offset().top - margintop}, 1000);
          return false;
     });
  });


  $(function() {
    $('.css-about-items .owl-item').matchHeight();
  });


});

$(document).ready(function() {

  var sync1 = $(".js-about-items");
  var sync2 = $(".js-about-bg");
  var slidesPerPage = 1; //globaly define number of elements per page
  var syncedSecondary = true;

  sync1.owlCarousel({
    items : 1,
    loop: true,
    dots: false,
	  responsive:{

	    550:{
        margin: -200,
        nav: true,
        navText: ['',''],
	    },
	    0:{
	    	margin: -90
	    }
    },
    autoheight: true,
    onRefreshed: function () {
      $(window).resize();
    }
  }).on('changed.owl.carousel', syncPosition);

  sync2
    .on('initialized.owl.carousel', function () {
      sync2.find(".owl-item").eq(0).addClass("current");
    })
    .owlCarousel({
    	dots: false,
	    items : slidesPerPage,
	    slideBy: slidesPerPage, //alternatively you can slide by 1, this way the active slide will stick to the first item in the second carousel
	    responsiveRefreshRate : 100
	}).on('changed.owl.carousel', syncPosition2);

  
  function syncPosition(el) {
    //if you set loop to false, you have to restore this next line
    //var current = el.item.index;
    
    //if you disable loop you have to comment this block
    var count = el.item.count-1;
    var current = Math.round(el.item.index - (el.item.count/2) - .5);
    
    if(current < 0) {
      current = count;
    }
    if(current > count) {
      current = 0;
    }
    
    //end block

    sync2
      .find(".owl-item")
      .removeClass("current")
      .eq(current)
      .addClass("current");
    var onscreen = sync2.find('.owl-item.active').length - 1;
    var start = sync2.find('.owl-item.active').first().index();
    var end = sync2.find('.owl-item.active').last().index();
    
    if (current > end) {
      sync2.data('owl.carousel').to(current, 100, true);
    }
    if (current < start) {
      sync2.data('owl.carousel').to(current - onscreen, 100, true);
    }
  }
  
  function syncPosition2(el) {
    if(syncedSecondary) {
      var number = el.item.index;
      sync1.data('owl.carousel').to(number, 100, true);
    }
  }
  
  sync2.on("click", ".owl-item", function(e){
    e.preventDefault();
    var number = $(this).index();
    sync1.data('owl.carousel').to(number, 300, true);
  });

  $('.readmore').on('click', function(){
    $(this).parent().find($('.readmore~p')).slideDown();
    $(this).parent().find($('.showless')).slideDown();
    $(this).slideUp();
  })
  $('.showless').on('click', function(){
    $(this).parent().find($('.readmore~p')).slideUp();
    $(this).slideUp();
    $(this).parent().find($('.readmore')).slideDown();
  })

  $('.project_video #single_title_video').on('click', function(){
    $('.project_video #single_title_video').parent().find('.play_img').fadeToggle(100);
  })
  $('.project_video .play_img').on('click', function(){
    $('.project_video #single_title_video').get(0).play();
    $(this).hide();
  })

  $('.menu.js-window li:nth-child(2)').on('click', function(){
    $(this).find('ul').slideToggle(400);
  })

  var bLazy = new Blazy({
    // Options
  });
  
  $('[data-fancybox="gallery-video"]').fancybox({
    // Options will go here
  });

  $('[data-fancybox="gallery-image"]').fancybox({
    // Options will go here
  });

  var t = document.querySelector("#menu");
    new MenuSpy(t)
});