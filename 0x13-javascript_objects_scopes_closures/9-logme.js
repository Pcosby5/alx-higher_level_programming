#!/usr/bin/node

let counter = 0; // Counter to track the number of arguments already printed

// Export a function named logMe using exports
exports.logMe = function (item) {
  console.log(`${counter}: ${item}`); // Print the current counter and argument value
  counter++; // Increment the counter for the next call
};
