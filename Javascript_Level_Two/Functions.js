function hello(name) {
  console.log("hello " + name);
}

function addNum(num1, num2) {
  console.log(num1 + num2);
}

//setting default args
function helloSomeone(name = "noname") {
  console.log("hello " + name);

}

function formal(name = "sam", title = "Sir") {
  console.log(title + name);
  return (title + name);
}

function timesFive(numInput) {
  return (numInput * 5);

}

//SCOPE

var v = "GLOBAL Var";
var stuff = "GLOBAL STUFF";

function reassign(stuff) {
  console.log(v);
  stuff = "Reassign stuff";
  console.log("inside" + stuff);
}

reassign();
console.log("outside " + stuff);