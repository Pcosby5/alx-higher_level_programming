#!/usr/bin/node

// Import the dictionary 'dict' from the file 101-data.js
const dict = require('./101-data').dict;

// Use the reduce function to create a new dictionary
const newDict = Object.keys(dict).reduce((result, userId) => {
  const occurrences = dict[userId];

  if (!result[occurrences]) {
    result[occurrences] = [userId];
  } else {
    result[occurrences].push(userId);
  }

  return result;
}, {});

// Print the new dictionary
console.log(newDict);
