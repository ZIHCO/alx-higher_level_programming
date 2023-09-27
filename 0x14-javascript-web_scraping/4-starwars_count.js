#!/usr/bin/node
/*
 * Write a script that prints the number of movies where the
 * character “Wedge Antilles” is present.
 */

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const dict = JSON.parse(body);
  const countMovies = dict.count;
  const charId = 18;
  const wedgeAntiles = 'https://swapi-api.alx-tools.com/api/people/' + charId + '/';
  console.log(wedgeAntiles);
  let count = 0;
  for (let i = 0; i < countMovies; i++) {
    if (dict.results[i].characters.indexOf(wedgeAntiles) !== -1) {
      count += 1;
    }
  }
  console.log(count);
});
