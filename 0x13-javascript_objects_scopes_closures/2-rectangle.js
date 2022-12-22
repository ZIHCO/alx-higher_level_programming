#!/usr/bin/node
/*
 * This module contains a Rectangle class
 */

module.exports = class Rectangle {
  // The constructor  takes 2 args w and h
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
