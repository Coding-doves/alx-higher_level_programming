#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const actors = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, function (error, response, body) {
  if (error) { console.log(error); } else {
    const movies = JSON.parse(body).results;
    const filt = movies.filter((film) => film.characters.includes(actors));
    console.log(filt.length);
  }
});
