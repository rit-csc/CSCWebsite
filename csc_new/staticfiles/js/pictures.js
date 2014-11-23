
window.addEventListener("load", formatRows);

function formatRows(){

	// get all rows.
	var rows = document.getElementsByClassName('row');

	for(var i = 0; i < rows.length; i++){

		// get all (both) pic divs in this row.
		var children = rows[i].getElementsByClassName('pic');

		// if this row has 2 pictures in it, standardize the height.
		// otherwise, it doesn't matter.
		if(children.length > 1){
			
			// change height of shorter element to match that of
			// taller element.

			var h0 = children[0].clientHeight;
			var h1 = children[1].clientHeight;
			if(h0 > h1){
				rows[i].style.height = h0 + "px";
			}else{
				rows[i].style.height = h1 + "px";
			}

		}
	}

}
