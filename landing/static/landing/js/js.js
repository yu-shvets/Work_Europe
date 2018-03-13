$(function(){
	$('.scroll').click(function(event) {
		// event.preventDefault();
		var scroll_el = $(this).attr('href');
		if ($(scroll_el).length != 0) {
			$('html, body').animate({ scrollTop: $(scroll_el).offset().top }, 800);
		}
		return false;
	});
	$('.ourOffers-select__item').click(function(event) {
		if ($(this).hasClass('arr-b')) {
			$(this).removeClass('arr-b');
		}else {
			$(this).addClass('arr-b');
		}
	});
	$(document).mouseup(function (e) {
		if ($(event.target).closest(".ourOffers-select__item").length) return;
		$(".ourOffers-select__item").removeClass('arr-b');
		event.stopPropagation();
  	});
  	   // hide/show menu
  	   $('.menu-show').click(function(e){
  	   	e.preventDefault();
  	   	$(this).addClass('hidden');
  	   	$('.header .header-nav').addClass('show');
  	   	$('body, html').addClass('open_menu');
  	   	$('.hidden-menu').addClass('show');
  	   });
  	   $('.hidden-menu').click(function(e){
  	   	e.preventDefault();
  	   	$(this).removeClass('show');
  	   	$('.header .header-nav').removeClass('show');
  	   	$('.menu-show').removeClass('hidden');
  	   	$('body, html').removeClass('open_menu');
  	   });
  	   $(document).mouseup(function (e) {
  	   	if ($(event.target).closest(".header .header-nav").length) return;
  	   	$(".header .header-nav").removeClass('show');
  	   	$('.menu-show').removeClass('hidden');
  	   	$('body, html').removeClass('open_menu');
  	   	$('.hidden-menu').removeClass('show');
  	   	event.stopPropagation();
  	   });
  	   var windowW = $(window).width();
  	   if (windowW > 767 ) {
  	   	$('.hidden-menu').removeClass('show');
  	   }
  	   $(window).resize(function(){
  	   	var windowW = $(window).width();
  	   	if (windowW > 767 ) {
  	   		$('.hidden-menu').removeClass('show');
  	   	}
  	   });
  	   $('.cbalink').hide();
});

$('#customer_form').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        url: form.attr('action'),
        method: 'post',
        data: form.serialize(),

        success: function (json) {
            console.log('Hello!');
            $('#success').text(json.success);
            form.each(function(){
            this.reset();
            });
        }
    });
});