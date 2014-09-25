function updateNavBar(){
	var menu = location.pathname;
	if (menu == "/") {
    	document.getElementById("index").setAttribute("class", "active");
	} else if (menu == "/about") {
    	document.getElementById("about").setAttribute("class", "active");
	} else if (menu == "/contact") {
    	document.getElementById("contact").setAttribute("class", "active");
	} else if (menu == "/projects") {
    	document.getElementById("projects").setAttribute("class", "active");
	} else if (menu == "/calendar") {
    	document.getElementById("calendar").setAttribute("class", "active");
	} else if (menu == "/resources") {
    	document.getElementById("resources").setAttribute("class", "active");
	} else if (menu == "/pictures") {
		document.getElementById("pictures").setAttribute("class", "active");
	}
}



function setActive(id){
    document.getElementById(id).setAttribute("class", "active");
}