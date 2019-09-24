var reset = document.querySelector("#b");

var squares = document.querySelectorAll("td");

function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = ""
  }
}

reset.addEventListener('click', clearBoard);

function changeMarker() {
  if (this.textContent === '') {
    this.textContent = "X";
  } else if (this.textContent === 'X') {
    this.textContent = 'O';
  } else {
    this.textContent = ''
  }
}


//this confused me for hours - can not assign textContent to squares[i], but can assign textContent to this
for (var i = 0; i < squares.length; i++) {
  let x = i;
  console.log(x);
  squares[i].addEventListener('click', function() {
    squares[x].textContent = 't';
    console.log(x);
  })
}

function helloFactory(person) {
  console.log("Creating " + person + " welcome");
  var x = 2

  var t = function() {
    console.log("Hello " + person);
    console.log("x = " + x);
  }

  x = 3;

  return t;
};