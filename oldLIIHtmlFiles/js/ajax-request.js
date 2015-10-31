// JavaScript Document
/*
	perform AJAX request to server
	- uses POST method
	- async = FALSE (script will wait for send to return)
	@param params - the variables and values to be sent to server script
	@param URL - the url to the file to be accessed; full or root-relative
	@param update_element - id of, or the object to be updated with returned data
	@param overwrite - boolean; true - replace content of update_element, false - append to update_element
*/
function makeRequest(params, URL, update_element, overwrite){
	var xhr = false;
	if (window.XMLHttpRequest) xhr = new XMLHttpRequest();
	else if (window.ActiveXObject){
		try { xhr = new ActiveXObject("Microsoft.XMLHTTP"); }
		catch(e){}
	}

	if (!xhr) return alert('Unable to create XMLHttpRequest');
	xhr.open('POST', URL, false);
	//Send the proper header information along with the request
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.setRequestHeader("Content-length", params.length);
	xhr.setRequestHeader("Connection", "close");
	
	//alert("sending request: " + params);
	xhr.send(params);

	if (xhr.status == 200) {
		if (update_element != null) {
			var output = (typeof(update_element) == "object") ? update_element : document.getElementById(update_element);
			if (overwrite) output.innerHTML = xhr.responseText;
			else output.innerHTML += xhr.responseText;
		}
		else document.write( xhr.responseText );
	}
	else document.body.innerHTML = "<h1>Response Code: " + xhr.status + "</h1>" + xhr.responseText;
}
