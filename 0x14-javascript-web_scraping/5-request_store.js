#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileP = process.argv[3];

request(url, 'utf-8', function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(fileP, body, (err) => {
    if (err) { console.log(err); }
  });
});
