#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  const count = parseInt(process.argv[2]);
  let i = 0;
  while (i < count) {
    console.log('x'.repeat(count));
    i++;
  }
}
