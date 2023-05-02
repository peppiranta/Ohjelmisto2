function searchShow(name) {
  const url = 'https://api.tvmaze.com/search/shows?q=' + name;
  fetch(url).then(response => response.json()).then((Data) => {
    tulostaHaku(Data);
    console.log(Data);

    console.log(result);
  }).catch((error) => {
    console.log(error);
  });
}

function tulostaHaku(Data) {
  const list = document.getElementById('showlist');
  list.innerHTML = '';

  for (let i = 0; i < Data.length; i++) {
    try {

      console.log(Data[i]);
      const article = document.createElement('article');
      const element = document.createElement('li');
      const name = document.createElement('h4');
      name.innerText = Data[i].show.name;
      const poster = document.createElement('img');
      if (Data[i].show.image === null) {
        poster.src = 'nothing.png';
      } else {
        poster.src = Data[i].show.image.medium;
      }
      const desc = document.createElement('p');
      desc.innerHTML = Data[i].show.summary;
      const link = document.createElement('a');
      if (Data[i].show.officialSite === null) {
        link.innerHTML = 'There is no link';
      } else {
        link.innerHTML = 'Link to the TV-Show';
        link.href = Data[i].show.officialSite;
      }
      const genre = document.createElement('h4');
      genre.innerHTML = Data[i].show.genres;

      list.appendChild(element);
      element.appendChild(article);
      article.appendChild(name);
      article.appendChild(poster);
      article.appendChild(link);
      article.appendChild(desc);
      article.appendChild(genre);

    } catch {
      console.log('error');
    }
  }
}

let searchTimeoutToken = 0;
window.onload = () => {
  const searchFieldElement = document.getElementById('searchField');
  const sbutton = document.getElementById('searchbutton');
  sbutton.onclick = () => {
    clearTimeout(searchTimeoutToken);

    if (searchFieldElement.value.trim().length === 0) {
      const list = document.getElementById('showlist');
      list.innerHTML = '';
      return;
    }

    searchTimeoutToken = setTimeout(() => {
      searchShow(searchFieldElement.value);
    }, 300);
  };
};