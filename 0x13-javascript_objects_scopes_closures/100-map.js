#!/usr/bin/node
/*
 * module is a script that imports an array,
 * and computes a new array
 */

const myList = require('./100-data').list;
const newList = myList.map((x, i) => x * i);
console.log(myList);
console.log(newList);
