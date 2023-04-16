"use strict";
// Event 'Click'
$("h1").click(function (e) {
    console.log("There was a click!");
});

// Grap multiple event
$("li").click(function (e) {
    console.log("any li was clicked!");
});

// use 'this' key word
$("h1").dblclick(function (e) {
    // This means any object we selected, here is 'h1'
    $(this).text("Double click is triggered");
    console.log($(this).text());
});

// Key press
$("input")
    .eq(0)
    .keypress(function (event) {
        // Each key has number code that stored in event.which()
        // 'enter' = 13
        if (event.which === 13) {
            console.log(event);
            $("h3").toggleClass("turnBlue");
        }
    });

// on() method essentially act like addEventListener
$("h1").on("dblclick", function () {
    $(this).toggleClass("turnBlue");
});

// grap mouseEnter using on()
$("h1").on("mouseenter", function () {
    $(this).toggleClass("turnBlue");
});

// event animation
$("input")
    .eq(1)
    .on("click", function () {
        // grap every thing in the `.container` class
        // fadeOut(x), make selector disappear in x milleseconds
        // $(".container").fadeOut(1000);
        $(".container").slideUp(1000);
    });
