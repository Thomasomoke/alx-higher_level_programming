#!/usr/bin/node
const factorial = (n) => {
    // If n is NaN or not a number, return 1
    if (isNaN(n)) {
        return 1;
    }
    // Base case: factorial of 0 or 1 is 1
    if (n <= 1) {
        return 1;
    }
    // Recursive case
    return n * factorial(n - 1);
};
