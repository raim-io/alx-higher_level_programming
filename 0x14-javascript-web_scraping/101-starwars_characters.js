#!/usr/bin/node
const req = require('request');

req.get(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  undefined,
  (err, res) => {
    if (err) {
      console.log(err);
      return;
    }

    recursivelyPrintAllCharactersOrderly(JSON.parse(res.body).characters, 0);
  }
);

const recursivelyPrintAllCharactersOrderly = (characters, index) => {
  req(characters[index], (err, res) => {
    if (err) {
      console.log(err);
      return;
    }

    console.log(JSON.parse(res.body).name);

    if (index + 1 < characters.length) {
      recursivelyPrintAllCharactersOrderly(characters, index + 1);
    }
  });
};
