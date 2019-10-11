// connect 4 javascript for jQuery practice.

//access the button elements
buttons = $(".board button");

var playerOne = true;
var playerOneName = prompt("Player one enter your name - you will be red")
var playerTwoName = prompt("Player two enter your name - you will be yellow")
$('h3').text(playerOneName + ", you go first")
$('.playerTwoDemo').toggleClass('turnYellow')
$('.playerOneName').text(playerOneName)
$('.playerTwoName').text(playerTwoName)

function changePlayer() {
  {
    playerOne = !playerOne;
    $('.playerOneDemo').toggleClass('turnRed')
    $('.playerTwoDemo').toggleClass('turnYellow')

    if (playerOne) {
      $('h3').text(playerOneName + " it's your turn")
    } else {
      $('h3').text(playerTwoName + " it's your turn")
    }
  }
}
//getting the index of a table position on click
buttons.on('click', function(event) {
  console.log("row" + $(this).closest('tr').index());
  console.log("column" + $(this).closest('td').index());

})
//get the css background colour of the clicked button
function getColour(rowIndex, columnIndex) {
  index = columnIndex + rowIndex * 7;
  return (buttons.eq(index).css('background-color'));
}

//check which is the lowest empty row in the input column
function bottomFinder(columnIndex) {
  console.log("bottomFinder");
  for (var row = 5; row > -1; row--) {
    console.log(row);
    colour = getColour(row, columnIndex);
    console.log(colour);
    if (colour === "rgb(200, 200, 200)") {
      return row;
    }
  }
}

//main
buttons.on('click', function(event) {
  var column = ($(this).closest('td').index());
  var row = bottomFinder(column);
  var buttonIndex = column + row * 7;
  if (playerOne) {
    buttons.eq(buttonIndex).toggleClass('turnRed');
  } else {
    buttons.eq(buttonIndex).toggleClass('turnYellow');
  }
  checkWin();
  changePlayer();
})

function colourMatchCheck(one, two, three, four) {
  var emptyTileColour = "rgb(200, 200, 200)";
  return (one === two && one === three && one === four && one !== emptyTileColour && one !== undefined);
}

function checkWin() {
  if (checkHorizontals() ||
    checkVerticals() ||
    checkDiagonals()) {
    if (playerOne) {
      alert(playerOneName + " you won! \n Refresh the browser to restart");
    } else {
      alert(playerTwoName + " you won! \n Refresh the browser to restart");
    }
  }
}

function checkHorizontals() {
  for (var row = 5; row > -1; row--) {
    for (var column = 0; column < 4; column++) {
      if (colourMatchCheck(getColour(row, column), getColour(row, column + 1), getColour(row, column + 2), getColour(row, column + 3))) {
        console.log("4 in a row! Horizontal");
        return (true);
      }
    }
  }
}

function checkVerticals() {
  //of all the buttons
  for (var column = 0; column < 7; column++) {
    for (var row = 5; row > 2; row--) {
      if (colourMatchCheck(getColour(row, column), getColour(row - 1, column), getColour(row - 2, column), getColour(row - 3, column))) {
        console.log("4 in a row! Vertical");
        return (true);
      }
    }
  }
}

function checkDiagonals() {
  for (var column = 0; column < 7; column++) {
    var runningTotal = 0;
    for (var row = 5; row > 3; row--) {
      if (colourMatchCheck(getColour(row, column), getColour(row - 1, column + 1), getColour(row - 2, column + 2), getColour(row - 3, column + 3))) {
        console.log("4 in a row! Diagonal");
      } else if (colourMatchCheck(getColour(row, column), getColour(row - 1, column - 1), getColour(row - 2, column - 2), getColour(row - 3, column - 3))) {
        console.log("4 in a row! Diagonal");
        return (true);
      }
    }
  }
}