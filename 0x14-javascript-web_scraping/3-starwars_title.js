#!/usr/bin/node

// use require to import the request module
const request = require('request');

// Get the movie_id from the command line
const movieId = process.argv[2];

// Get the URL from the url we are targeting
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);

    // Parse the response body as JSON
  } else {
    const movieData = JSON.parse(body);

    // Print the title of the movie
    console.log(movieData.title);
  }
});
