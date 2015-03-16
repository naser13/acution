$(".navbar-toggle").click(function(e) {
//        alert(className.getTagName);
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});