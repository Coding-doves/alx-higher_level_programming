#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  const ser = [];

  for (i = list.length - 1; i >= 0; i--) {
    ser.push(list[i]);
  }
  return ser;
}
