#!/usr/bin/node

/*
 * subclass square, with an instance method called charPrint(c)
 */

const SuperSquare = require('./5-square');

module.exports = class Square extends SuperSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      let width;
      for (let i = 0; i < this.size; i++) {
        width = '';
        for (let j = 0; j < this.size; j++) {
          width += c;
        }
        console.log(width);
      }
    } else {
      let width;
      for (let i = 0; i < this.size; i++) {
        width = '';
        for (let j = 0; j < this.size; j++) {
          width += 'X';
        }
        console.log(width);
      }
    }
  }
};
