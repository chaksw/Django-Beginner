'use strict';

const player1 = prompt('Player One: Enter Your Name, you will be Blue');
const player1Color = 'rgb(86, 151, 255)';

const player2 = prompt('Player Two: Enter Your Name, you will be Blue');
const player2Color = 'rgb(237, 45, 73)';

let game_on = true;
const table = $('table tr');
const colorGray = 'rgb(128, 128, 128)';

// Win report
const reportWin = function (rowNum, colNum) {
    console.log(`You won starting at this row: ${rowNum}, col: ${colNum}`);
};
// Table represnte a row(行) and tr represents a column(列)
// find the button with given row and column index, and change color
const changeColor = function (rowIndex, colIndex, color) {
    return table
        .eq(rowIndex)
        .find('td')
        .eq(colIndex)
        .find('button')
        .css('background-color', color);
};

// return the color of button with given row and index of table
const returnColor = function (rowIndex, colIndex) {
    return table
        .eq(rowIndex)
        .find('td')
        .eq(colIndex)
        .find('button')
        .css('background-color');
};

// return the first checked button of which color is gray from bottom row
const checkBottom = function (colIndex) {
    let colorReport = returnColor(5, colIndex);
    for (let row = 5; row > -1; row--) {
        colorReport = returnColor(row, colIndex);
        if (colorReport == colorGray) {
            return row;
        }
    }
};

// check if we have four same color mathc togther
const colorMatchCheck = function (one, two, three, four) {
    return (
        one === two &&
        one === three &&
        one === four &&
        one !== colorGray &&
        one !== undefined
    );
};

// Check for Horizantal Win
const horizontalWinChekck = function () {
    for (let row = 0; row < 6; row++) {
        for (let col = 0; col < 4; col++) {
            if (
                colorMatchCheck(
                    returnColor(row, col),
                    returnColor(row, col + 1),
                    returnColor(row, col + 2),
                    returnColor(row, col + 3)
                )
            ) {
                console.log('Horiz');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
};

// Check for Veritcal Win
const verticalWinChekck = function () {
    for (let col = 0; col < 7; col++) {
        for (let row = 0; row < 3; row++) {
            if (
                colorMatchCheck(
                    returnColor(row, col),
                    returnColor(row + 1, col),
                    returnColor(row + 2, col),
                    returnColor(row + 3, col)
                )
            ) {
                console.log('Verti');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
};

// Check for Diagonal Wins
const diagonalWinChekc = function () {
    for (let col = 0; col < 5; col++) {
        for (let row = 0; row < 7; row++) {
            if (
                colorMatchCheck(
                    returnColor(row, col),
                    returnColor(row + 1, col + 1),
                    returnColor(row + 2, col + 2),
                    returnColor(row + 3, col + 3)
                )
            ) {
                console.log('Diagonal');
                reportWin(row, col);
                return true;
            } else if (
                colorMatchCheck(
                    returnColor(row, col),
                    returnColor(row - 1, col + 1),
                    returnColor(row - 2, col + 2),
                    returnColor(row - 3, col + 3)
                )
            ) {
                console.log('Diagonal');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
};

// Game Logic
/* 
1. Start game and enter play name for player1 and player2
2. Click any button in the table and change the color the not-gray button in the bottom
3. Switch Player (text, color changed while pressing)
4. Verify if we have four same match color (horizontal, vertical, Diagonal)
5. Loop steps 2-4
6. Anounnce Winner when 4 is true
*/
const currentPlayer = {
    playerNum: 1,
    playerName: player1,
    playerColor: player1Color,
    swtichPlayer: function (playerNum) {
        this.playerNum = playerNum === 1 ? 1 : 2;
        this.playerName = playerNum === 1 ? player1 : player2;
        this.playerColor = playerNum === 1 ? player1Color : player2Color;
    },
};
// Start with player1
let curPlayer = 1;
let curName = player1;
let curColor = player1Color;
$('h3').text(
    `Player ${currentPlayer.playerName}: it is your turn, please pick a column to drop our blue chip`
);

$('.board button').on('click', function () {
    // Get the cloumn number of closest button that mouse clicked
    let col = $(this).closest('td').index();
    // get the row number of bottom gray button
    let bottomAvail = checkBottom(col);
    changeColor(bottomAvail, col, currentPlayer.playerColor);
    console.log(currentPlayer.playerColor);
    if (horizontalWinChekck() || verticalWinChekck() || diagonalWinChekc()) {
        $('h1').text(`${currentPlayer.playerName}, You have won!`);
        $('h2').fadeOut('fast');
        $('h3').fadeOut('fast');
    }
    currentPlayer.swtichPlayer(currentPlayer.playerNum === 1 ? 2 : 1);
    $('h3').text(
        `Player ${currentPlayer.playerName}
        : it is your turn, please pick a column to drop our blue chip`
    );
});
