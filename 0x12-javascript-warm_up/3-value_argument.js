#!/usr/bin/node
const nArgs = process.argv[2];

if (!nArgs) {
  console.log('No argument');
} else {
  console.log(nArgs);
}