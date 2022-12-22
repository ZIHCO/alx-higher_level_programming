#!/usr/bin/node
/*
 * This module contains a Rectangle class
 */

module.exports = class Rectangle {
  /* The constructor  takes 2 args w and h
   * print method
   */

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
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
};
