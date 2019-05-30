$("#playlist_item_page > div > a").click(function () {
  var playlist_id = $(this).parent().parent().attr("playlist_id");
  slide_playlist_item_page(playlist_id);
});


function slide_playlist_item_page(playlist_id) {
  var selector = "#playlist_item_page[playlist_id=" + playlist_id + "]";
  var div_width = $("#playlist_page").width();

  $(selector).css({"opacity": 0, "visibility": "hidden", "display": "none"});
  $("#playlist_page").css({"display": "block", "left": -1 * div_width + "px"});
  $("#playlist_page").css("visibility", "visible")
            .animate({opacity: 1.0, left: "0px"}, 1500);
};
