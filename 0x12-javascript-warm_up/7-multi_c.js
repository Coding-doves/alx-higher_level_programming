#!/usr/bin/node
let x = parseInt(process.argv[2]);
let i;
if(!isNaN(x)) {
for (i = 0; i < x; i++) {
    console.log('C is fun');
}
} else {
    console.log('Missing number of occurrences');
}