#!/usr/bin/node
class Square extends supSquare {
    charPrint (c) {
        if (c == null) {
            c = 'x';
        }
        for (let i = 0; i < this.width; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

module.exports = Square;

