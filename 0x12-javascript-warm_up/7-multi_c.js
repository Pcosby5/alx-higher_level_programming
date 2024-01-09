#!/usr/bin/node

// Check if the first argument is not a number or is NaN
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  // Loop to print 'C is fun' based on the number provided as the argument
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun'); // Print 'C is fun' x times based on the argument
  }
}
