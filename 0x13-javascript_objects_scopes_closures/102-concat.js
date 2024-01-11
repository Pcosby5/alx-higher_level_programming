#!/usr/bin/node

const file = require('fs'); // Import the 'fs' module for file operations

// Read the contents of the first source file (specified in the first command-line argument)
const fileA = file.readFileSync(process.argv[2], 'utf8');

// Read the contents of the second source file (specified in the second command-line argument)
const fileB = file.readFileSync(process.argv[3], 'utf8');

// Concatenate the contents of the two files
const concatenatedContent = fileA + fileB;

// Write the concatenated content to the destination file (specified in the third command-line argument)
file.writeFileSync(process.argv[4], concatenatedContent);
