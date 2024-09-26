let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const testCase = input[0];
let count = 0;

for (let i = 1; i <= testCase; i++) {
  let arr = input[i].split('');
  let alpha = new Set();
  let isGroup = true;
  alpha.add(arr[0])

  for (let i = 1; i <= arr.length; i++) {
    // 연속된 알파벳인 경우 예외 처리
    if (arr[i] === arr[i - 1]) continue;

    if (!alpha.has(arr[i])) alpha.add(arr[i]);
    else {
      isGroup = false;
      break;
    }
  }
  if (isGroup === true) count++;
}

console.log(count);