#!/usr/bin/node
const req = require('request');

req(process.argv[2], undefined, (_err, res) => {
  console.log(
    JSON.parse(res.body).results.filter((result) =>
      result.characters.some((character) => character.endsWith('/18/'))
    ).length
  );
});
