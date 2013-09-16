

(function($){


$(document).ready(function (){

	$("#op-contacto a").click(function(e){
		e.preventDefault();
		$('html,body').animate({scrollTop: $("#contact-form").offset().top}, 800,"swing",function(){
			$("#inputName").focus()
		}); 		
	
	})
	
});




})(window.jQuery);