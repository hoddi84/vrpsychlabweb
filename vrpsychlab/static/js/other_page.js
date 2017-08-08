$( document ).ready(function() {

  document.getElementById("demo").addEventListener("click", myFunction);
});

function myFunction() {
  var select = document.getElementById("demo");
  var e = select.options[select.selectedIndex].value;

  document.getElementById("msg").innerHTML = e;
}
