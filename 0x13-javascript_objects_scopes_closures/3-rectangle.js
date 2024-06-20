#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let hex = '';
      for (let j = 0; j < this.width; j++) {
        hex += 'X';
      }
      console.log(hex);
    }
  }
}

module.exports = Rectangle;
