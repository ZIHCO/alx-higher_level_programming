#!/usr/bin/node
/*
 * Contain the anonymous function that
 * executes a passed function x times
 */

exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
