$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var gamesock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);
    
    gamesock.onmessage = function(message) {
        var data = JSON.parse(message.data);
	handle = data['handle']        
	switch(handle) {
	case 'start':
            console.log(data);	    
	    $('#searchModal').modal('hide');
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

});


