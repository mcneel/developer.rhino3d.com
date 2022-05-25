/////////////////////////////////////////////////////////////////////////
// Header Scrolling Functions
// When the user scrolls down 80px from the top of the document, 
// resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    var footer = $(".footer");
    var footerPosTop = footer.position().top;
    var viewportHeight = $(window).height();
    var scrollPos = document.body.scrollTop || document.documentElement.scrollTop; 
    var footerFromTop = footerPosTop - scrollPos;

    if (scrollPos > 80 ) {
    contractNavBar();
    setTocHeight( viewportHeight- Math.max(viewportHeight - footerFromTop, 0) - 55);
    } else {
    expandNavBar();
    setTocHeight( viewportHeight- Math.max(viewportHeight - footerFromTop, 0) - 125);
    }
}

function expandNavBar() {
    if ($(window).width() > 768) {
    document.getElementById("sitesearch").style.display = "inline";
    } else {
    document.getElementById("sitesearch").style.display = "none";
    }
    document.getElementById("logo-container").style.height = "125px";
    document.getElementById("logo-title-text-secondary").style.display = "inline";
    document.getElementById("logo-title-text").style.fontSize = "40px";
    document.getElementById("logo-title-text").style.top = "-10px";
    document.getElementById("logo-title-text").style.left = "90px";
    document.getElementById("site-nav-logo").style.height = "125px";
    document.getElementById("logo-subtitle").style.opacity = 1;
    document.getElementById("logo-subtitle").style.pointerEvents = "all";
    expandTOC();
}

function contractNavBar() {
    document.getElementById("sitesearch").style.display = "none";
    document.getElementById("logo-container").style.height = "55px";
    document.getElementById("site-nav-logo").style.height = "55px";
    document.getElementById("logo-title-text-secondary").style.display = "none";
    document.getElementById("logo-title-text").style.fontSize = "25px";
    document.getElementById("logo-title-text").style.top = "7px";
    document.getElementById("logo-title-text").style.left = "70px";
    document.getElementById("logo-subtitle").style.opacity = 0;
    document.getElementById("logo-subtitle").style.pointerEvents = "none";
    contractTOC();
}

function expandTOC() {
    if (document.getElementsByClassName("toc")[0]){
        document.getElementsByClassName("toc")[0].style.top = "150px";
    }
}

function contractTOC() {
    if (document.getElementsByClassName("toc")[0]){
        document.getElementsByClassName("toc")[0].style.top = "80px";
    }
}

function setTocHeight(height) {
    var paddedHeight = height-65
    if (document.getElementById("TableOfContents")){
        document.getElementById("TableOfContents").style.height = `${paddedHeight}px`;
    }
}
