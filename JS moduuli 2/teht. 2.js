numparticipants = parseInt(prompt("Enter numbers of participants:"))
let x = 0;
let num;
num = [];

for (x === 0; x < numparticipants; x++) {
  num[x] = prompt("Enter the names of the participants: ")
}
num.sort((a,b) => a > b ? 1: -1)
document.querySelector('#i1').textContent = "You have selected "+ numparticipants +  " of participants. These are the names of the participants: " + num;