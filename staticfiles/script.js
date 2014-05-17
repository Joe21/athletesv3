// button functionality
function meME(){
	var el = $('#music-container');
	var player = $('#audio-player');
	var body = $('body');
	var block = $('.block-container');

	if(stealth === true){
		el.append("<audio id='audio-player' src='https://s3.amazonaws.com/samplepublicbucket/me-unchartered_worlds_cutup.mp3' controls autoplay>");
		block.hide();
		$('body').css("background-image", "url('/static/n7.jpg')");
		stealth = false;
	} else {
		el.empty();
		block.show();
		$('body').css("background-image", "url('/static/football.jpg')");
		stealth = true;
	}
}

function dorkyglow(){
	var option = {
		x: 0,
		y: 0,
		radius: 10,
		color: 'red'
	};
	$('h2').textShadow(option);
}

// Global variable
var stealth = true;

// On window load
$(function(){
	$('#crazy-button').on('click', meME);
});