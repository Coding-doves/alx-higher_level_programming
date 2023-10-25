#!/usr/bin/node
const fs = require('fs');

const fileP = process.argv[2];
const string = process.argv[3];

fs.writeFile(fileP, string, { encoding: 'utf-8' }, (err) => {
  if (err) { console.log(err); }
});
