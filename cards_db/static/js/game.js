$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var gamesock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);
    var timeinterval;           
    var time = 15;
    gamesock.onmessage = function(message) {
	$('#searchModal').modal('hide');
	var msg = JSON.parse(message.data);
	handle = msg.message.handle;        
	switch(handle) {
	case 'start':
	    $.cookie("handle", handle);
	    if (msg.message.user_one == $.cookie("username")){
	    $('#own_name').text(msg.message.user_one);
	    $('#opponent_name').text(msg.message.user_two);
	    $('#player_image').attr("src",encodeURI("/static/images/"+msg.player_one.name+".jpg"));
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
	    $('#own_score').text(msg.message.user_one_score);
	    $('#opponent_score').text(msg.message.user_two_score);
	    $.cookie("status", msg.message.player_one_turn);
	    }
	    else{
	    $('#own_name').text(msg.message.user_two);
	    $('#opponent_name').text(msg.message.user_one);
	    $('#player_image').attr("src",encodeURI("/static/images/"+msg.player_two.name+".jpg"));
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
	    $('#own_score').text(msg.message.user_two_score);
	    $('#opponent_score').text(msg.message.user_one_score);
	    $.cookie("status", msg.message.player_two_turn);
	    }
	    console.log(msg); 
	    break;
	case 'active':
            $.cookie("handle", handle);
	    if (msg.message.player_one_turn == true){
	    $('#myModal').find('.modal-title').html(msg.message.user_one+" wins");
	    $('#result_win').attr("src",encodeURI("/static/images/"+msg.message.player_one+".jpg"));
	    $('#result_loss').attr("src",encodeURI("/static/images/"+msg.message.player_two+".jpg"));
	    }
	    else{
	    $('#myModal').find('.modal-title').html(msg.message.user_two+" wins");
	    $('#result_win').attr("src",encodeURI("/static/images/"+msg.message.player_two+".jpg"));
	    $('#result_loss').attr("src",encodeURI("/static/images/"+msg.message.player_one+".jpg"));
	    } 	
	    $.removeCookie("myClock");
	    clearInterval(timeinterval);
            $('#myModal').modal('show');
	    break;
	case 'next':
	    $.cookie("handle", handle);
	    if (msg.message.user_one == $.cookie("username")){
	    $('#player_image').attr("src","/static/images/"+msg.player_one.name+".jpg");
            $('#player_name').text(msg.player_one.name);
	    $('#test_matches').text("Matches: "+msg.player_one.test_matches);
	    $('#test_runs').text("Runs: "+msg.player_one.test_runs);
	    $('#test_bat_average').text("Avg: "+msg.player_one.test_bat_average);
  	    $('#test_highest_score').text("HS: "+msg.player_one.test_highest_score);
	    $('#test_hundreds').text("100s: "+msg.player_one.test_hundreds);
	    console.log(msg.player_one.test_fifties);
            $('#test_fifties').text("50s: "+msg.player_one.test_fifties);
  	    $('#test_wickets').text("Wkts: "+msg.player_one.test_wickets);
	    $('#test_best_figs').text("BBM: "+msg.player_one.test_bbm_wkts+"/"+msg.player_one.test_bbm_runs);
	    $('#test_econ_rate').text("Econ Rate: "+msg.player_one.test_econ_rate);
  	    $('#test_no_of_five_wickets').text("5W: "+msg.player_one.test_no_of_five_wickets);
	    $.cookie("status", msg.message.player_one_turn);
	    $('#own_score').text(msg.message.user_one_score);
	    $('#opponent_score').text(msg.message.user_two_score);
	    $.cookie("status", msg.message.player_one_turn);
	    }
	    else{
	    $('#player_image').attr("src",decodeURI("/static/images/"+msg.player_two.name+".jpg"));
            $('#player_name').text(msg.player_two.name);
            $('#test_matches').text("Matches: "+msg.player_two.test_matches);
	    $('#test_runs').text("Runs: "+msg.player_two.test_runs);
	    $('#test_bat_average').text("Avg: "+msg.player_two.test_bat_average);
  	    $('#test_highest_score').text("HS: "+msg.player_two.test_highest_score);
	    $('#test_hundreds').text("100s: "+msg.player_two.test_hundreds);
	    console.log(msg.player_two.test_fifties);
            $('#test_fifties').text("50s: "+msg.player_two.test_fifties);
  	    $('#test_wickets').text("Wkts: "+msg.player_two.test_wickets);
	    $('#test_best_figs').text("BBM: "+msg.player_two.test_bbm_wkts+"/"+msg.player_one.test_bbm_runs);
	    $('#test_econ_rate').text("Econ Rate: "+msg.player_two.test_econ_rate);
  	    $('#test_no_of_five_wickets').text("5W: "+msg.player_two.test_no_of_five_wickets);
	    $.cookie("status", msg.message.player_two_turn);
	    $('#own_score').text(msg.message.user_two_score);
	    $('#opponent_score').text(msg.message.user_one_score);
	    $.cookie("status", msg.message.player_two_turn);
	    }
	    $.removeCookie("myClock");
	    clearInterval(timeinterval);
	    console.log(msg); 
	    break;
	    case 'timeout':
	    $.cookie("handle", handle);
	    if (msg.message.player_one_turn == true){
	    $('#timeout_title').html(msg.message.user_two+" Timed Out!!");
	    $('#timeout_win').html(msg.message.user_one+" Gets the point!!");
	    $('#timeout_score').html(msg.message.user_one_score + "-" + msg.message.user_two_score );
	    }
	    else{
	    $('#timeout_title').html(msg.message.user_one+" Timed Out!!");
	    $('#timeout_win').html(msg.message.user_two+" Gets the point!!");
	    $('#timeout_score').html(msg.message.user_two_score + "-" + msg.message.user_one_score );
	    } 	
            $('#timeOutModal').modal('show');
	    $.removeCookie("myClock");
	    clearInterval(timeinterval);
	    console.log("Entering timeout");
	    console.log(msg);
	    break; 
	}
	if ($.cookie("myClock")!=null){
	    var deadline = $.cookie("myClock");	
	}
	else{
	    var deadline = new Date();
	    deadline.setTime(deadline.getTime() +(time*1000));
	    $.cookie("myClock", deadline)
	}

        $('#clockdiv').initializeClock(deadline);
	
    };

    gamesock.onclose = function(){
	if ($.cookie("myClock")!=null){$.removeCookie("myClock");}
	if ($.cookie("handle")!=null){$.removeCookie("handle");}
	if ($.cookie("label")!=null){$.removeCookie("label");}
	if ($.cookie("username")!=null){$.removeCookie("username");}
    };

    gamesock.onerror = function(event){
	alert(event.data);
    };



    $(document).ready(function(){
	$('#searchModal').modal({backdrop:'static'});
    	$('#searchModal').modal('show');
	
	   
	$(".btn-info").on("click",function(e) {
            e.preventDefault();
	    console.log($.cookie("status"));	
            if($.cookie("status") == "true"){
                var id = this.id;
                var handle = 'active';
                var message = {handle: handle,id: id}
            	gamesock.send(JSON.stringify(message));
            }
        return false;
    	});

	$.getTimeRemaining = function(endtime) {
  	    var t = Date.parse(endtime) - Date.parse(new Date());
  	    var seconds = Math.floor((t / 1000) % 60);
  	    return {'total': t, 'seconds': seconds};
    	};

    	$.fn.initializeClock =function (endtime) {

  	    $.updateClock = function() {
    	    	var t = $.getTimeRemaining(endtime);
		
		if (t.seconds < 0) {
		    console.log("Timed Out!!");
		    clearInterval(timeinterval);
		    $('.radial-progress-cover').attr('stroke-dashoffset','0em');
		    $.removeCookie("myClock");
		    if ($.cookie("status") == "true"){
		        var handle = 'timeout';
                        var message = {handle: handle};
            	        gamesock.send(JSON.stringify(message));
		    }
	    	}
	    	else{
		    $('.radial-progress-cover').attr('stroke-dashoffset', 9.4245*(t.seconds/time)+'em');
	    	}
	    }
  	    $.updateClock();
  	    timeinterval = setInterval($.updateClock, 1000);
        };

    });

    $(function(){
    	$('#myModal').on('show.bs.modal', function(){
    	    var myModal = $(this);
            clearTimeout(myModal.data('hideInterval'));
            myModal.data('hideInterval', setTimeout(function(){myModal.modal('hide');}, 2000));
        });

	$('#timeOutModal').on('show.bs.modal', function(){
    	    var myModal = $(this);
            clearTimeout(myModal.data('hideInterval'));
            myModal.data('hideInterval', setTimeout(function(){myModal.modal('hide');}, 5000));
        });
    });

    $(function(){
    	$('#myModal').on('hide.bs.modal', function(){
	    
    	    if($.cookie("status") == "true"){
	    var handle = 'next';     
	    var message = {handle: handle};
            gamesock.send(JSON.stringify(message));
	    }
        });
    	$('#timeOutModal').on('hide.bs.modal', function(){
	    
    	    if($.cookie("status") == "true"){
	    var handle = 'next';     
	    var message = {handle: handle};
            gamesock.send(JSON.stringify(message));
	    }
        });
    });
});


