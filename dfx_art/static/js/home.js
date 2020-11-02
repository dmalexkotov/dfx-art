$(document).ready(function() {
    $('.history__desc a[href="/#cut"]').parent().nextAll('p').addClass('hide hide-xl');
    $('.projects__item a').unbind('click')
});