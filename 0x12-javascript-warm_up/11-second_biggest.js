#!/usr/bin/node

// Create an empty array to store integers
const array = [];

// Check if no arguments or only one argument is provided
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0); // Print 0 if there are no arguments or only one argument
} else {
  // Iterate through process.argv starting from index 2 (skipping node and script name)
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i])); // Convert arguments to integers and add to the array
  }

  const max = Math.max(...array); // Find the maximum value in the array
  array.splice(array.indexOf(max), 1); // Remove the maximum value from the array

  // Print the second largest integer in the array
  console.log(Math.max(...array));
}
