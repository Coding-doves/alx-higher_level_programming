#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let occ = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { occ++; }
  }
  return occ;
}
