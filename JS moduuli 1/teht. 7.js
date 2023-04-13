let diceroll
let dice = parseInt(prompt("Enter the number of dice:"))
let dicesum = 0;
for(let x = 0; x < dice; x++) {
  diceroll = Math.floor(Math.random() * 6)+1;
  dicesum += diceroll;
}
document.querySelector('#n1').innerHTML = " Number of the dice have thrown: " + dice + "."
    + " The sum of the dice numbers: " + dicesum ;