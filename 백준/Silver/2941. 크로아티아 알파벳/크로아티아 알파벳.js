let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim();

let len = input.replace(/c=|c-|dz=|d-|lj|nj|s=|z=/g, "a").length;
console.log(len);