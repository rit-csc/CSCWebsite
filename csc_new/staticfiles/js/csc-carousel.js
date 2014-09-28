$(document).ready(function() {
	var arr = $("#carousel > div");
	
	var curr = 0;
	
	$($("#carousel > div").get((arr.length+curr-1) % arr.length)).switchClass("carousel-img", "outfocus-left");
	$($("#carousel > div").get(curr)).switchClass("carousel-img", "focus");
	$($("#carousel > div").get((arr.length+curr+1) % arr.length)).switchClass("carousel-img", "outfocus-right");
	
	var loopFunc = function() {					
		//$("#carousel > div").each(function(index, elem) {
/*		for(var i = 0; i < $("#carousel > div").length; i++) {
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
			
		}//);*/
		$($("#carousel > div").get((arr.length+curr-1) % arr.length)).switchClass("outfocus-left", "carousel-img");
		$($("#carousel > div").get(curr)).switchClass("focus", "outfocus-left");
		$($("#carousel > div").get((arr.length+curr+1) % arr.length)).switchClass("outfocus-right", "focus");
		$($("#carousel > div").get((arr.length+curr+2) % arr.length)).switchClass("carousel-img", "outfocus-right");
		
		curr++;
		if(curr >= arr.length) {
			curr = curr % arr.length
		}
	}
	
	setInterval(loopFunc, 7500);
});