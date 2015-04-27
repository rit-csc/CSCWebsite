$().ready(function() {

	var bioExists = function(anchorName) {
		var theAnchor = $(".position_anchors a[name='"+anchorName+"']");
		return !!(theAnchor[0]);
	};

	$(".position_quicklinks a").each(function() {
		var that = $(this);
		var anchorName = that.prop("href").split("\#")[1];
		if( !bioExists(anchorName) ){
			that.addClass("nobio");
			that.attr("title", "This officer hasn't filled in their bio yet!");
			that.removeAttr("href");
		}
	});
});