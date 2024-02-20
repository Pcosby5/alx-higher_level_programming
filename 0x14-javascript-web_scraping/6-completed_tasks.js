#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the URL from the command-line arguments
const url = process.argv[2];

// Make a GET request to the specified URL with the option to parse the response as JSON
request.get(url, { json: true }, (error, response, body) => {
  // If an error occurred during the request, log the error and exit the function
  if (error) {
    console.log(error);
    return;
  }

  // Object to store the number of tasks completed by each user
  const tasksCompleted = {};

  // Iterate over each todo in the response body
  body.forEach((todo) => {
    // Check if the todo is marked as completed
    if (todo.completed) {
      // If the user's ID is not already in the tasksCompleted object, initialize it to 1
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      }
      // If the user's ID is already in the tasksCompleted object, increment the count
      else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });

  // Print the tasksCompleted object, which contains the number of tasks completed by each user
  console.log(tasksCompleted);
});
