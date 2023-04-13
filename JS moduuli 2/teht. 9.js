const numberarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
function even(array){
  const evenum = []
  for (i = 0; i < array.length; i++){
    if (array[i] % 2 === 0){
      evenum.push(array[i])
    }
  }
  return evenum;
}
console.log(numberarray)
console.log(even(numberarray))