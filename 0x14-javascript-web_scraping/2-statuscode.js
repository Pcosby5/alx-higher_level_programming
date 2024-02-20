#!/usr/bin/node

// use require to import the request module
const request = require('request');

// Get the URL from the command line
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
