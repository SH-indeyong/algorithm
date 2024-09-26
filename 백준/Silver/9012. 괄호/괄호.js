let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const testCase = Number(input[0]);

for (let i = 1; i <= testCase; i++) {
  let str = input[i];
  let stack = [];
  let result = "YES";

  for (let char of str) {
    if (char === "(") {
      stack.push(0);
    } else {
      if (stack[stack.length - 1] === 0) stack.pop();
      else {
        result = "NO";
        break;
      };
    }
  }

  if (stack.length != 0) {
    result = "NO";
  }
  console.log(result);
}