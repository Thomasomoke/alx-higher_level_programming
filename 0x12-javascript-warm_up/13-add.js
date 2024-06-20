#!/usr/bin/node
const add = (a, b) => {
    // Ensure both arguments are integers
    const intA = parseInt(a, 10);
    const intB = parseInt(b, 10);

    // Return the sum of the two integers
    return intA + intB;
};
