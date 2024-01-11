#!/usr/bin/node

// Export a function named esrever using exports
exports.esrever = function (list) {
  const reversedList = []; // Create an empty array to store the reversed elements

  // Loop through the elements in the list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]); // Add each element to the reversedList array
  }

  return reversedList; // Return the reversed version of the list
};
