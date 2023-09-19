#!/usr/bin/node
const arg  = process.arg.slice(2);

if (arg.length < 2) {
  console.log(0);
} else {
  console.log(arg.map(Number).sort((a, b) => b - a)[1]);
};
  