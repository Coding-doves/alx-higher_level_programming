#!/usr/bin/node
let x = parseInt(process.argv[2]);
let i, j, squ = '';
if (isNaN(x)) {
    console.log('Missing size');
} else {
    for (i = 0; i < x; i++) {
        for (j = 0; j < x; j++) {
            squ += 'X';
        }
        console.log(squ);
        squ = '';
    }
}