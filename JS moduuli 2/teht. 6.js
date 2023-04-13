let r = -1

function rollDice() {
  return Math.ceil(Math.random() * 6);
}

const list = document.getElementById('list');
let liste;
while (r !== 6){
  r = rollDice()
  liste = document.createElement('li');
  liste.innerHTML = r;
  list.append(liste);
}