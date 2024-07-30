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

    JSON.parse(res.body).characters.forEach((characterUrl) => {
      req.get(characterUrl, (err, res) => {
        if (err) {
          console.log(err);
          return;
        }
        console.log(JSON.parse(res.body).name);
      });
    });
  }
);
