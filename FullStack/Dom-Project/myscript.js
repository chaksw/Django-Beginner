// Restart Game Button
"use strict";
// use #id to grab attribute
const btnRestart = document.querySelector("#b");
// Grabs all the squares
// use directly tag name to grab attribute
const squares = document.querySelectorAll("td");

// Clear all the squares
const clearBoard = function () {
    for (let i = 0; i < squares.length; i++) {
        squares[i].textContent = "";
    }
};
// Check the sqaure marker
const changeMarker = function () {
    this.textContent === ""
        ? (this.textContent = "X")
        : this.textContent === "X"
        ? (this.textContent = "O")
        : (this.textContent = "");
};
btnRestart.addEventListener("click", clearBoard);

// For the loop to add event Listeners to all the squares
for (let i = 0; i < squares.length; i++) {
    squares[i].addEventListener("click", changeMarker);
}
