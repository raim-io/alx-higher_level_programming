#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = parseInt(process.argv[2]); i > 0; --i) {
    console.log('C is fun');
  }
}
