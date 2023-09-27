#!/usr/bin/node
/*
 * Write a script that reads and prints the content of a file.
 */

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err, content) => {
  if (err) {
    console.log(err);
  }
});
