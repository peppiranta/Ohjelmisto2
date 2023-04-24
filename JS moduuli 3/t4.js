'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

students.map((student) => {
  const Option = document.createElement('option');
  Option.value = student.id;
  Option.innerHTML = student.name;
  document.querySelector('#target').appendChild(Option);

});
