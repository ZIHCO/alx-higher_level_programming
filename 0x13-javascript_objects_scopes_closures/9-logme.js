#!/usr/bin/node
/*
 * prints the number of argument printed
 */
let count = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(`${count}: ${item}`);
    count++;
  }
};
