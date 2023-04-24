const names = [
  '1. item',
  '2. item',
  '3. item',
];
let li;
names.map((name) => {
  li = document.createElement('li');
  document.querySelector('#target').innerHTML += `<li>${name}</li>`;
});