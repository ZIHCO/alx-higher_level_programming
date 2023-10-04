const character = $('#character');
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, textstatus) {
  $(character).text(data.name);
});
