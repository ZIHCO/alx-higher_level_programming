#!/usr/bin/node
/*
 * searches for the second biggest integer in the list
 */

const myList = process.argv.slice(2);
let sortedList;
const newList = [];
if (myList.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < myList.length; i++) {
    newList.push(parseInt(myList[i]));
  }
  sortedList = newList.sort(function (a, b) {
    return a - b;
  });
  console.log(sortedList[sortedList.length - 2]);
}
