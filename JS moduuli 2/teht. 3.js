koirat = []
let u = 0;

for (u === 0; u < 6; u++) {
  koirat[u] = prompt("Enter the names of the Dogs: ")
}
koirat.sort((a,b) => a > b ? -1: 1)
document.querySelector('#r1').textContent = "These are the names of the dogs you have entered: "+ koirat;