#!/usr/bin/node
const arg = process.argv[2]; // Get the first argument passed to the script

const num = parseInt(arg); // Attempt to convert the argument to an integer

if (!isNaN(num)) {
    console.log(`My number: ${num}`);
} else {
    console.log("Not a number");
}

