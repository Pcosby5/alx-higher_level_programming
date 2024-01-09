#!/usr/bin/node
// check if the first argument is a number
if (!isNaN(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
