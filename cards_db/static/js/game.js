$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var gamesock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);
    
    gamesock.onmessage = function(message) {
	$('#searchModal').modal('hide');
	var msg = JSON.parse(message.data);        
	handle = msg.message.handle;        
	switch(handle) {
	case 'start':
	    console.log(msg.player_one.name);
	    $('#player_image').attr("src",decodeURI("images/"+msg.player_one.name+".jpg"));
            $('#player_name').text(msg.player_one.name);
            $('#test_matches').text("Matches: "+msg.player_one.test_matches);
	    $('#test_runs').text("Runs: "+msg.player_one.test_runs);
	    $('#test_bat_average').text("Avg: "+msg.player_one.test_bat_average);
  	    $('#test_highest_score').text("HS: "+msg.player_one.test_highest_score);
	    $('#test_hundreds').text("100s: "+msg.player_one.test_hundreds);
	    $('#test_fifties').text("50s: "+msg.player_one.test_fifties);
  	    $('#test_wickets').text("Wkts: "+msg.player_one.test_wickets);
	    $('#test_best_figs').text("BBM: "+msg.player_one.test_bbm_wkts+"/"+msg.player_one.test_bbm_runs);
	    $('#test_econ_rate').text("Econ Rate: "+msg.player_one.test_econ_rate);
  	    $('#test_no_of_five_wickets').text("5W: "+msg.player_one.test_no_of_five_wickets);
	    break;	
	}
	
    };

    $("#chatform").on("submit", function(event) {

	var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
        }
        gamesock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });

    $(".btn").on("submit", function(e) {

	e.preventdefault();
	var id = $(this).id;
	var handle = 'active';
	var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
        }
        gamesock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });

});
