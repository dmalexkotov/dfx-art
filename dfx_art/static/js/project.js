$(document).ready(function() {
    $('.single_progect_descr').find('img').each(function(i, x){
        const itemsCount = $(x).nextAll('p').length;
        if (itemsCount > 0){
            $(x).nextAll('p')[0].remove();
        }
    })
});

$("video").contextmenu(function (event) {
    event.preventDefault();
})