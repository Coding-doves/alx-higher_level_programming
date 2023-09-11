#!/usr/bin/node
const nArgs = process.argv[2];

if (nArgs === 0) {
  console.log("No argument");
} else {
  console.log(nArgs);
}