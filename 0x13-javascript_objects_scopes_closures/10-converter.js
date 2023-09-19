#!/usr/bin/node
exports.converter = function (base) {
  return function (convertToBase) {
    return convertToBase.toString (base);
  };
};