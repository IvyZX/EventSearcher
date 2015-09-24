var main = function(){
	$('.arrow-next1').click(function(){
		var currentSlide = $('.active-slide');
		var nextSlide = $('.slide2');
		
		currentSlide.fadeOut(1000).removeClass('active-slide');
		nextSlide.fadeIn(1000).addClass('active-slide');
	});
	
	$('.arrow-next2').click(function(){
		var currentSlide = $('.active-slide');
		var nextSlide = $('.slide3');
		
		currentSlide.fadeOut(1000).removeClass('active-slide');
		nextSlide.fadeIn(1000).addClass('active-slide');
	});
	
	$('.arrow-next3').click(function(){
		var currentSlide = $('.active-slide');
		var nextSlide = $('.slide4');
		
		currentSlide.fadeOut(1000).removeClass('active-slide');
		nextSlide.fadeIn(1000).addClass('active-slide');
	});
	
}

$(document).ready(main);