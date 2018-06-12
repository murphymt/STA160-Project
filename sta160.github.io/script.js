$(document).ready(function() {
    
    

    
    /* Navigation scroll */
    $(function() {
      $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top
            }, 1000);
            return false;
          }
        }
      });
    });
    
    GMaps.geocode({
        div:'.map',
  address: $('#address').val(),
  callback: function(results, status) {
    if (status == 'OK') {
      var latlng = results[0].geometry.location;
      map.setCenter(latlng.lat(), latlng.lng());
      map.addMarker({
        lat: latlng.lat(),
        lng: latlng.lng()
      });
    }
  }
});

});