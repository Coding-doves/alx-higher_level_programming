#!/usr/bin/node
const { list } = require('./100-data');

const map = list.map((a, b) => a * b);

console.log(list);
console.log(map);
