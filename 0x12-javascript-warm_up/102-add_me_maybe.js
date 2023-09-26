#!/usr/bin/node
/*
 * increment and call
 */

function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

exports.addMeMaybe = addMeMaybe;
