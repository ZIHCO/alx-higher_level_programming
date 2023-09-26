#!/usr/bin/node
/*
 * import and do functional programming
 */

const list = require('./100-data').list;

const listIndex = list.map((x) => (x * list.indexOf(x)));

console.log(list);
console.log(listIndex);
