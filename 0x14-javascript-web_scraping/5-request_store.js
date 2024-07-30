#!/usr/bin/node
const req = require('request');
const fs = require('fs');

req(process.argv[2]).pipe(
  fs.createWriteStream(process.argv[3], { encoding: 'utf-8' })
);
