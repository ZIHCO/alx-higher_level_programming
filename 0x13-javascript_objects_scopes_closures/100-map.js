#!/usr/bin/node
/*
 * import and do functional programming
 */

const list = require('./100-data').list;

const listIndex = [];

for (let i = 0; i < list.length; i++) {
  listIndex.push(list[i] * i);
}

console.log(list);
console.log(listIndex);
