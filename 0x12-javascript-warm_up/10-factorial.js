#!/usr/bin/node

/*
 * compute factorial recursively
 */

let factorial = 1;
const n = process.argv[2];

function getFactorial (n) {
  if (!n || n <= 0) {
    console.log(1);
  } else {
    if (n === 1) {
      console.log(factorial);
    } else {
      factorial *= n;
      n -= 1;
      getFactorial(n);
    }
  }
}

getFactorial(n);
