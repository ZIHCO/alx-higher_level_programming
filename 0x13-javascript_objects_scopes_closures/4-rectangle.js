#!/usr/bin/node

/*
 * gate your instance attribute
 * add a print()  method
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let width = '';
      for (let j = 0; j < this.width; j++) {
        width += 'X';
      }
      console.log(width);
    }
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
