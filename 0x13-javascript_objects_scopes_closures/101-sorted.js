#!/usr/bin/node
/*
 * dictionary of occurence
 */

const dict = require('./101-data').dict;

const newDict = {};
const keysList = Object.keys(dict);
const valuesList = [...new Set(Object.values(dict))];
for (let i = 0; i < valuesList.length; i++) {
  newDict[valuesList[i]] = [];
  for (let j = 0; j < keysList.length; j++) {
    if (valuesList[i] === dict[keysList[j]]) {
      newDict[valuesList[i]].push(keysList[j]);
    }
  }
}
console.log(newDict);
