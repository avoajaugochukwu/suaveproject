 jQuery(document).ready(function($) {

		$('.new_user_check').shake({/*direction: "up", distance: 50*/ times: 6, speed: 60});
		$('.shake-element').shake({/*direction: "up", distance: 50*/ times: 6, speed: 150});
		$('.general-login-shake').shake({times: 3, speed: 80});
		$('.new_user_check').delay(5000).slideUp(2000);
		if ($('.new_user_check').is(':visible')){
			$('.dashboard-button-panel').hide().delay(7000).slideDown(2000);
		}
		else {
			$('.dashboard-button-panel').hide().slideDown(500);
			$('.dashboard-button-panel').shake({times: 3, speed: 100});
		}

		$('.shaker').shake({times: 5, speed: 80});


		//Code for selecting male and female size
		$('.size-container').click(function() {
			$('.size-container').removeClass('radio_select_new_color');
			$(this).addClass('radio_select_new_color');
		});

		$('.fabric').click(function() {
			$('.fabric').removeClass('radio_select_new_color');
			$(this).addClass('radio_select_new_color');
		});



		// $('#thumbnails a').click(function(e) {
		// 	e.preventDefault();
		// 	e.stopPropagation();
		// 	// var value = $(this).closest('.fabric').find('input:radio[name=fabric]').val();
		// 	$(this).closest('.fabric').find('input:radio[name=fabric]').prop('checked', true);
		// 	$(this).lightBox().delay(3000);
		// });


		// $('#thumbnails a').lightBox();



	// Snippet to make span slide up and down image
	$(".photos").on("mouseenter", "li", showPhotos).on("mouseleave", "li", showPhotos);
	  
  function showPhotos() {
  	$(this).find("span").slideToggle();
  }

  // Snippet to make imput value change instantly in Page
  // use +$(..) to convert value to number
  $(document).ready(function() {
  $("#nights").on("keyup", function() {
    
    $("#nights-count").text($(this).val());
  });
});

});