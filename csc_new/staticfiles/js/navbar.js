window.onscroll =
	function updatePos(){
		var navbar = document.getElementById('csc-navbar');
		var carousel = document.getElementById('carousel');

		var pos = carousel.getBoundingClientRect().bottom;

		if(pos <= 0){
			navbar.style.position = "fixed";
			navbar.style.top = "0px";

			carousel.style.marginBottom = String(
				Number(document.getElementByClassName("space")[0].style.height) +
				Number(navbar.style.height))
				+ "px";
		}else{
			navbar.style.position = "static";
			navbar.style.top = carousel.style.height;
			carousel.style.marginBottom = "0px";
		}
	};

function updateStyle(){
	var menu = location.pathname;
	if (menu == "/") {
    	setActive("index");
	} else if (menu == "/about") {
    	setActive("about");
	} else if (menu == "/contact") {
    	setActive("contact");
	} else if (menu == "/projects") {
    	setActive("projects");
	} else if (menu == "/calendar") {
    	setActive("calendar");
	} else if (menu == "/resources") {
    	setActive("resources");
	} else if (menu == "/pictures") {
		setActive("pictures");
	}
}

function setActive(id){
    elem = document.getElementById(id);
    curr = elem.getAttribute("class");
    elem.setAttribute("class", curr+" active");
}
