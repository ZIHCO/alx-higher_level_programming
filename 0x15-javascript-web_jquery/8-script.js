const listMovies = $('#list_movies');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data, statusText) {
  const listObjs = data.results;
  for (let count = 0; count < listObjs.length; count++) {
    const movie = $('<li></li>').text(listObjs[count].title);
    $(listMovies).append(movie);
  }
});
