$(window).on('load', function() {

    $('.slide-carousel').owlCarousel({
        loop: true,
        autoplay: true,
        dots: true,
        responsiveClass: true,
        navText: [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ],
        responsive: {
            0: {
                items: 1,
                nav: false,
                dots: true,
                loop: true
            }
        }
    });
	
		$('.slide-carousel').on('translate.owl.carousel', function () {
        $('.this-item h2').removeClass('fadeInUp animated').hide();
        $('.this-item h3').removeClass('fadeInUp animated').hide();
        $('.this-item p').removeClass('fadeInUp animated').hide();
    });

    $('.slide-carousel').on('translated.owl.carousel', function () {
        $('.this-item h2').addClass('fadeInUp animated').show();
        $('.this-item h3').addClass('fadeInUp animated').show();
        $('.this-item p').addClass('fadeInUp animated').show();
    });
	
});	
	