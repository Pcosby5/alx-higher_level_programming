#!/usr/bin/node

// Define and export a function named callMeMoby using exports
exports.callMeMoby = function (x, theFunction) {
  // Loop x times and execute theFunction on each iteration
  for (let i = 0; i < x; i++) {
    theFunction(); // Call the provided function x times
  }
};
