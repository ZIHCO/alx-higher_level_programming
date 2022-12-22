#!/usr/bin/node
/*
 * returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (searchElement && list) {
    for (let i = 0; i < list.length; i++) {
      if (searchElement === list[i]) {
        count += 1;
      }
    }
  }
  return count;
};
