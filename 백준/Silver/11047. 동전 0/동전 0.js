let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [num, price] = input[0].split(" ").map(Number);
let coins = [];

for (let i = 1; i <= num; i++) {
  if (input[i] <= price) coins.push(Number(input[i]));
}

let count = 0;
for (let i = coins.length - 1; i >= 0; i--) {
  count += Math.floor(price / coins[i]);
  price = price % coins[i];
  // console.log({ '개수': count, '현재금액': price });
}

console.log(count);