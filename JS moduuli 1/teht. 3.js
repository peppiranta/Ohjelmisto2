const num1 = parseFloat(prompt("Enter an integer:"))
const num2 = parseFloat(prompt("Enter an integer:"))
const num3 = parseFloat(prompt("Enter an integer:"))

const sumint = num1 + num2 + num3
const productint = num1 * num2 * num3
const averageint =  sumint / 3

document.querySelector('#p1').innerHTML = " Sum = " + sumint;
document.querySelector('#p2').innerHTML = " Product = " + productint;
document.querySelector('#p3').innerHTML = " Average = " + averageint;