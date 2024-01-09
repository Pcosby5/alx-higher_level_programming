#!/usr/bin/node

// Import the Rectangle class from another file
const Rectangle = require('./4-rectangle');

// Define a class named Square that extends the Rectangle class
class Square extends Rectangle {
  // Constructor that takes size as an argument and calls the superclass constructor with size, size
  constructor (size) {
    super(size, size); // Call the superclass (Rectangle) constructor with size as both width and height
  }
}

module.exports = Square; // Export the Square class to make it accessible outside the script
