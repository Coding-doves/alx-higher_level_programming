#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (this.width && this.height) {
      let i;
      let j;
      for (i = 0; i < this.height; i++) {
        let x = '';
        for (j = 0; j < this.width; j++) {
          x += 'X';
        }
        console.log(x);
      }
    }
  }

  rotate() {
    if (this.width && this.height) {
      let exchange = this.height;
      this.height = this.width;
      this.width = exchange;
    }
  }

  double() {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }

}

module.exports = Rectangle;
