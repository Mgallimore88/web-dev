console.log("js connected!")

var one = document.querySelector("#ONE")
var two = document.querySelector("#TWO")
var three = document.querySelector("#THREE")

one.addEventListener("mouseover", function() {
  one.textContent = "mouse currently over";
  one.style.color = 'red'
})

one.addEventListener("mouseout", function() {
  one.textContent = "HOVER OVER ME"
  one.style.color = 'black'

})

two.addEventListener('click', function() {
  two.textContent = "clicked on"

})

three.addEventListener("dblclick", function() {
  three.textContent = "I was double clicked"
  three.style.color = 'red'
})