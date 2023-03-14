#!/usr/bin/node
/*
 * This module print a square:
 * Usage - ./module size
 * where size is an integer represent of the sie of the
 * square
 */

const myInt = parseInt(process.argv[2]);
if (myInt) {
  let i = 0;
  let j;
  let myX;
  while (i < myInt) {
    j = 0;
    myX = '';
    while (j < myInt) {
      myX += 'X';
      j++;
    }
    console.log(myX);
    i++;
  }
} else {
  console.log('Missing size');
}
