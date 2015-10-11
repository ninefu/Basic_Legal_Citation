//LII Enticement JS functions
//author Wayne Weibel
//created March 4, 2010

var ENTICE_COOKIENAME = "";
var ENTICE_ONYESDEST = "";

function enticement(cookieName, onYesDestination) {
	ENTICE_COOKIENAME = cookieName;
	ENTICE_ONYESDEST = onYesDestination;
	var entice_cookie = getCookie(ENTICE_COOKIENAME);
	if (entice_cookie == ""){ showEnticeSplash(); }
	//else { alert("cookie present: " + entice_cookie); }
	
	//assign entice-buttons actions
	$("#entice-notever").click(donateNever);
	$("#entice-maybelater").click(donateLater);
	$("#entice-yesnow").click(donateNow);
}

function showEnticeSplash() {
	//alert("loading splashover");
	var xcoord = ($(window).width()/2) - ($("#enticement").width()/2) + "px";
	$("#enticement").css("left",xcoord);
	var ycoord = ($(window).height()/2) - ($("#enticement").height()/2) + "px";
	$("#enticement").css("top",ycoord);
	$("#enticement").show("slow");
	
	$("#entice-screen").css("width",$(window).width()+"px");
	$("#entice-screen").css("height",$(window).height()+"px");
	$("#entice-screen").show();
}

function donateNever() {
	setCookie(ENTICE_COOKIENAME,"nonever",90);
	closeSplashover();
}

function donateLater() {
	setCookie(ENTICE_COOKIENAME,"maybelater");
	closeSplashover();
}

function donateNow() {
	setCookie(ENTICE_COOKIENAME,"yesnow",60);
	closeSplashover();
	window.open(ENTICE_ONYESDEST,"onYesWindow");
}

function closeSplashover() {
	$("#enticement").hide("fast");
	$("#entice-screen").hide();
}


function setCookie(c_name,value,expiredays)
{
var exdate=new Date();
exdate.setDate(exdate.getDate()+expiredays);
document.cookie=c_name+ "=" +escape(value)+
((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
}

function getCookie(c_name)
{
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