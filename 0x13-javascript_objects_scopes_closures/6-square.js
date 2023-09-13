#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare{
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      let keep = '';
      for (j = 0; j < this.width; j++) {
        keep += c;
      }
      console.log(keep);
    }
  }
}

module.exports = Square;
