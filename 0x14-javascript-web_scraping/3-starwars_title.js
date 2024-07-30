#!/usr/bin/node
const req = require('request');

req(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  undefined,
  (_err, res) => {
    console.log(JSON.parse(res.body).title);
  }
);
