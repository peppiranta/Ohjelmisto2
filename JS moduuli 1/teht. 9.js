const numbr = parseInt(prompt('Enter a number: '));
juu = true
var i;

if (numbr > 1) {
  for (i = 2; i < numbr; i++) {
      if (numbr % i === 0) {
        juu = false;
        break;
      }
  }
}
else {
  juu = false
}
if (juu) {
  document.body.textContent = `${numbr} is a prime number.`;
}
else {
  document.body.textContent = `${numbr} is not a prime number.`;
}
