mca = {};
mca.utilities = {};
mca.model = {};
mca.model.iframe = null;
mca.model.origin = "https://accounts.rhino3d.com";
mca.model.listeners = [];


mca.utilities.buildURL = function(path, qs) {

    if (Object.keys(qs).length > 0)
        path += "?";

    for (var key in qs) {
        path += (key + "=" + encodeURIComponent(qs[key]) + "&");
    }

    return path.substring(0, path.length - 1);
};

mca.utilities.getCookieForName = function(name) {
    name += "=";
    var cookie = document.cookie;
    var ca = cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return decodeURIComponent(c.substring(name.length, c.length));
        }
    }

    return undefined;
};

mca.utilities.pluckListeners = function (sub, sid) {

    var result = [];
    var remainingContainers = [];

    for (var i=0; i < mca.model.listeners.length; i++) {
        var currentContainer = mca.model.listeners[i];

        if (currentContainer.sub == sub && currentContainer.sid == sid) {
            result = result.concat(currentContainer.fns);
        } else {
            remainingContainers.push(currentContainer);
        }
    }

    mca.model.listeners = remainingContainers;
    return result;
};

mca.utilities.addListener = function (sub, sid, callbackFn) {

    //Make sure it doesn't already exist.
    var container;

    for (var i=0; i < mca.model.listeners.length; i++) {
        var currentContainer = mca.model.listeners[i];

        if (currentContainer.sub == sub && currentContainer.sid == sid) {
            container = currentContainer;
            break;
        }
    }

    if (container) {
        container.fns.push(callbackFn);
    } else {
        mca.model.listeners.push({sub: sub, sid: sid, fns: [callbackFn]});
    }
};

mca.utilities.informListeners = function (sub, sid) {
    var listeners = mca.utilities.pluckListeners(sub, sid);

    for (var i = 0; i < listeners.length; i++) {
        listeners[i]();
    }
};

mca.utilities.askLoginStatus = function (sub, sid) {
    mca.model.iframe.contentWindow.postMessage({sub: sub, sid: sid}, "*");
};

mca.utilities.askAllLoginStatus = function () {
    for (var i = 0; i < mca.model.listeners.length; i++) {
        mca.utilities.askLoginStatus(mca.model.listeners[i].sub, mca.model.listeners[i].sid)
    }
};


/**
 * We begin listening for message events from an iframe we create that will
 * tell us when someone has logged out of https://accounts.rhino3d.com
 */
(function () {
    //Setup the iframe.
    window.addEventListener("message", function (e) {

        if (e.origin !== mca.model.origin || !mca.model.iframe || e.source !== mca.model.iframe.contentWindow)
            return;

        //See who the message is geared towards and inform them.
        mca.utilities.informListeners(e.data.sub, e.data.sid);

    }, false);

    document.addEventListener("DOMContentLoaded", function() {

        mca.model.iframe = document.createElement('iframe');
        mca.model.iframe.style.display = 'none';
        mca.model.iframe.src = 'https://accounts.rhino3d.com/login-status-iframe';
        document.body.appendChild(mca.model.iframe);

        mca.model.iframe.addEventListener("load", function() {
            //Process pending listeners.
            mca.utilities.askAllLoginStatus();

            window.addEventListener("focus", function () {
                //Whenever the window is focused, we ask the iframe about the current login status of the user.
                mca.utilities.askAllLoginStatus();

            }, false);
        });
    });
}());


/**
 * PUBLIC METHODS BELOW THIS LINE.
 */


/**
 * Adds a logout listener that will be invoked whenever the specified user logs out of accounts.rhino3d.com.
 * If the user is already logged out, the listener will be invoked immediately in the current or next run loop.
 * @param sub The user's unique id in Rhino Accounts.
 * @param sid The Session Id included in the OpenID Connect Token.
 * @param callbackFn A function called when said user logs out of accounts.rhino3d.com
 */
mca.addLogoutListener = function(sub, sid, callbackFn) {

    mca.utilities.addListener(sub, sid, callbackFn);

    if (mca.model.iframe) {
        //Ask the iframe about the current login status of the user.
        mca.utilities.askLoginStatus(sub, sid);
    }
};


/**
 * A convenience function for sites using the Rhino Accounts Client Module.
 * This function looks up the currently logged in user and the session id for the given client id automatically.
 * @param clientId The id of the client to whom the OpenID Connect Token was issued to.
 * @param callbackFn A function called when said user logs out of accounts.rhino3d.com, with a logoutURL argument.
 */
mca.addLogoutListenerForClientId = function (clientId, callbackFn) {

    //First we see if the user is logged in.
    var infoCookie = mca.utilities.getCookieForName("MCA_CLIENT_USER_SESSION_INFO-" + clientId);

    if (!infoCookie)
        return;

    infoCookie = JSON.parse(infoCookie);

    mca.addLogoutListener(infoCookie.sub, infoCookie.sid, function () {

        //Build the logout url.
        var logoutURL = mca.utilities.buildURL("/" + encodeURIComponent(clientId) + "/mcneel-accounts/logout", {
            nonce: infoCookie.nonce,
            host_url: window.location.origin,
            dest_url: window.location.href
        });

        callbackFn(logoutURL);
    });
};


mca.startSecureCallback = function (controllerName, a, oauth2Token, callbackFn) {
    //callbackFn params: success, result
    a.controller = controllerName;
    a.secureCallback = "true";
    var childWindow = window.open(mca.utilities.buildURL(mca.model.origin + "/", a));

    //Now we wait for a message to be delivered.
    window.addEventListener("message", function (e) {

        if (e.origin !== mca.model.origin ||  e.source !== childWindow)
            return;

        if (e.data.loaded) {
            childWindow.postMessage({token: oauth2Token}, mca.model.origin); //It's crucial that we only reveal the token to the origin.
        } else if (e.data.finished) {
            childWindow.close();
            callbackFn(true, e.data.result);
        }

    }, false);
};