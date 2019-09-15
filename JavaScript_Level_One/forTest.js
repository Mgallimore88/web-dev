console.log("for loop demo: count to 5");
for (var i = 1; i < 6; i++) {
  console.log("number is " + i)
}

console.log("test 2");

var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for (var i = 0; i < alphabet.length; i++) {
  console.log(alphabet[i]);
}

console.log("test 3");
var abab = "ABABABABABABA";
for (var i = 0; i < abab.length; i = i + 2) {
  console.log(abab[i]);
}