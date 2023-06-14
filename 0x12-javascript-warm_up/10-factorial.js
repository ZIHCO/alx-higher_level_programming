#!/usr/bin/node

/*
 * compute factorial recursively
 */

const n = parseInt(process.argv[2]);

if (!n) {
  console.log(1);
} else {
  console.log(getFactorial(n));
}

function getFactorial (n) {
  if (n === 1 || n === 0) {
    return (1);
  } else {
    return (n * getFactorial(n - 1));
  }
}
