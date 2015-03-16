jQuery(document).ready(function($) {
		
		// $('.nav-tabs ul li').click(function(e))
		// {
		// 	e.preventDefault();
		// }
		$('.new-register').shake({/*direction: "up", distance: 50*/ times: 6, speed: 60});

		$('.new-register').delay(5000).slideUp(2000);
		if ($('.new-register').is(':visible')){
			$('.client-dashboard-panel').hide().delay(7000).slideDown(2000);
		}
		else {
			$('.client-dashboard-panel').hide().slideDown(1000);
			$('.client-dashboard-panel').shake({times: 6, speed: 100});
		}

		$('.client-order-form-male, .client-order-form-female').hide();

		// $('#id_sex').click(function() {
		// 	if ($('.client-order-form-female').is(':visible')) {
		// 		$('.client-order-form-female').hide();
		// 	};
		// 	if ($('.client-order-form-male').is(':visible')) {
		// 		$('.client-order-form-male').hide();
		// 	};
		// });

		//make it not function if it is checked
		$('#id_sex_0').click(function() {
			if ($('.client-order-form-male').is(':visible')) {
				$('.client-order-form-male').hide(1000);
			};
			$('.client-order-form-female').slideToggle(1000);
		});

		$('#id_sex_1').click(function() {
				if ($('.client-order-form-female').is(':visible')) {
				$('.client-order-form-female').hide(1000);
			};
			$('.client-order-form-male').slideToggle(1000);
		});
});