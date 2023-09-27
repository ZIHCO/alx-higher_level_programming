#!/usr/bin/node
/*
 * reading file
 */

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, fileA) => {
  if (err) throw err;
  fs.readFile(process.argv[3], 'utf8', (err, fileB) => {
    if (err) throw err;
    const str = fileA + fileB;
    fs.writeFile(process.argv[4], str, (err) => {
      if (err) throw err;
    });
  });
});
