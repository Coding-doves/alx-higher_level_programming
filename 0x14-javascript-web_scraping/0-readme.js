#!/usr/bin/node
const fs = require('fs');

const fileP = process.argv[2];

fs.readFile(fileP, 'utf-8', (err, data) => {
  if (err) { console.log(err); } else { console.log(data); }
});
