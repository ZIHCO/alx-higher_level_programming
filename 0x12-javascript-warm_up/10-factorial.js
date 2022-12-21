#!/usr/bin/node
/*
 * This module contains the factorial function
 */

const myInt = parseInt(process.argv[2]);

if (myInt) {
  console.log(`${factorial(myInt)}`);
} else {
  console.log('1');
}

function factorial (a) {
  if (a === 1 || a === 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}
