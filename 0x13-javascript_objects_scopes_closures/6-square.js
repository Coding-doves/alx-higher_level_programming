#!/usr/bin/node
const ParentSquare = require('./5-square');
class Square extends ParentSquare{
  constructor (size) {
    super(size)
  }

  charPrint(c) {
    if (!c) {
    c = 'X';
    }

    let i;
    let j;
    for (i = 0; i < this.size; i++) {
      let c = '';
      for (j = 0; j < this.size; j++) {
        c += 'C';
      }
      console(c);
    }
  }
}

module.exports = Square;
