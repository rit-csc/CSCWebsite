window.onload = function(){
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
