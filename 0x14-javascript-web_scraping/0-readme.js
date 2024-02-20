#!/usr/bin/node

// Import fs using require
const fs = require('fs');

// Get the file path from command line
const filename = process.argv[2];

// Read the content of the file
fs.readFile(filename, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
