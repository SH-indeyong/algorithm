// 셀프 넘버가 아닌 숫자를 가려내는 함수
function d(n) {
  let num = n;
  let result = 0;

  for (let i = 0; i < String(n).length; i++) {
    result += num % 10;
    num = Math.floor(num / 10);
  }

  return result + n;
}

const range = 10000;
let selfNumbers = Array(range + 1).fill(true);

for (let i = 0; i <= range; i++) {
  selfNumbers[d(i)] = false;
}

for (let i = 1; i <= range; i++) {
  if (selfNumbers[i]) console.log(i);
}