$(document).ready(function() {
    $('.portfolio-navigation .btn-main').click(function(){
        $.get(`/api/v2/portfolio/${pageId}/projects-ajax/`, { page: pageNumber + 1, size: pageSize }, function( data, status, r ) {
            $(".portfolio-list").append(data);
            pageNumber = pageNumber + 1;
            if (r.status == 211) {
                $('.portfolio-navigation .btn-main').hide()
            }
        });
        
    })
});