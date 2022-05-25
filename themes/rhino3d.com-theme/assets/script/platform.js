
//  A great Javascript DOM tutorial:  https://youtu.be/SowaJlX1uKA 

  // Function to add the class of show to the node that has
  // the class that matches the current value of the select drop down (#choose)
// Specify the class names for Window Mac
const pWin = "Rhino_Win"
const pMac = "Rhino_Mac"

  function displayPlatform (showThis) {
    var x = document.getElementsByClassName(showThis);
    for ( i = 0; i < x.length; i++ ) {
      x[i].style.display = "contents";
    }
  }

  function hidePlatform ( hideThis ) {
    var x = document.getElementsByClassName(hideThis);
    for ( i = 0; i < x.length; i++ ) {
      x[i].style.display = "none";
    }
  }

  function showPlatform (showP) {
    var ele = document.getElementsByName("showPlatform");
    if (ele) {      
      if (showP == pWin) {
        Cookies.set("rhinoPlat", pWin);
        displayPlatform (pWin);
        console.log("setting Windows");
        hidePlatform (pMac);
        ele[0].checked = true;
      } else if (showP == pMac) {
        Cookies.set("rhinoPlat", pMac);
        displayPlatform (pMac);
        console.log("Setting Mac");
        hidePlatform (pWin);
        ele[1].checked = true;
      }
    }
  }

  function checkCookie() {
    var cplatform = Cookies.get("rhinoPlat");
    if (cplatform != "") {
      console.log(`cookie-state:${cplatform}`);
    } else {
      console.log("No cookie set");
    }
  }


function winmacswitch(){
  var ele = document.getElementsByName('showPlatform'); 
 
  for(i = 0; i < ele.length; i++) { 
      if(ele[0].checked) {
       console.log ("Button:Windows");
       showPlatform( pWin );
      } else if (ele[1].checked) {
        console.log("Button:Mac");
        showPlatform( pMac );      
      } else {
        console.log("none");          
      }
  }
} 

/*
Logic for Cookies
- Default Windows is displayed
- Check and return current default
   - the browser type
   - Read an exisitng cookie
   - Set platform switcher to platform, if platform is recognized.
   - SHow selected Platform
- Read any Update event to the Platform radio button and store cookie

*/


window.onload=function(){
  if (typeof(Storage) !== "undefined") {
    // Code for localStorage
    console.log("Local storage enabled");
    var navplatform = this.navigator.platform;
    console.log(`Platform: ${navplatform}`);
    var ccookie = Cookies.get("rhinoPlat");
    if (ccookie) {
        // Then set platform to cookie
        console.log (`Cookie Used: ${ccookie}`);
        this.showPlatform(ccookie);
      } else {
        // Then set to browser
        console.log ("No Cookie stored");
/*Here is the code to automatically switch when encountering both an Iphone and a Mac.
  if (!!navigator.platform && /^iP|^Mac/.test(navigator.platform)) {   
  It was decided not to switch for mobile since it is not a good indicator of desktop platform.     
*/
      if (!!navigator.platform && /^Mac/.test(navigator.platform)) {
          this.showPlatform(pMac);
        } else {
          this.showPlatform(pWin);
        }
      }
    } else {
    // Code for no localStorage
      console.log("No Local storage");
  } 
}

