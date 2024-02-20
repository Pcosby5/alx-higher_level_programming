#!/usr/bin/node

// Import fs using require
const fs = require('fs');

// Import request
const request = require('request');

// Get the file path from command line
const url = process.argv[2];

// Get the string to write
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Write the content of the file
    fs.writeFile(fileName, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
        /* } else {
    console.log(data); */
      }
    });
  }
});
