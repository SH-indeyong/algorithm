let fs = require('fs');
let [N, M] = fs.readFileSync('/dev/stdin').toString().split(" ").map(v => +v);

function solution(N, M) {
  // 소수 여부를 저장하는 배열
  let isPrime = Array(M + 1).fill(true);
  isPrime[0] = isPrime[1] = false;

  // 2부터 √M 까지의 모든 숫자에 대해 처리
  for (let i = 2; i * i <= M; i++) {
    if (isPrime[i]) {
      // i의 배수들을 소수가 아니라고 표시
      for (let j = i * i; j <= M; j += i) {
        isPrime[j] = false;
      }
    }
  }

  // N부터 M까지의 숫자 중에서 소수인 숫자 출력
  for (let i = N; i <= M; i++) {
    if (isPrime[i]) {
      console.log(i);
    }
  }
}

solution(N, M);
