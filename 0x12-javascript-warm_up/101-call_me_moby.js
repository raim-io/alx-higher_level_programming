#!/usr/bin/node
exports.callMeMoby = function (count, fxn) {
  let i = 0;
  while (i < count) {
    fxn();
    i++;
  }
};
