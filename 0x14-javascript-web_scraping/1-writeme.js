#!/usr/bin/node

// Import fs using require
const fs = require('fs');

// Get the file path from command line
const filename = process.argv[2];

// Get the string to write
const stringToWrite = process.argv[3];

// Write the content of the file
fs.writeFile(filename, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  /* } else {
    console.log(data); */
  }
});
