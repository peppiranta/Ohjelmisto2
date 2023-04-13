const r = Math.random()
const name = prompt("Enter your name: ")
if (r < 0.25) {
    document.querySelector('#h1').innerHTML = (name + " you are a Daredevil");
}
else if (r > 0.26 && r < 0.50) {
    document.querySelector('#h1').innerHTML = (name + " you are a Slytherin");
}
else if (r > 0.51 && r < 0.75) {
    document.querySelector('#h1').innerHTML = (name + " you are a Hufflepuff");
}
else {
    document.querySelector('#h1').innerHTML = (name + " you are a Ravenclaw");
}