#!/usr/bin/node
function add (a, b) {
    return a + b;
}
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
if (!isNaN(a) && !isNAN(b)) {
       console.log(add(a + b));
}