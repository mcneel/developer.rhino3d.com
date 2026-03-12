// Copy to clipboard functionality for code blocks
(function() {
  'use strict';

  // Add copy buttons to all code blocks
  function addCopyButtons() {
    // Find all <pre> elements that contain <code>
    var codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(function(codeBlock) {
      var pre = codeBlock.parentElement;
      
      // Skip if already has a copy button
      if (pre.querySelector('.copy-code-button')) {
        return;
      }
      
      // Make sure pre has relative positioning for button placement
      pre.style.position = 'relative';
      
      // Create copy button
      var copyButton = document.createElement('button');
      copyButton.className = 'copy-code-button';
      copyButton.type = 'button';
      copyButton.setAttribute('aria-label', 'Copy code to clipboard');
      copyButton.innerHTML = '<i class="fas fa-copy"></i>';
      
      // Add click handler
      copyButton.addEventListener('click', function() {
        var code = codeBlock.innerText;
        
        // Use clipboard API if available
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(code).then(function() {
            showCopySuccess(copyButton);
          }).catch(function(err) {
            console.error('Failed to copy: ', err);
            fallbackCopy(code, copyButton);
          });
        } else {
          fallbackCopy(code, copyButton);
        }
      });
      
      // Insert button at the beginning of the pre element
      pre.insertBefore(copyButton, pre.firstChild);
    });
  }
  
  // Fallback copy method for older browsers
  function fallbackCopy(text, button) {
    var textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-9999px';
    textArea.style.top = '0';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
      document.execCommand('copy');
      showCopySuccess(button);
    } catch (err) {
      console.error('Fallback copy failed: ', err);
    }
    
    document.body.removeChild(textArea);
  }
  
  // Show success feedback
  function showCopySuccess(button) {
    var originalHTML = button.innerHTML;
    button.innerHTML = '<i class="fas fa-check"></i>';
    button.classList.add('copied');
    
    setTimeout(function() {
      button.innerHTML = originalHTML;
      button.classList.remove('copied');
    }, 2000);
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addCopyButtons);
  } else {
    addCopyButtons();
  }
})();
