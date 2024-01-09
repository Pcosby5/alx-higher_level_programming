#!/usr/bin/node

// Define a recursive function to calculate factorial
function factorial(n) {
  // Check if n is NaN or less than 0, return 1 in these cases
  if (isNaN(n) || n < 0) {
    return 1;
  }

  // Base case: if n is 0, return 1
  if (n === 0) {
    return 1;
  }

  // Recursive call to calculate factorial
  return n * factorial(n - 1);
}

// Extract the first argument from process.argv and convert it to an integer
const arg = parseInt(process.argv[2]);

// Compute the factorial and print the result
console.log(factorial(arg));
