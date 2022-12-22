#!/usr/bin/node
/*
 * This module contains a Square subclass
 */

const SquareP = require('./5-square');
module.exports = class Square extends SquareP {
  /* The constructor  takes 2 args w and h
   * print method
   */

  constructor (size) {
    super();
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        let str = '';
        for (let j = 0; j < this.size; j++) {
          str = str + c;
        }
        console.log(str);
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        let str = '';
        for (let j = 0; j < this.size; j++) {
          str = str + 'X';
        }
        console.log(str);
      }
    }
  }
};
