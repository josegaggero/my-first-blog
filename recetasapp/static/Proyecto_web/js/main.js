document.addEventListener('DOMContentLoaded', () => {
    const elementosCarousel = document.querySelectorAll('.carousel')
    M.Carousel.init(elementosCarousel, {
        duration: 150,
        dist: -80,
        shift: 5,
        padding: 9,
        numVisible: 5,

        noWrap: true,


    });

});

$(document).ready(function() {

    var show = 1;

    $('.show').on('click', function() {

        if (show == 1) {
            $('.content-menu').addClass("content-menu2");
            show = 0;
        } else {
            $('.content-menu').removeClass("content-menu2");
            show = 1;
        }


    })

})