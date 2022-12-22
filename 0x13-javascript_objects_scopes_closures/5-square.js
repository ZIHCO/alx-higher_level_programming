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

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str = str + 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    const copywidth = this.width;
    this.width = this.height;
    this.height = copywidth;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
