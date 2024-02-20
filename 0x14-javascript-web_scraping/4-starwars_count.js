#!/usr/bin/node

// use require to import the request module
const request = require('request');

// Get the url from the command line
const url = process.argv[2];

// The characterId we are targeting
const characterId = '18';

let numberOfMovies = 0;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);

    // Parse the response body/object as JSON
  } else {
    // Parsed Json data
    const data = JSON.parse(body);

    // iterates the results array for each film
    data.results.forEach((film) => {
      // For each film, it iterates over the characters array
      film.characters.forEach((character) => {
        // checks if the characterId finds a match
        if (character.includes(characterId)) {
          // Increment count for matched characterId
          numberOfMovies += 1;
        }
      });
    });

    // Print the number of movies by Wedge Antilles
    console.log(numberOfMovies);
  }
});
