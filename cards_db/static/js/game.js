$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);
    
    chatsock.onopen = function(event){
	
        chatsock.send(JSON.stringify(message));
    }


    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        
    };

    $("#chatform").on("submit", function(event) {

	var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        return false;
    });
});
