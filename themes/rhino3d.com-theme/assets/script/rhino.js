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
    cookie = readCookie("MCA_CLIENT_USER_SESSION_INFO-rhino3dWebsite");
    if(cookie) {
        $('.logged_in').removeClass('hidden');
        $('.logged_out').addClass('hidden');
    }
    else {
        $('.logged_in').addClass('hidden');
        $('.logged_out').removeClass('hidden');
    }

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

    $('.section-selector').click(function(o) {
        $this = $(this);
        $('.section-selector').removeClass('selected');
        $this.addClass('selected');
        var fam = $this.attr('data-section-group');
        var name = $this.attr('data-section-name');
        var behavior = $this.attr('data-section-behavior');
        if (behavior === 'close-all') {
            $('.section').hide();
        }
        showOneInFamily(fam, name);
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
    if ($(window).width() > 768 ) {
    document.getElementById("sitesearch").style.display = "inline";
    } else {
    document.getElementById("sitesearch").style.display = "none";
    }
}
//
///////////////////////////////////////////////////


///////////////////////////////////////////////////
// Section Toggle Functions
function clearActionShowLicenseType(name) {
    showOneInFamily('action', '');
    showOneInFamily('license-type', name);
}
function showOneInFamily(family, name) {
    $('.section[data-group="' + family + '"]').hide();
    if (name != '') {
        $('.section[data-name="' + name + '"]').show()[0].scrollIntoView({
            behavior: "smooth", // or "auto" or "instant"
            block: "start" // or "end"
        });
    }
}
//
///////////////////////////////////////////////////

