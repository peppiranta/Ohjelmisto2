const answer = confirm('Should I calculate the square root?')
console.log(answer);
let neliojuuri = 0
if (answer === true) {
  const  neliojuuri = parseInt(prompt("Enter a number: "))
  if (neliojuuri < 0) {
    document.querySelector('#a1').innerHTML = neliojuuri + " Number is negative!";
  }
  else {
    document.querySelector('#a1').innerHTML = ("Number " + neliojuuri + " square root is ") + Math.sqrt(neliojuuri);
  }
}
else {
  document.querySelector('#a1').innerHTML = "The square root is not calculated!"
}