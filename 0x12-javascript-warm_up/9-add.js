#!/usr/bin/node

// Define the function add(a, b) to add two integers
function add (a, b) {
  return a + b; // Return the sum of the two integers
}

// Call the add function with the integers parsed from arguments and print the result
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
