#!/usr/bin/node
/*
 * Write a script that reads and prints the content of a file.
 */

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
