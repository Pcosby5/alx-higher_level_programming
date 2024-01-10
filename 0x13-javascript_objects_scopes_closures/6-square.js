#!/usr/bin/node

// Import the Square class from another file
const Square1 = require('./5-square');

// Define a class named Square that extends the Square1 class
class Square extends Square1 {
  // Instance method named charPrint that prints the square using a specified character
  charPrint(c) {
    // Check if the character is not provided
    if (!c) {
      // Print the square using 'X' characters based on the width and height
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      // Print the square using the provided character based on the width and height
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square; // Export the Square class to make it accessible outside the script
