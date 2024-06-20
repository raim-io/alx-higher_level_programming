#!/usr/bin/node
const dictionary = require('./101-data.js').dict;

const userIds = Object.values(dictionary);
const uniqueUserIds = [...new Set(userIds)];
const occurrences = Object.entries(dictionary);

const transformedDictionary = {};
for (const id in uniqueUserIds) {
  const temp = [];
  for (const occurrence in occurrences) {
    if (occurrences[occurrence][1] === uniqueUserIds[id]) {
      temp.unshift(occurrences[occurrence][0]);
    }
  }

  transformedDictionary[uniqueUserIds[id]] = temp;
}

console.log(transformedDictionary);
