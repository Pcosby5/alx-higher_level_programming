#!/usr/bin/node

// Check if the first argument is not a number
if (isNaN(process.argv[2])) {
  console.log('Missing size'); // Print "Missing size" if the argument is not a number
} else {
  const size = parseInt(process.argv[2]); // Convert the argument to an integer
  const row = 'X'.repeat(size); // Create a row of 'X' characters based on the size

  // Loop to print 'X' rows to form a square
  for (let i = 0; i < size; i++) {
    console.log(row); // Print each row of 'X' characters
  }
}
