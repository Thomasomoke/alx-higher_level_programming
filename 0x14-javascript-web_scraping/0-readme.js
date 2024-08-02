#!/usr/bin/node
const fs = require('fs');
fs.readFile("./t.txt", "utf-8", (error, data) => {
	if (error) {
		console.log(error)
	} else {
		console.log(data);
	}

});
