#!/usr/bin/node
/*
 * this module contains the global function:
 * addMeMaybe. addMeMaybe increment the arg1, and
 * calls arg2
 */

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
