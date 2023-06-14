#!/usr/bin/node

/*
 * print a dynamic size square.
 */

const size = parseInt(process.argv[2]);
let myX;

if (size) {
  for (let i = 0; i < size; i++) {
    myX = '';
    for (let j = 0; j < size; j++) {
      myX += 'X';
    }
    console.log(myX);
  }
} else {
  console.log('Missing size');
}
