#!/usr/bin/node
/*
 * Prints the first arguments passed
 */

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
