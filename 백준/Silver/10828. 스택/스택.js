let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const testCase = input[0];
let stack = [];

for (let i = 1; i <= testCase; i++) {
  let arr = input[i].split(' ');
  let isEmpty = stack.length === 0 ? 1 : 0;

  switch (arr[0]) {
    case "push":
      stack.push(arr[1]);
      break;
    case "pop":
      if (isEmpty) console.log(-1)
      else console.log(stack.pop());
      break;
    case "size":
      console.log(stack.length);
      break;
    case "empty":
      console.log(isEmpty);
      break;
    case "top":
      if (isEmpty) console.log(-1)
      else console.log(stack[stack.length - 1]);
      break;
  }
}