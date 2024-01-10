#!/usr/bin/node

// Export a function named nbOccurences using exports
exports.nbOccurences = function (list, searchElement) {
  let count = 0; // Initialize a counter for occurrences

  // Loop through the elements in the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the searchElement
    if (list[i] === searchElement) {
      count++; // Increment the counter if a match is found
    }
  }

  return count; // Return the final count of occurrences
};
