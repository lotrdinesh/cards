$(document).ready(function(){
	function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      	}
 	return cookieValue;
	}

	$(".btn-lg").click(function(e){
		e.preventDefault();
		var csrftoken = getCookie('csrftoken');
		var tr = $(this).html();
		var str = tr.split(":");
	        var parameter=str[0];
		var value = str[1];
		$.ajax({
		type:"POST", 
		url: window.location.href,
		data : {
		csrfmiddlewaretoken: csrftoken,		
		param: parameter,	
		value: value
		},
		success : function (json){
		str = json['name'];
		console.log(str);
		$('#image').attr('src', '../images/'+json['name']+'.jpg');
		$('#name').html(json['name']);
		$('#Matches').html('Matches: '+json['test_matches']);
		$('#Runs').html('Runs: '+json['test_runs']);
		$('#Avg').html('Avg: '+json['test_bat_average']);
		$('#Highest').html('Highest Score: '+json['test_highest_score']);
		$('#100s').html('100s: '+json['test_hundreds']);
		$('#50s').html('50s: '+json['test_fifties']);
		$('#Wickets').html('Wkts: '+json['test_wickets']);
		$('#BBM').html('BBM: '+json['test_BBM_wkts']+'/'+json['test_BBM_runs']);
		$('#Economy').html('100s: '+json['test_econ_rate']);
		$('#5W').html('5W: '+json['test_no_of_five_wickets']);
		},
		failure : function (xhr, errmsg, err){
		console.log(xhr.status 	+ ":" + xhr.responseText);
		}
		});
	
	});
});
