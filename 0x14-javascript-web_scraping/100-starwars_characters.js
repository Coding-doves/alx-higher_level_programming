#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const cName = JSON.parse(body).characters;

  cName.forEach((acts) => {
    request(acts, (err, res, films) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(films).name);
    });
  });
});
