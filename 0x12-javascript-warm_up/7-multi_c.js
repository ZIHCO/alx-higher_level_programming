#!/usr/bin/node
/*
 * this module prints x times 'C is fun'
 */

const myInt = parseInt(process.argv[2]);
if (myInt) {
  for (let i = 0; i < myInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
