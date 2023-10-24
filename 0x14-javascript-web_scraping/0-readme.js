#!/usr/bin/node
const fs = require('fs');

fileP = process.argv[2];

fs.readfile(fileP, (err, data) => {
  if (err) { console.log(err); }
  else { console.log(err); }
})
