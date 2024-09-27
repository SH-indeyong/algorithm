let fs = require('fs');
let num = fs.readFileSync('/dev/stdin').toString();

// 두 자릿수까지의 수는 한수의 개수와 같음
if (num < 100) return console.log(num);

let hansu = 99;
for (let i = 100; i <= num; i++) {
  let isHansu = true;
  const arr = i.toString().split("").map(Number);

  for (let j = 1; j < arr.length - 1; j++) {
    if (arr[j] - arr[j - 1] != arr[j + 1] - arr[j]) {
      isHansu = false;
      break;
    };
  }
  if (isHansu) hansu++;
}
console.log(hansu);