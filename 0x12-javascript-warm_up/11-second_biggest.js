#!/usr/bin/node

/*
 * get the second biggest integer from the args
 */

const list = process.argv.slice(2);
const sortedList = list.sort(function (a, b) { return a - b; });
const listLength = list.length;

if (listLength <= 1) {
  console.log(0);
} else {
  console.log(sortedList[listLength - 2]);
}
