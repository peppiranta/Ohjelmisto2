document.querySelector('button#start').addEventListener('click', () => {
  const text = document.querySelector('#calculation').value;

  if (text.includes('+')) {
    const numbers = text.split('+');
    document.querySelector('#result').textContent = parseInt(numbers[0]) +
        parseInt(numbers[1]);
  } else if (text.includes('-')) {
    const numbers = text.split('-');
    document.querySelector('#result').textContent = parseInt(numbers[0]) -
        parseInt(numbers[1]);
  } else if (text.includes('*')) {
    const numbers = text.split('*');
    document.querySelector('#result').textContent = parseInt(numbers[0]) *
        parseInt(numbers[1]);
  } else if (text.includes('/')) {
    const numbers = text.split('/');
    document.querySelector('#result').textContent = parseInt(numbers[0]) /
        parseInt(numbers[1]);
  }
});