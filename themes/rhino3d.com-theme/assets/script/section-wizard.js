/*
 * section-wizard.js — one-step-at-a-time chooser for the
 * {{< section-selector >}} / {{< section >}} shortcodes (WWW-3686).
 *
 * The shortcodes emit a flat page: a list of selectors, then every `.section`
 * body, all hidden. This script folds that flat markup into a horizontal
 * wizard: the opening list is panel 0, each shortcode *group* (in document
 * order) becomes the next panel. Picking a selector slides the track left to
 * the panel holding that group and shows the chosen section; a back arrow
 * above the track slides back, labelled with the step it returns to.
 *
 * Nothing here is page-specific: the steps come from the `data-group` values
 * in the markup, and every visible string is content (a selector label or a
 * section heading), so translated pages need no extra work.
 *
 * The chosen path lives in the URL fragment so a step can be linked and
 * shared all the way through to the final answer:
 *
 *     #commercial                     → license type
 *     #commercial/assign-to-team      → license type + the solution
 *
 * The legacy multi-hash form (`#commercial#assign-to-team`) still loads, and
 * is rewritten to the canonical form on arrival.
 *
 * Loaded only on pages that use the shortcodes (see partials/js-scripts.html).
 */
(function () {
    'use strict';

    var HEADER_OFFSET = 80;   // sticky navbar, so a scrolled-to panel clears it
    var SLIDE_MS = 320;       // keep in sync with $wizard-slide in the SCSS

    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    function toArray(list) {
        return Array.prototype.slice.call(list);
    }

    function reducedMotion() {
        return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    }

    /* Text used to label the back button for a panel: a section's own heading,
       or the heading that introduces the opening list. */
    function headingText(el) {
        if (!el) return '';
        var h = el.querySelector(':is(h1, h2, h3, h4, h5, h6):not([data-toc="skip"])');
        if (!h && /^H[1-6]$/.test(el.tagName)) h = el;
        return h ? h.textContent.trim() : '';
    }

    ready(function () {
        var sections = toArray(document.querySelectorAll('.section[data-group]'));
        if (!sections.length) return;

        var allSelectors = toArray(document.querySelectorAll('.section-selector'));
        var rootSelectors = allSelectors.filter(function (el) {
            return !el.closest('.section');
        });
        if (!rootSelectors.length) return;

        /* The rendered content element the shortcodes were written into. */
        var root = sections[0].parentNode;

        /* Steps: one panel per group, in the order the groups first appear. */
        var groups = [];
        sections.forEach(function (s) {
            var g = s.getAttribute('data-group');
            if (g && groups.indexOf(g) < 0) groups.push(g);
        });

        /* name -> group, for reading a path out of the URL. */
        var groupOf = {};
        sections.forEach(function (s) {
            groupOf[s.getAttribute('data-name')] = s.getAttribute('data-group');
        });

        // ---------------------------------------------------------------
        // Build the wizard around the existing markup
        // ---------------------------------------------------------------

        /* Top-level blocks holding the opening selectors (normally one <ul>),
           plus the heading that introduces them, so the whole step slides. */
        var openingBlocks = [];
        rootSelectors.forEach(function (el) {
            var block = el;
            while (block.parentNode && block.parentNode !== root) block = block.parentNode;
            if (block.parentNode === root && openingBlocks.indexOf(block) < 0) openingBlocks.push(block);
        });
        if (!openingBlocks.length) return;

        var lead = [];
        var prev = openingBlocks[0].previousElementSibling;
        while (prev && !prev.classList.contains('section')) {
            lead.unshift(prev);
            if (/^H[1-6]$/.test(prev.tagName)) break;     // heading found: stop here
            prev = prev.previousElementSibling;
        }
        if (!lead.length || !/^H[1-6]$/.test(lead[0].tagName)) lead = [];  // no heading, take the list alone

        var wizard = document.createElement('div');
        wizard.className = 'section-wizard';

        var nav = document.createElement('div');
        nav.className = 'section-wizard__nav';
        var back = document.createElement('button');
        back.type = 'button';
        back.className = 'section-wizard__back';
        var backLabel = document.createElement('span');
        backLabel.className = 'section-wizard__back-label';
        back.appendChild(backLabel);
        nav.appendChild(back);

        var viewport = document.createElement('div');
        viewport.className = 'section-wizard__viewport';
        var track = document.createElement('div');
        track.className = 'section-wizard__track';
        viewport.appendChild(track);

        wizard.appendChild(nav);
        wizard.appendChild(viewport);
        root.insertBefore(wizard, lead.length ? lead[0] : openingBlocks[0]);

        var panels = [];
        function addPanel() {
            var p = document.createElement('div');
            p.className = 'section-wizard__panel';
            p.setAttribute('tabindex', '-1');
            track.appendChild(p);
            panels.push(p);
            return p;
        }

        var opening = addPanel();
        lead.concat(openingBlocks).forEach(function (el) { opening.appendChild(el); });

        groups.forEach(function (group) {
            var panel = addPanel();
            sections.filter(function (s) {
                return s.getAttribute('data-group') === group;
            }).forEach(function (s) {
                s.style.display = '';            // visibility is class-driven from here on
                panel.appendChild(s);
            });
        });

        /* A list item that *starts* with a selector is a choice, so it is
           drawn as a row: the whole row reacts and is clickable, not just the
           label. A selector used mid-sentence stays an inline link. */
        function choiceRow(el) {
            var block = el.parentNode;
            if (!block || block.firstElementChild !== el) return null;
            for (var n = block.firstChild; n && n !== el; n = n.nextSibling) {
                if (n.nodeType === 3 && n.textContent.trim()) return null;
            }
            if (block.tagName === 'LI') return block;
            /* An item with sub-points is a loose list item, so its text is
               wrapped in a paragraph. */
            var li = block.tagName === 'P' ? block.parentNode : null;
            if (li && li.tagName === 'LI' && li.firstElementChild === block) return li;
            return null;
        }

        allSelectors.forEach(function (el) {
            var li = choiceRow(el);
            if (!li) return;
            li.classList.add('section-wizard__choice');
            li.parentNode.classList.add('section-wizard__choices');
        });

        var openingLabel = headingText(lead[0]) || document.title;

        // ---------------------------------------------------------------
        // State: one pick per group, and the panel we are showing
        // ---------------------------------------------------------------

        var picks = groups.map(function () { return ''; });
        var step = 0;

        function sectionFor(group, name) {
            if (!name) return null;
            return panels[groups.indexOf(group) + 1].querySelector('.section[data-name="' + name + '"]');
        }

        /* The path to the current step. A step that was never picked (a link
           straight to a later step) is simply left out — reading it back
           lands on the same panel. */
        function buildHash() {
            var path = [];
            for (var i = 0; i < step; i++) {
                if (picks[i]) path.push(picks[i]);
            }
            return path.length ? '#' + path.join('/') : '';
        }

        /* Reads the fragment as a path through the steps. Accepts `#a/b`, the
           legacy `#a#b`, and a bare `#b` (a step name on its own — show that
           step and let Back walk out of it).

           Returns null when the fragment is not ours, so an ordinary in-page
           anchor (the heading links AnchorJS adds, say) leaves the wizard
           alone instead of resetting it. */
        function readHash() {
            var raw = (window.location.hash || '').replace(/^#/, '');
            var names = raw.split(/[#\/]/).filter(Boolean).map(decodeURIComponent);
            var next = groups.map(function () { return ''; });
            var deepest = 0;
            names.forEach(function (name) {
                var group = groupOf[name];
                if (!group) return;
                var i = groups.indexOf(group);
                next[i] = name;
                if (i + 1 > deepest) deepest = i + 1;
            });
            /* Only offer a step whose section actually exists. */
            while (deepest > 0 && !next[deepest - 1]) deepest--;
            if (deepest > 0) return { picks: next, step: deepest, canonical: true };

            /* Not a step name: an id *inside* a step still opens that step,
               so a link to a heading in a section lands somewhere useful. */
            var target = raw && document.getElementById(raw);
            var section = target && target.closest('.section[data-group]');
            if (section) {
                var g = groups.indexOf(section.getAttribute('data-group'));
                if (g >= 0) {
                    next[g] = section.getAttribute('data-name');
                    return { picks: next, step: g + 1, canonical: false, target: target };
                }
            }
            if (raw) return null;
            return { picks: next, step: 0, canonical: true };
        }

        function render(opts) {
            opts = opts || {};

            groups.forEach(function (group, i) {
                var panel = panels[i + 1];
                toArray(panel.querySelectorAll('.section')).forEach(function (s) {
                    s.classList.toggle('is-active', s.getAttribute('data-name') === picks[i]);
                });
            });

            allSelectors.forEach(function (el) {
                var i = groups.indexOf(el.getAttribute('data-section-group'));
                var on = i >= 0 && picks[i] === el.getAttribute('data-section-name');
                el.classList.toggle('selected', on);
                el.setAttribute('aria-pressed', on ? 'true' : 'false');
                var row = el.closest('.section-wizard__choice');
                if (row) row.classList.toggle('is-selected', on);
            });

            panels.forEach(function (p, i) {
                var active = i === step;
                p.classList.toggle('is-active', active);
                p.setAttribute('aria-hidden', active ? 'false' : 'true');
            });

            wizard.setAttribute('data-step', String(step));
            track.style.transform = 'translateX(-' + (step * 100) + '%)';

            back.hidden = step === 0;
            if (step > 0) {
                backLabel.textContent = step === 1
                    ? openingLabel
                    : headingText(sectionFor(groups[step - 2], picks[step - 2])) || openingLabel;
            }

            syncHeight();

            if (opts.scroll) scrollToWizard();
            if (opts.focus) {
                window.setTimeout(function () {
                    panels[step].focus({ preventScroll: true });
                }, reducedMotion() ? 0 : SLIDE_MS);
            }
        }

        function syncHeight() {
            var panel = panels[step];
            var h = panel.getBoundingClientRect().height;
            if (h) viewport.style.height = h + 'px';
        }

        function scrollToWizard() {
            var top = wizard.getBoundingClientRect().top;
            if (top >= HEADER_OFFSET && top < window.innerHeight * 0.6) return;   // already in view
            window.scrollTo({
                top: window.pageYOffset + top - HEADER_OFFSET,
                behavior: reducedMotion() ? 'auto' : 'smooth'
            });
        }

        /* How many steps deep into this page's own history we are, carried in
           the history entry itself so it survives Back and Forward. Zero means
           every entry behind us belongs to somewhere else, which is what
           arriving on a link to a step looks like. */
        var depth = (window.history.state && window.history.state.wizardDepth) || 0;

        function urlFor(hash) {
            return window.location.pathname + window.location.search + hash;
        }

        /* Going forward adds a history entry, so Back and Forward walk the
           steps and a copied URL reopens the one being looked at. */
        function pushState() {
            var url = urlFor(buildHash());
            if (url === urlFor(window.location.hash)) return;
            depth += 1;
            window.history.pushState({ wizardDepth: depth }, '', url);
        }

        function replaceState() {
            window.history.replaceState({ wizardDepth: depth }, '', urlFor(buildHash()));
        }

        function applyUrl(opts) {
            var state = readHash();
            if (!state) return;          // someone else's fragment
            /* Steps the URL says nothing about keep whatever was picked in
               them, so stepping back still shows the choice that was made
               from the step being returned to. The URL only ever describes
               the path up to the current step, so this cannot change it. */
            picks = state.picks.map(function (name, i) { return name || picks[i]; });
            step = state.step;
            render(opts);
            /* Rewrite a legacy or partial fragment to the canonical form
               without adding a history entry. A fragment pointing inside a
               step is left as it is, so the browser can still find it. */
            var canonical = buildHash();
            if (state.canonical && canonical !== (window.location.hash || '')) {
                replaceState();
            }
            if (state.target) {
                /* The browser could not reach it while the step was hidden. */
                window.setTimeout(function () {
                    state.target.scrollIntoView({ block: 'start', behavior: 'auto' });
                    window.scrollBy(0, -HEADER_OFFSET);
                }, reducedMotion() ? 0 : SLIDE_MS);
            }
        }

        // ---------------------------------------------------------------
        // Interaction
        // ---------------------------------------------------------------

        function choose(el) {
            var group = el.getAttribute('data-section-group');
            var name = el.getAttribute('data-section-name');
            var i = groups.indexOf(group);
            if (i < 0 || !sectionFor(group, name)) return;

            picks[i] = name;
            for (var j = i + 1; j < picks.length; j++) picks[j] = '';    // deeper steps are stale
            step = i + 1;
            pushState();
            render({ scroll: true, focus: true });
        }

        /* A click anywhere on a choice row counts as a click on its label,
           except on a control of its own: a link, or the button a {{< term >}}
           opens its definition with. */
        function selectorFrom(target) {
            if (!target || !target.closest) return null;
            if (target.closest('a, button')) return null;
            var el = target.closest('.section-selector');
            if (el) return el;
            var row = target.closest('.section-wizard__choice');
            return row ? row.querySelector('.section-selector') : null;
        }

        wizard.addEventListener('click', function (ev) {
            var el = selectorFrom(ev.target);
            if (!el) return;
            ev.preventDefault();
            choose(el);
        });

        wizard.addEventListener('keydown', function (ev) {
            if (ev.key !== 'Enter' && ev.key !== ' ' && ev.key !== 'Spacebar') return;
            var el = selectorFrom(ev.target);
            if (!el) return;
            ev.preventDefault();
            choose(el);
        });

        back.addEventListener('click', function () {
            if (step === 0) return;

            /* The step behind us is already in the browser's history, so hand
               the move to the browser: the entry we are on is dropped rather
               than another one stacked on top, and the browser's own Back
               button keeps meaning what it says. popstate does the render. */
            if (depth > 0) {
                window.history.back();
                return;
            }

            /* Nothing of ours behind us (someone opened a link to this step),
               so walk out to the previous step in place instead, leaving the
               history alone. */
            step -= 1;
            while (step > 0 && !picks[step - 1]) step -= 1;   // a step nothing was picked in
            replaceState();
            render({ scroll: true, focus: true });
        });

        window.addEventListener('popstate', function () {
            depth = (window.history.state && window.history.state.wizardDepth) || 0;
            applyUrl({ scroll: true });
        });
        window.addEventListener('hashchange', function () { applyUrl({ scroll: true }); });

        window.addEventListener('resize', syncHeight);
        if (window.ResizeObserver) {
            var ro = new ResizeObserver(syncHeight);
            panels.forEach(function (p) { ro.observe(p); });
        }
        window.addEventListener('load', syncHeight);

        // ---------------------------------------------------------------
        // First paint
        // ---------------------------------------------------------------

        applyUrl({ scroll: Boolean(window.location.hash) });
        /* Animate only after the initial state is on screen. */
        window.requestAnimationFrame(function () {
            window.requestAnimationFrame(function () { wizard.classList.add('is-ready'); });
        });
    });
}());
