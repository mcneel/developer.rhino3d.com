/*
 * subscribe.js — behaviour for the {{< subscribe >}} shortcode (WWW-3622).
 *
 * The shortcode emits a .rh-subscribe root carrying data-maillist and
 * data-id, a button, an error line and a sign-in <dialog>. This script:
 *
 *   - looks up the visitor's Rhino Accounts token once (shared by every
 *     button on the page) and, when signed in, their current subscriptions;
 *     a list they are already on shows as "subscribed" straight away;
 *   - on click, signed in: POSTs the subscription and flips the root to
 *     data-state="subscribed" — the button stays on the page as a check mark
 *     plus "Subscribed" instead of disappearing;
 *   - on click, signed out: opens the dialog; its sign-in button goes to the
 *     site login and comes back to this page with ?subscribe=<maillist>:<id>,
 *     which finishes the subscription on arrival (the legacy ?subscribe=1
 *     still works and means "every list on the page");
 *   - honours the legacy `container` param by moving the widget into that
 *     element (the TOC's top/bottom slots).
 *
 * Every visible string lives in the shortcode's markup; the script only
 * switches data-state and the error line's hidden attribute.
 *
 * Loaded only on pages that use the shortcode (see partials/js-scripts.html).
 */
(function () {
    'use strict';

    var API_URL = 'https://api.mcneel.com/maillist/preferences';
    var SESSION_URL = 'https://www.rhino3d.com/licenses/session_variables.json';
    var LOGIN_URL = 'https://www.rhino3d.com/user/login';
    var SITE_URL = 'https://www.rhino3d.com';
    var ID_FIELDS = {
        profession: ['ProfessionID'],
        market_segment: ['MarketSegmentID'],
        companion_product: ['CompanionProductId'],
        // WWW-3609: the API resolves a legacy list by ID or name, so authors may pass either.
        legacy_maillist: ['LegacyMaillistID', 'LegacyMaillistName']
    };

    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    function asJson(response) {
        return response.ok ? response.json() : Promise.reject(response.status);
    }

    // One session lookup per page; '' means signed out (or unreachable).
    var tokenPromise = null;
    function getToken() {
        if (!tokenPromise) {
            tokenPromise = fetch(SESSION_URL, { credentials: 'same-origin' })
                .then(asJson)
                .then(function (data) { return (data && data.oauth2Token) || ''; })
                .catch(function () { return ''; });
        }
        return tokenPromise;
    }

    // One preferences lookup per page; null when it fails.
    var subscriptionsPromise = null;
    function getSubscriptions(token) {
        if (!subscriptionsPromise) {
            subscriptionsPromise = fetch(API_URL, { headers: { Authorization: 'Bearer ' + token } })
                .then(asJson)
                .catch(function () { return null; });
        }
        return subscriptionsPromise;
    }

    function isSubscribed(data, maillist, id) {
        var fields = ID_FIELDS[maillist];
        var rows = data && data[maillist];
        if (!fields || !Array.isArray(rows)) return false;
        // SQL compares legacy list names case-insensitively.
        var want = String(id).toLowerCase();
        return rows.some(function (row) {
            return fields.some(function (field) { return String(row[field]).toLowerCase() === want; });
        });
    }

    function listKey(maillist, id) {
        return maillist + ':' + id;
    }

    // ?subscribe=<maillist>:<id> targets one list; the legacy ?subscribe=1
    // (what the old login redirect sent) means every list on the page.
    function wantsAutoSubscribe(key) {
        var value = new URLSearchParams(window.location.search).get('subscribe');
        return value === key || value === '1';
    }

    function dropQueryParam() {
        if (!window.history || !window.history.replaceState) return;
        var params = new URLSearchParams(window.location.search);
        params.delete('subscribe');
        var query = params.toString();
        window.history.replaceState(null, '', window.location.pathname + (query ? '?' + query : '') + window.location.hash);
    }

    function init(root) {
        var maillist = root.getAttribute('data-maillist');
        var id = root.getAttribute('data-id');
        var key = listKey(maillist, id);
        var button = root.querySelector('.rh-subscribe-button');
        var error = root.querySelector('.rh-subscribe-error');
        var dialog = root.querySelector('.rh-subscribe-dialog');
        var loginButton = root.querySelector('.rh-subscribe-login');
        var closeButton = root.querySelector('.rh-subscribe-dialog-close');

        // Legacy `container` param: move the whole widget into that element.
        var containerId = root.getAttribute('data-container');
        var container = containerId && document.getElementById(containerId);
        if (container) container.appendChild(root);

        function setState(state) {
            root.setAttribute('data-state', state);
            button.disabled = state !== 'idle';
        }

        function subscribe(token) {
            var body = {};
            body[maillist] = [{ id: id, add: true }];
            error.hidden = true;
            setState('saving');
            return fetch(API_URL, {
                method: 'POST',
                headers: {
                    Authorization: 'Bearer ' + token,
                    'Content-Type': 'application/json',
                    Accept: 'application/json'
                },
                body: JSON.stringify(body)
            }).then(function (response) {
                if (!response.ok) throw response.status;
                setState('subscribed');
            }).catch(function () {
                setState('idle');
                error.hidden = false;
            });
        }

        function login() {
            var redirect = SITE_URL + window.location.pathname + '?subscribe=' + encodeURIComponent(key);
            window.location.assign(LOGIN_URL + '?redirect_uri=' + encodeURIComponent(redirect));
        }

        function askToSignIn() {
            if (dialog && typeof dialog.showModal === 'function') {
                dialog.showModal();
            } else {
                login();   // no <dialog> support: go straight to sign-in
            }
        }

        button.addEventListener('click', function () {
            getToken().then(function (token) {
                if (token) {
                    subscribe(token);
                } else {
                    askToSignIn();
                }
            });
        });

        if (loginButton) loginButton.addEventListener('click', login);
        if (closeButton) closeButton.addEventListener('click', function () { dialog.close(); });
        if (dialog) {
            // A click on the backdrop lands on the <dialog> element itself.
            dialog.addEventListener('click', function (e) {
                if (e.target === dialog) dialog.close();
            });
        }

        // Already on the list? Show it. Just back from sign-in? Finish up.
        getToken().then(function (token) {
            if (!token) return;
            return getSubscriptions(token).then(function (data) {
                if (isSubscribed(data, maillist, id)) {
                    setState('subscribed');
                } else if (wantsAutoSubscribe(key)) {
                    dropQueryParam();
                    subscribe(token);
                }
            });
        });
    }

    ready(function () {
        document.querySelectorAll('.rh-subscribe').forEach(init);
    });
})();
