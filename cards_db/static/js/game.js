$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var gamesock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);
    console.log("Connection established");
    gamesock.onmessage = function(message) {
	$('#searchModal').modal('hide');
	var msg = JSON.parse(message.data);
	handle = msg.message.handle;        
	switch(handle) {
	case 'start':
	    $.cookie("handle", handle);
	    if (msg.message.user_one == $.cookie("username")){
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
	    $.cookie("status", msg.message.player_one_turn);
	    console.log($.cookie("status"));
	    }
	    else{
	    $('#player_image').attr("src",decodeURI("images/"+msg.player_two.name+".jpg"));
            $('#player_name').text(msg.player_two.name);
            $('#test_matches').text("Matches: "+msg.player_two.test_matches);
	    $('#test_runs').text("Runs: "+msg.player_two.test_runs);
	    $('#test_bat_average').text("Avg: "+msg.player_two.test_bat_average);
  	    $('#test_highest_score').text("HS: "+msg.player_two.test_highest_score);
	    $('#test_hundreds').text("100s: "+msg.player_two.test_hundreds);
	    $('#test_fifties').text("50s: "+msg.player_two.test_fifties);
  	    $('#test_wickets').text("Wkts: "+msg.player_two.test_wickets);
	    $('#test_best_figs').text("BBM: "+msg.player_two.test_bbm_wkts+"/"+msg.player_one.test_bbm_runs);
	    $('#test_econ_rate').text("Econ Rate: "+msg.player_two.test_econ_rate);
  	    $('#test_no_of_five_wickets').text("5W: "+msg.player_two.test_no_of_five_wickets);
	    $.cookie("status", msg.message.player_two_turn);
	    console.log($.cookie("status"));
	    } 
	    break;
	case 'active':
            $.cookie("handle", handle);
            $('#myModal').modal('show');
	    console.log(msg);              
            break;
	}
		
    };

    $(document).ready(function(){
        $(".btn-info").on("click",function(e) {
            e.preventDefault();
	    console.log("Entering button");
	
            if($.cookie("status" == true)){
                var id = this.id;
                var handle = 'active';
                var message = {
            	    handle: handle,
                    id: id,
            }
	    console.log(id);
            gamesock.send(JSON.stringify(message));
        }
        return false;
    });
});




});


