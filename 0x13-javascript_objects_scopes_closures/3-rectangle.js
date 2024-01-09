#!/usr/bin/node

// Define a class named Rectangle
class Rectangle {
  // Constructor that initializes the width and height attributes if both are positive integers
  constructor (w, h) {
    // Check if both width and height are positive integers
    if (w > 0 && h > 0) {
      this.width = w; // Initialize width attribute with the value of w
      this.height = h; // Initialize height attribute with the value of h
    }
  }

  // Instance method named print() to print the rectangle using the character 'X'
  print () {
    // Print the rectangle using 'X' characters based on width and height
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle; // Export the Rectangle class to make it accessible outside the script
