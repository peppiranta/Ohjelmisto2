let list = ['Jonny', 'Deedee', 'Joey', 'Marky'];
function concat(array){
  let modif = " "
  let i;
  for (i = 0; i < array.length; i++){
    modif = modif + array[i];
  }
  return modif;
}
document.querySelector('#names').textContent = concat(list);