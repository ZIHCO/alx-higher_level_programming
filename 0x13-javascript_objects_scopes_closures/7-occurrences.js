#!/usr/bin/node

/*
 * the function returns the number of occurrence in a list
 */

exports.nbOccurences = function (list, searchElement) {
  if (list && searchElement) {
    let occurence = 0;
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        occurence += 1;
      }
    }
    return occurence;
  }
};
