function showhide(divid, state){
    document.getElementById(divid).style.display=state
}
function email(emname,domain){
    var email = "mailto:"+emname + "@"+domain;
    document.location=email;
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// True if Rhino Accounts has left a session cookie for any client id. The id
// varies by host (rhino3dWebsite on www, rhino3dWebsiteDEBUG everywhere else),
// so matching the prefix rather than one name keeps the navbar's logged-in
// state working on staging and dev too, where the avatar and account links
// used to never appear at all (WWW-3684).
function hasAccountSession() {
    var prefix = "MCA_CLIENT_USER_SESSION_INFO-";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(prefix) == 0) return true;
    }
    return false;
}

$(document).ready(function(){

    // Set up tabs for learn page (and others?)
    $( "#tabs" ).tabs();
    $( ".ui-tabs-vertical li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );

    // Search Box
    $('#cse-search-box .searchBox').focus(function(){
      $(this).css('cursor', 'auto')
          .css('color', 'black').animate( {
            width: '15em',
            marginBottom: '1.8em',
            borderColor: 'black'
          }, 150
          )
          .val('');
    }).blur(function(){
      $(this).animate({
          borderColor: 'white',
          width: '',
          marginBottom: '0px'
      }, 150).css('cursor', 'pointer')
    });

    $('#cse-search-box').bind('submit', function(e) {
     $('#q').val($('#ss').val());
    });

    var is_mcneel = false;
    $.getJSON('/user/is-mcneel/', function(data){
        is_mcneel = data[0];
        if(is_mcneel) {
            $('.mcneel_only').removeClass('hidden');
        }
    });
    if(hasAccountSession()) {
        $('.logged_in').removeClass('hidden');
        $('.logged_out').addClass('hidden');
    }
    else {
        $('.logged_in').addClass('hidden');
        $('.logged_out').removeClass('hidden');
    }

    // /user/avatar/ has no image to serve for every account, and can be
    // blocked outright. Hide an avatar that fails to load so the Font Awesome
    // fallback glyph behind it shows through instead of a broken-image icon
    // (see .dd-button::before in _partial/_nav-account.scss, WWW-3684).
    $('.avatar').each(function() {
        var img = this;
        var hideBroken = function() { $(img).addClass('hidden'); };
        // The error may already have fired before this script ran
        if (img.complete && img.naturalWidth === 0) hideBroken();
        $(img).on('error', hideBroken);
    });

    $(".rhinoProtocol").click(function (event) {
        var url = $(this).attr('href');
        var encodedUrl = encodeURIComponent(url);
        var verb = $(this).attr('data-verb');
        var path = 'rhino://' + verb + "?url=" + encodedUrl;
        protocolCheck($(this).attr("href"), function () {
                window.location = url;
            });
        window.location = path;
        event.preventDefault ? event.preventDefault() : event.returnValue = false;
    });

});

///////////////////////////////////////////////////
// Open the overlay menu when clicking the menu 
// (hamburger) button
function toggleMenu() {
    let logoContainer = document.getElementById("logo-container")
    let height = window.innerHeight-logoContainer.offsetHeight;
    let menuItems = document.getElementById("theMenuItems");
    let toggleIcon = document.getElementById("menuToggleIcon");
    if (toggleIcon.className === "fa fa-times") {
        document.body.style.overflowY = "visible";
        menuItems.style.height = "0vh";
        toggleIcon.className = "fa fa-bars";
    } else {
        document.body.style.overflowY = "hidden";
        menuItems.style.height = `${height}px`;
        toggleIcon.className = "fa fa-times"
    }
}
//
///////////////////////////////////////////////////


///////////////////////////////////////////////////
// Resizing to show/hide the menu (hamburger) button
window.onresize = function() {resizeFunction()};

function resizeFunction() {
    if ($(window).width() > 848 ) {
        var scrollPos = document.body.scrollTop || document.documentElement.scrollTop; 
        if (scrollPos <= 80 ) {
            document.getElementById("sitesearch").style.display = "inline";
        }
    } else {
    document.getElementById("sitesearch").style.display = "none";
    }
}
//
///////////////////////////////////////////////////



