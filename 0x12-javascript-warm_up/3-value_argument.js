#!/usr/bin/node
// Check if the first argument is undefined or null
const firstArg = process.argv[2];

if (firstArg === undefined || firstArg === null) {
    console.log("No argument");
} else {
    console.log(firstArg);
}

