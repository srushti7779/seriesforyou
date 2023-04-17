jQuery(function ($) {
    $(".nav-item a")
        .click(function(e) {
            var link = $(this);

            var item = link.parent("li");
            
            if (item.hasClass("active1")) {
                item.removeClass("active1").children("a").removeClass("active1");
            } else {
                item.addClass("active1").children("a").addClass("active1");
            }

            if (item.children("ul").length > 0) {
                var href = link.attr("href");
                link.attr("href", "#");
                setTimeout(function () { 
                    link.attr("href", href);
                }, 300);
                e.preventDefault();
            }
        })
        .each(function() {
            var link = $(this);
            if (link.get(0).href === location.href) {
                link.addClass("active1").parents("li").addClass("active1");
                return false;
            }
        });
});