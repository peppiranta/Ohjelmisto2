document.querySelector('form#source').addEventListener('submit', e => {
  e.preventDefault();
  const firstName = document.querySelector('input[name=\'firstname\']').value;
  const lastName = document.querySelector('input[name=\'lastname\']').value;
  document.querySelector('#target').textContent = 'Your name is ' + firstName +
      ' ' + lastName;
});