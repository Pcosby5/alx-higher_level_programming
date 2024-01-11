#!/usr/bin/node

// Import the array 'list' from the file 100-data.js
const list = require('./100-data').list;

// Use the map function to create a new array
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log(list);

// Print the new list
console.log(newList);
