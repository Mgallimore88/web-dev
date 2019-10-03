// connect 4 javascript for jQuery practice.

//access the button elements
buttons = $(".board button");

var playerOne = true;


//getting the index of a table position on click
$('.board button').on('click', function(event) {
  console.log("this is the row");
  console.log($(this).closest('tr').index());
  console.log("this is the column");
  console.log($(this).closest('td').index());

})
//get the css background colour of the clicked button
function getColour(rowIndex, columnIndex) {
  return ($("tr").eq(rowIndex).find('td').eq(columnIndex).find('.button').css('background-color'));
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

function changePlayer() {
  {
    playerOne = !playerOne;
    console.log(playerOne)
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
  changePlayer();
})