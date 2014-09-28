$(document).ready(function() {
	var arr = document.getElementsByClassName("carousel-img");
	
	var curr = 0;
	
	arr[(arr.length+curr-1) % arr.length].className = "outfocus-left"; //because js does mod SHITTILY
	arr[curr % arr.length].className = "focus";
	arr[(curr+1) % arr.length].className = "outfocus-right";
	
	curr = 2;
	
	var loopFunc = function() {					
		//$("#carousel > div").each(function(index, elem) {
		for(var i = 0; i < $("#carousel > div").length; i++) {
			switch ($($("#carousel > div").get(i)).attr('class')) {
				case "focus":
					$($("#carousel > div").get(i)).switchClass("focus", "outfocus-left");
					break;
				case "outfocus-left":
					$($("#carousel > div").get(i)).switchClass("outfocus-left", "carousel-img");
					break;
				case "outfocus-right":
					$($("#carousel > div").get(i)).switchClass("outfocus-right", "focus");
					break;
				default:
					if(i == curr) {
						$($("#carousel > div").get(i)).switchClass("carousel-img", "outfocus-right");
					}
			}
			
		}//);
		curr++;
		if(curr >= arr.length) {
			curr = curr % arr.length
		}
	}
	
	setInterval(loopFunc, 7500);
});