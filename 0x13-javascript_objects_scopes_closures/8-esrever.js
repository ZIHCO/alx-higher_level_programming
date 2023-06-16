#!/usr/bin/node

/*
 * reverses a list
 */

exports.esrever = function (list) {
  if (list) {
    const tsil = [];
    for (let i = (list.length - 1); i >= 0; i--) {
      tsil.push(list[i]);
    }
    return tsil;
  }
};
