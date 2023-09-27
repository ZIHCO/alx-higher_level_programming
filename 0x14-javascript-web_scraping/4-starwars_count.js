#!/usr/bin/node
/*
 * Write a script that prints the number of movies where the
 * character “Wedge Antilles” is present.
 */

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  const dict = JSON.parse(body);
  const countMovies = dict.count;
  let count = 0;
  for (let i = 0; i < countMovies; i++) {
    for (let j = 0; j < dict.results[i].characters.length; j++) {
      const character = dict.results[i].characters[j].split('/')[5];
      if (character === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
