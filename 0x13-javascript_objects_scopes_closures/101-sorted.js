#!/usr/bin/node
/*
 * module is a script that imports a dictionary of
 * occurrences by user id and computes a dictionary of
 * user ids by occurrence
 */

const myDict = require('./101-data.js').dict;
let myList = Object.keys(myDict);
let valueList = myList.map(x => myDict[x]);
const newDict = {};
let x, newList, index;
while (valueList.length !== 0) {
  x = valueList[0];
  index = valueList.indexOf(x);
  newList = [];
  while (index >= 0) {
    newList.push(myList[index]);
    myList = myList.slice(0, index).concat(myList.slice(index + 1));
    valueList = valueList.slice(0, index).concat(valueList.slice(index + 1));
    index = valueList.indexOf(x);
  }
  newDict[x] = newList;
}
console.log(newDict);
