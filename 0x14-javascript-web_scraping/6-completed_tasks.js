#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const todos = JSON.parse(body);
  const comptTasks = {};

  todos.forEach((compt) => {
    if (compt.completed) {
      if (comptTasks[compt.userId]) {
        comptTasks[compt.userId]++;
      } else { comptTasks[compt.userId] = 1; }
    }
  });
  console.log(comptTasks);
});
