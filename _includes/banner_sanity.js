$.ready(function() 
{ 
	var splitPath = window.location.pathname.split("/");
	var nonWipURL = "/" + splitPath.splice(2,splitPath.length-2).join("/");

	$.get(nonWipURL).fail(function () 
	{ 
		var $aTag = $("div.version-banner > a");
		$aTag.remove();
	});
});
