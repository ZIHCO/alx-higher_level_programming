#!/usr/bin/node

/*
 * Square subclass of REctangle
 */

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
