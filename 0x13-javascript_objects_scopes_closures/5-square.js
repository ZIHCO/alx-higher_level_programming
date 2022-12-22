#!/usr/bin/node
/*
 * This module contains a Square subclass
 */

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  /* The constructor  takes 2 args w and h
   * print method
   */

  constructor (size) {
    super(size, size);
  }
};
