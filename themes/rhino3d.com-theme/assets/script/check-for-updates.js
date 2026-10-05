/*
 * check-for-updates.js
 *
 * Fills in the /check-for-updates/ page (RH-15299).
 *
 * Rhino's Options > Updates and Statistics > "Check Now..." opens
 * www2.mcneel.com/updates/<id>/<edition>/<platform>/<locale>/<stability>/<version>,
 * which redirects here with those details in the query string and the language
 * in the path. We rebuild the API path from them and ask
 * /www-api/updates/...?format=json, which answers with one of three states:
 *
 *   {"status": "update_available", "url": "https://files.mcneel.com/...",
 *    "version": "8.34.26223.11001"}
 *   {"status": "up_to_date"}
 *   {"status": "unavailable"}   (HTTP 502)
 *
 * version is optional: the button falls back to the plain "Download now" label
 * when it is absent, so the page works against an API that predates it.
 *
 * Every string shown to the user comes from data-* attributes that the
 * check-for-updates-widget partial fills in from i18n, so there is no English
 * in here. The container starts out showing the "unavailable" message, which is
 * also what a visitor without JavaScript is left with.
 */
(function () {
  'use strict';

  var PARAMS = ['id', 'edition', 'platform', 'locale', 'stability', 'version'];

  /* "8.34.26223.11001" reads as "8.34" on a button. Anything that is not the
   * expected shape is left out of the label rather than shown raw. */
  function shortVersion(version) {
    var parts = /^(\d+)\.(\d+)\./.exec(version || '');
    return parts ? parts[1] + '.' + parts[2] : null;
  }

  function downloadLabel(root, version) {
    var short = shortVersion(version);
    var template = root.getAttribute('data-label-download-version');
    if (short && template && template.indexOf('[VERSION]') !== -1) {
      return template.replace('[VERSION]', short);
    }
    return root.getAttribute('data-label-download');
  }

  function show(root, message, downloadUrl, version) {
    var messageEl = root.querySelector('[data-cfu-message]');
    var actionEl = root.querySelector('[data-cfu-action]');
    var linkEl = root.querySelector('[data-cfu-download]');
    var labelEl = root.querySelector('[data-cfu-download-label]');

    if (messageEl) {
      messageEl.textContent = message;
    }
    if (actionEl && linkEl) {
      if (downloadUrl) {
        linkEl.href = downloadUrl;
        if (labelEl) {
          labelEl.textContent = downloadLabel(root, version);
        }
        actionEl.hidden = false;
      } else {
        actionEl.hidden = true;
      }
    }
  }

  /* The URL comes from our own API, but it ends up in an href, so only accept
   * an https McNeel address rather than whatever arrives. */
  function safeDownloadUrl(value) {
    if (!value) {
      return null;
    }
    try {
      var parsed = new URL(value, window.location.href);
      var isMcNeel = parsed.hostname === 'mcneel.com' ||
                     parsed.hostname.endsWith('.mcneel.com');
      return (parsed.protocol === 'https:' && isMcNeel) ? parsed.href : null;
    } catch (e) {
      return null;
    }
  }

  function apiUrl(root, query) {
    var segments = PARAMS.map(function (name) {
      return encodeURIComponent(query.get(name));
    });
    return root.getAttribute('data-api-base') + '/' + segments.join('/') +
           '?format=json';
  }

  function run(root) {
    var query = new URLSearchParams(window.location.search);
    var missing = PARAMS.some(function (name) {
      return !query.get(name);
    });

    /* Reached without Rhino's parameters - a bookmark, or someone typing the
     * URL. There is no installation to check, so say so rather than guess. */
    if (missing) {
      show(root, root.getAttribute('data-msg-no-details'), null);
      return;
    }

    show(root, root.getAttribute('data-msg-checking'), null);

    fetch(apiUrl(root, query), { headers: { Accept: 'application/json' } })
      .then(function (response) {
        return response.json().catch(function () {
          return { status: 'unavailable' };
        });
      })
      .then(function (data) {
        var url = safeDownloadUrl(data && data.url);
        if (data && data.status === 'update_available' && url) {
          show(root, root.getAttribute('data-msg-update-available'), url,
               data.version);
        } else if (data && data.status === 'up_to_date') {
          show(root, root.getAttribute('data-msg-up-to-date'), null);
        } else {
          show(root, root.getAttribute('data-msg-unavailable'), null);
        }
      })
      .catch(function () {
        show(root, root.getAttribute('data-msg-unavailable'), null);
      });
  }

  function init() {
    var root = document.querySelector('[data-check-for-updates]');
    if (root) {
      run(root);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
