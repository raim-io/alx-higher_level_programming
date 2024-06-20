#!/usr/bin/node
let tracker = 0;

exports.logMe = function (item) {
  console.log(`${tracker}: ${item}`);
  tracker++;
};
