function privacyStatus() {
    const privacy = Cookies.get('eprivacy');
    return privacy
}

function privacyCheck() {
    if (privacyStatus() == 'accept') {
        return true;
    }
    return false;
}

$(document).ready(function() {
    const privacy = Cookies.get('eprivacy');
    $('.privacy_box .accept_button').click(function name() {
        Cookies.set('eprivacy', 'accept');
        $('.privacy_box').hide()
    })
    if (privacy) {
        
    } else {
        $('.privacy_box').show() 
    }
});