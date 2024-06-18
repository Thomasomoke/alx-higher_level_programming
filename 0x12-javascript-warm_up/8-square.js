#!/usr/bin/node
#!/usr/bin/env node

// Retrieve the first argument
const sizeArg = process.argv[2];

// Check if the argument is a number
const size = parseInt(sizeArg, 10);

// If the argument is not a valid number, print "Missing size"
if (isNaN(size)) {
    console.log("Missing size");
} else {
    // Loop to print the square of X's
    for (let i = 0; i < size; i++) {
        let line = '';
        for (let j = 0; j < size; j++) {
            line += 'X';
        }
        console.log(line);
    }
}

