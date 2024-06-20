#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const similarItems = list.filter((item) => item === searchElement);

  return similarItems.length;
};
