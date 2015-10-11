// JavaScript Document
//LII Survey Javascript functions

/** execute on script load **/
addLoadEvent(surveyOnLoad);

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
	return "";
}

function deleteCookie(name){
	//clear the cookie from browser memory
	setCookie(name,"",-1);
}
//##########################

/** main functions **/
function surveyOnLoad(){
	if (SURVEY_TYPE == "exit" || SURVEY_TYPE == "thank you") {
		document.getElementById("survey-close-button").onclick = function e() { window.close(); } 
	}
	else { document.getElementById("survey-close-button").onclick = declinedSurvey; }
	
	if (SURVEY_TYPE != "thank you") { document.getElementById("survey-submit").onclick = submitSurvey; }
	
	showSurvey();
}

function submitSurvey() {
	if (SURVEY_TYPE != "exit") { 
		setCookie(SURVEY_COOKIENAME,"submitted",365);
	}
	if (SURVEY_TYPE == "enter") {
		alert("Thank You\n\nwhen you are done at LII, please take a moment to answer the follow up questions in the new window or tab.");
	}
	doSubmit(this.form);//this = element calling this function 
	closeSurvey(); 
}

function declinedSurvey() {
	setCookie(SURVEY_COOKIENAME,"declined",30);
	document.getElementById("user_market_survey").value = "declined";
	doSubmit(document.forms["lii-user-survey"]);
	closeSurvey();
}

function doSubmit(theform){
	//do submit request
	var mywindow = window.open('','mywin','');
	theform.target = 'mywin';
	theform.submit();

	if (getCookie(SURVEY_COOKIENAME) == "declined") mywindow.close();
	
	window.focus();
	if (SURVEY_TYPE == "enter" || SURVEY_TYPE == "prompt") { window.location.reload(true); }
}

function showSurvey(){
	$("#survey-screen").css("width",$(window).width()+"px");
	$("#survey-screen").css("height",$(window).height()+"px");
	$("#survey-screen").show();
	
	$("#lii-survey").css("width",($(window).width()*.8) + "px");
	
	var xcoord = ($(window).width()/2) - ($("#lii-survey").width()/2) + "px";
	var ycoord = "50px";
	if ($(window).height() > $("#lii-survey").height()) { 
		ycoord = ($(window).height()/2) - ($("#lii-survey").height()/2) + "px"; 
	}
	$("#lii-survey").css("left",xcoord);
	$("#lii-survey").css("top",ycoord);
	$("#lii-survey").show("slow");
}

function closeSurvey(){
	$("#survey-screen").hide(0,function(){ $(this).remove(); });
	$("#lii-survey").hide('fast',function(){ $(this).remove(); });
}