#!/usr/bin/node

// Export a function named converter using exports
exports.converter = function (base) {
  // Return a function that converts a number to a string representation in the specified base
  return function (num) {
    return num.toString(base);
  };
};
