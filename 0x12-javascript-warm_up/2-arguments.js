#!/usr/bin/node
// Check the number of arguments passed and print using console.log
if (process.argv.length === 2)
{
  console.log("No argument");
} else if (process.argv.length === 3)
{
  console.log("Argument found");
} else
{
  console.log("Arguments found");
}
