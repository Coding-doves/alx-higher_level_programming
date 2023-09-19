#!/usr/bin/node
exports.converter = function (base) {
  return function (convertToBase) {
    if (convertToBase < base) {
      return convertToBase.toString(base);
    } else {
      return convertToBase.toString(Math.floor(n / base)) + (n % base);
    }
  }
};
