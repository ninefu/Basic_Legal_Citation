// LII Fundraiser JS functions
//Author: Wayne Weibel
//created: May 28, 2010

/** execute on script load **/
FUNDRAISER_SUFFIX = "june2011";
FUNDRAISER_COOKIENAME = "lii_fundraiser_" + FUNDRAISER_SUFFIX;
TRACKING_SCRIPT_URL = "http://www.law.cornell.edu/survey/fundraiser-tracking.php";
DONATION_URL = "http://www.law.cornell.edu/donors/" + FUNDRAISER_SUFFIX + "/donations.html";
LEARN_MORE_URL = "http://topics.law.cornell.edu/lii/about-lii";
LEARNED_MORE = false;


addLoadEvent(fundraiserOnLoad);

//##########################

/** main functions **/
function fundraiserOnLoad() {
	if (getCookie(FUNDRAISER_COOKIENAME) == null) { 
		setSplashOptions();
		showFundraiserSplash(); 
	}
	//else { alert("cookie present: " + entice_cookie); }
	
	//assign button actions
	$("#close-button").click(donateNo);
	$("#do-donation").click(donateYes);
	$("#learn-more").click(learnMore);
	
}

function showFundraiserSplash() {
	//alert("loading splashover");
	var xcoord = ($(window).width()/2) - ($("#fundraiser").width()/2) + $(window).scrollLeft() + "px";
	$("#fundraiser").css("left",xcoord);
	var ycoord = ($(window).height()/2) - ($("#fundraiser").height()/2) + $(window).scrollTop() + "px";
	$("#fundraiser").css("top",ycoord);
	$("#fundraiser").show("slow");
	
	$("#fundraiser-screen").css("width",$(window).width()+"px");
	$("#fundraiser-screen").css("height",$(window).height()+"px");
	$("#fundraiser-screen").show();
}

function donateNo() {
	setCookie(FUNDRAISER_COOKIENAME,"NO",30);
	closeSplashover();
	recordSplashOptions(false);
}

function donateYes() {
	setCookie(FUNDRAISER_COOKIENAME,"YES",365);
	closeSplashover();
	window.open(DONATION_URL,"donateYes");
	recordSplashOptions(true);
}

function learnMore() {
	window.open(LEARN_MORE_URL, "learnMore");
	LEARNED_MORE = true;
}

function closeSplashover() {
	$("#fundraiser").hide("fast");
	$("#fundraiser-screen").hide();
}

function setSplashOptions() {
	var message = [
		"<p class='message'>Help us keep legal information free for everyone.</p><p class='message cta'>Donate to LII</p>",
		"<p class='message'>Every month, your contributions enable 1 million people to access the law here, for free.</p><p class='message cta'>Show Your Support</p>",
		"<p class='message'>Support open access to legal information.</p><p class='message cta'>Donate to LII</p>",
		"<p class='message'>You allow LII to provide free, open access to the law.</p><p class='message cta'>Contribute Today</p>",
		"<p class='message'>Law without the media filter. One reason we're unbiased? We rely on individual donors.</p><p class='message cta'>Donate now.</p>",
		"<p class='message'>It's free, but not costless. Actual computer geeks keep up LII. Donate. We gotta pay the geeks.</p><p class='message cta'>Donate now.</p>",
	];
	
	var value = [
		"Help us keep legal information free for everyone. Donate to LII",
		"Every month, your contributions enable 1 million people to access the law here, for free. Show Your Support",
		"Support open access to legal information. Donate to LII",
		"You allow LII to provide free, open access to the law. Contribute Today.",
		"Law without the media filter. One reason we're unbiased? We rely on individual donors. Donate now.",
		"It's free, but not costless. Actual computer geeks keep up LII. Donate. We gotta pay the geeks. Donate now.",
	];
	
	var randnum = Math.floor( Math.random() * message.length); //random number between 0 and array.length - the indexes of the arrays
	var content = message[randnum] + "<input type='hidden'id='fundraiser-message' name='fundraiser-message' value='" + value[randnum] + "' />";
	
	$("#fundraiser-content").html(content);
}

function recordSplashOptions(donated) {
	params = "action=trackDonor&suffix=" + FUNDRAISER_SUFFIX;
	params += "&learned_more=" + LEARNED_MORE + "&donated=" + donated;
	params += "&message=" + $('#fundraiser-message').val();

	response = makeRequest(params, TRACKING_SCRIPT_URL);
	//alert(response);
}
//############################

/** utility functions **/
function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      oldonload();
      func();
    }
  }
}

function setCookie(c_name,value,expiredays) {
	var exdate=new Date();
	exdate.setDate(exdate.getDate()+expiredays);
	
	var cookievalue = c_name + "=" + escape(value);
	cookievalue += ((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
	cookievalue += ";path=/";
	document.cookie = cookievalue;
}

function getCookie(c_name) {
	if (document.cookie.length>0)
	  {
	  c_start=document.cookie.indexOf(c_name + "=");
	  if (c_start!=-1)
		{
		c_start=c_start + c_name.length+1;
		c_end=document.cookie.indexOf(";",c_start);
		if (c_end==-1) c_end=document.cookie.length;
		return unescape(document.cookie.substring(c_start,c_end));
		}
	  }
	return null;
}

function deleteCookie(name){
	//clear the cookie from browser memory
	setCookie(name,"",-1);
}

/*
	perform AJAX request to server
	- uses POST method
	- async = FALSE (script will wait for send to return)
	@param params - the variables and values to be sent to server script as a String
	@param URL - the url to the file to be accessed; full or root-relative
	@param update_element - id of, or the object to be updated with returned data
	@param overwrite - boolean; true - replace content of update_element, false - append to update_element
*/
function makeRequest(params, URL){
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

	if (xhr.status == 200) return xhr.responseText
	else alert("Error During AJAX Request to\n" + URL + "\n\nResponse Code: " + xhr.status + "</h1>" + xhr.responseText);
	
	return null
}
