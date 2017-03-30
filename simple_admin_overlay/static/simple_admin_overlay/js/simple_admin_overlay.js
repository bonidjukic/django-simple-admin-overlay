document.addEventListener('DOMContentLoaded', function() {
  var adminOverlay = (function () {

    var caret = document.getElementById('toggle-caret'),
        apps_container = document.getElementById('apps-container'),
        overlay = apps_container.parentNode;

    function toggleOverlay(e) {
      var state = overlay.getAttribute('data-state');
      apps_container.style['display'] = (state == 'open') ? 'none'
                                                          : 'initial';
      overlay.setAttribute('data-state', (state === 'open' ? 'closed'
                                                           : 'open'));
    }

    function init() {
      caret.addEventListener('click', function(e) {
        e.preventDefault();
        toggleOverlay(e);
      }, false);
    }

    init();

    return;

  })();
});