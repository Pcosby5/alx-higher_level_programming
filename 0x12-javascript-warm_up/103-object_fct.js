#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject); // Display the initial state of myObject

// Define a function named incr that increments the value property of myObject
function incr () {
  this.value++; // Increment the value property of the calling object
}

myObject.incr = incr; // Assign the incr function as a method to myObject

myObject.incr(); // Call the incr method to increment myObject's value
console.log(myObject); // Display myObject after the first increment

myObject.incr(); // Call incr method again
console.log(myObject); // Display myObject after the second increment

myObject.incr(); // Call incr method again
console.log(myObject); // Display myObject after the third increment
