#!/usr/bin/node

/*
 * looping and commandline argument
 */

const amount = parseInt(process.argv[2]);

if (amount) {
  for (let i = 0; i < amount; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
