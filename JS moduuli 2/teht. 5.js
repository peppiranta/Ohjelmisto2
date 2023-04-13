let digits = [];
let digit;
while (true) {
  digit = parseInt(prompt("Enter number: "));
  if (digits.includes(digit)) {
    alert("Number already given");
    break;
  }
  digits.push(digit);
}
const nr = digits.sort( (a, b) => a - b).map(items => `<li>${items}</li>`)
console.log(digits);
const result = document.querySelector('ul');
result.innerHTML = nr.join(" ");