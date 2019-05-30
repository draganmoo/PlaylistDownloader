$("#downloading_playlist > a").click(function () {
  var playlist_id = $(this).attr("playlist_id");
  slide_playlist_page(playlist_id);
});


function slide_playlist_page(playlist_id) {
  var selector = "#playlist_item_page[playlist_id=" + playlist_id + "]";
  var div_width = $(selector).width();

  $("#playlist_page").css({"opacity": 0, "visibility": "hidden", "display": "none"});
  $(selector).css({"display": "block", "right": -1 * div_width + "px"});
  $(selector).css("visibility", "visible")
            .animate({opacity: 1.0, right: "0px"}, 1500);
};
