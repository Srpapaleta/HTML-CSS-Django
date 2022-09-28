/**
 * @file
 * Home page events.
 */


/**
 * Open modal event.
 */
$('.td-estado').on('click', function () {
  // Change data.
  let changeState = $(this).attr('state-id') == 'available' ?
    'Ocupado' : 'Disponible';
  $("#change-state").text(changeState);

  $("#confirm-state-change").attr('apt-id', $(this).attr('apt-id'));
  $("#confirm-state-change").attr('apt-state', $(this).attr('state-id') == 'available' ?
    'unavailable' : 'available'
  );

  // Open modal.
  $("#confirmation-modal-container").css("display","block");
  $("#confirmation-modal").css("display","block");
});

/**
 * Close modal event.
 */
$(".cancel-modal").on('click', function () {
  // Hide modal.
  $("#confirmation-modal-container").fadeOut();
  $("#confirmation-modal").fadeOut();
});

/**
 * Update apartament state.
 */
$(".confirm-state-change").on('click', function () {
  let id = $(this).attr('apt-id');
  let state = $(this).attr('apt-state');

  if (typeof id != "undefined" && typeof state != "undefined") {
    fetch('/update/apartment/' + id + '/state/' + state)
      .then((response) => response.json())
      .then((data) => {
        if (data.status == 1) {
          window.location.href = "/home";
        }else{
          console.log("Error!")
        }
      });
  }
});


