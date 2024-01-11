#!/usr/bin/node

const fs = require('fs');

// Ensure that three command-line arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: ./concatFiles.js <file1> <file2> <destination>');
  process.exit(1);
}

// Extract file paths from command-line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read the contents of the first source file
const content1 = fs.readFileSync(sourceFilePath1, 'utf-8');

// Read the contents of the second source file
const content2 = fs.readFileSync(sourceFilePath2, 'utf-8');

// Concatenate the contents of the two files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFilePath, concatenatedContent);

console.log(`Contents of ${sourceFilePath1} and ${sourceFilePath2} concatenated to ${destinationFilePath}`);
