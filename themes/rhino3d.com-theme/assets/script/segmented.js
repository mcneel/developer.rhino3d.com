/*
 * segmented.js — pane switching for {{< segmented >}} controls.
 *
 * Loaded by partials/js-scripts.html when a page rendered at least one
 * segmented control in pane mode (the shortcode sets the "has_segmented"
 * page store flag). Link-mode controls are plain anchors and need no script.
 *
 * Each control carries its own configuration in data attributes, and every
 * lookup below is scoped to one control, so a page may hold any number of
 * them (WWW-3776). Before this, the selectors were templated into an inline
 * script and the radios had fixed ids, which limited a page to one control.
 *
 *   <div class="segmented-controls"
 *        data-segmented-panes
 *        data-a-target=".install-windows-8"
 *        data-b-target=".install-mac-8"
 *        data-b-query="upgrade=1">
 *     <input id="…-A" name="…" class="segmentInput" type="radio" checked>
 *     <label for="…-A">Windows</label>
 *     <input id="…-B" name="…" class="segmentInput" type="radio">
 *     <label for="…-B">Mac</label>
 *   </div>
 */
(function () {
  'use strict';

  function controls() {
    return document.querySelectorAll('.segmented-controls[data-segmented-panes]');
  }

  // The control's own two radios — never a nested control's.
  function inputs(root) {
    return root.querySelectorAll(':scope > input.segmentInput');
  }

  function display(selector, visible) {
    if (!selector) return;
    var panes;
    try {
      panes = document.querySelectorAll(selector);
    } catch (e) {
      // An author typo in Atarget/Btarget shouldn't take down the other
      // controls on the page.
      return;
    }
    Array.prototype.forEach.call(panes, function (pane) {
      pane.style.display = visible ? '' : 'none';
    });
  }

  function sync(root) {
    var radios = inputs(root);
    var aSelected = radios[0] ? radios[0].checked : true;
    display(root.getAttribute('data-a-target'), aSelected);
    display(root.getAttribute('data-b-target'), !aSelected);
  }

  // Deep link: ?<data-b-query> pre-selects B. "key" alone matches on presence,
  // "key=value" on an exact value. Runs before sync() so the matching pane is
  // shown on first paint.
  function preselect(root) {
    var query = root.getAttribute('data-b-query');
    if (!query) return;
    var eq = query.indexOf('=');
    var key = eq < 0 ? query : query.slice(0, eq);
    var value = eq < 0 ? null : query.slice(eq + 1);
    var params = new URLSearchParams(window.location.search);
    if (params.has(key) && (value === null || params.get(key) === value)) {
      var radios = inputs(root);
      if (radios[1]) radios[1].checked = true;
    }
  }

  // Idempotent: a control is only ever wired once, so this can run both now
  // and again at DOMContentLoaded without binding the handlers twice.
  function init() {
    Array.prototype.forEach.call(controls(), function (root) {
      if (root.hasAttribute('data-segmented-ready')) return;
      root.setAttribute('data-segmented-ready', '');
      preselect(root);
      sync(root);
      Array.prototype.forEach.call(inputs(root), function (input) {
        input.addEventListener('change', function () { sync(root); });
      });
    });
  }

  // js-scripts.html puts this at the end of <body>, so the controls above are
  // already parsed: wire them now rather than at DOMContentLoaded, so a
  // Bquery deep link (/?upgrade=1) shows its pane on the first paint instead
  // of flashing the other one. The listener covers any control that is still
  // to be parsed, and any other placement of this script.
  init();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  }

  // Restored from the back/forward cache: the browser puts the radios back the
  // way they were, so re-apply the panes to match. Handlers survive the
  // restore, so they are not bound again here.
  window.addEventListener('pageshow', function (event) {
    if (!event.persisted) return;
    Array.prototype.forEach.call(controls(), function (root) {
      preselect(root);
      sync(root);
    });
  });
})();
