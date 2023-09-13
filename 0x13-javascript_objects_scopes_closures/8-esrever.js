#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

exports.esrever = function (list) {
  let i;
  let ser = [];

  for (i = list.length - 1; i >= 0; i--) {
    ser.push(list[i]);
  }
  return ser;
}

