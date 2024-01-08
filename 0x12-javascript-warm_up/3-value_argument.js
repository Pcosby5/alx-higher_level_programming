#!/usr/bin/node
// Check if an argument is passed and print, else print no argument
const arg = process.argv[2];

if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
