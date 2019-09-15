var firstName = prompt('hi, please enter your first name');
var lastName = prompt("and your second name");
var age = prompt("how old are you?");
var height = prompt("and how tall in cm?");
var pet = prompt("last, what's your pet name:")

// key 1
if (firstName[0] === lastName[0]) {
  var key1 = true;
}

// key 2
if (age >= 20 && age <= 30) {
  var key2 = true;
}

//  key 3
if (height >= 170) {
  var key3 = true;
}
//  key 4
var petWordLength = pet.length;
if (pet[petWordLength] == "y" || "Y") {
  var key4 = true;
}

// calculation
if (key1 && key2 && key3 && key4) {
  console.log('orange smoothies are very sweet');
}