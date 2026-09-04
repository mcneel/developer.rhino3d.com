// Hover preview tooltip for rhino-command shortcode links
(function() {
  'use strict';

  function addCommandTooltips() {
    var links = document.querySelectorAll('.unfurl-link[data-tooltip-href]');

    links.forEach(function(link) {
      if (link.dataset.tooltipInitialized) {
        return;
      }
      link.dataset.tooltipInitialized = 'true';

      var tooltip = document.createElement('span');
      tooltip.classList.add('cmd_tooltip');
      tooltip.classList.add('arrow-top');

      var iframe = document.createElement('iframe');
      iframe.src = link.dataset.tooltipHref;
      iframe.style.width = '100%';
      iframe.style.height = '100%';
      iframe.style.border = 'none';
      tooltip.appendChild(iframe);

      link.appendChild(tooltip);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addCommandTooltips);
  } else {
    addCommandTooltips();
  }
})();
