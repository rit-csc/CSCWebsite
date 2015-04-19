function updateStyle() {
	var menu = location.pathname;
	if (menu == "/") {
    	setActive("index");
	} else if (menu.match("/about(/)?")) {
    	setActive("about");
	} else if (menu.match("/projects(/)?")) {
    	setActive("projects");
	} else if (menu.match("/calendar(/)?")) {
    	setActive("calendar");
	} else if (menu.match("/resources(/)?")) {
    	setActive("resources");
	} else if (menu.match("/pictures(/)?")) {
		setActive("pictures");
	}
}

function setActive(id) {
    elem = document.getElementById(id);
    $(elem).addClass("active");
}

$(document).ready(function() {

	var manageStickyNav = (function() {

		var navbar = $("#csc-navbar").get(0);

		var navPlaceholder = $( "<div id=\"navPlaceholder\"></div>" );
		navPlaceholder.insertBefore($(navbar));

		var navHeight = $(navbar).innerHeight();

		var makeSticky = function() {
			navbar.style.position = "fixed";
			navbar.style.top = "0px";

			// this is the effective height of the navbar
			navPlaceholder.css("marginBottom", navHeight + "px");
		};

		var removeSticky = function() {
			navbar.style.position = "static";
			navbar.style.top = navPlaceholder.height();
			navPlaceholder.css("marginBottom", "0px");
		};

		return function() {
			var pos = navPlaceholder.get(0).getBoundingClientRect().bottom;

			if(pos <= 0){
				makeSticky();
			} else {
				removeSticky();
			}
		};
	}());

	window.addEventListener("scroll", function() {
		manageStickyNav();
	});
});
