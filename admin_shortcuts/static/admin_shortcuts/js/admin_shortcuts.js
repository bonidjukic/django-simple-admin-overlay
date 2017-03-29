document.addEventListener('DOMContentLoaded', function() {
  var adminShortcuts = (function () {

    var caret = document.getElementById('toggle-caret'),
        apps_container = document.getElementById('apps-container'),
        toolbar = apps_container.parentNode;

    function toggleLayer(e) {
      var state = toolbar.getAttribute('data-state');
      apps_container.style['display'] = (state == 'open') ? 'none'
                                                          : 'initial';
      toolbar.setAttribute('data-state', (state === 'open' ? 'closed'
                                                           : 'open'));
    }

    function init() {
      caret.addEventListener('click', function(e) {
        toggleLayer(e);
      }, false);
    }

    init();

    return;

  })();
});