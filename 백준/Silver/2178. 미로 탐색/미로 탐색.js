let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, M] = input.shift().split(" ").map((n) => +n);
const map = input.map((row) => row.split('').map(Number));

function bfs(pi, pj) {
  const queue = [[pi, pj]];
  const result = [];
  const visited = {};
  // 현재 위치는 방문했다는 표시
  visited[[pi, pj]] = 1;

  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];

  while (queue.length) {
    for (let i = 0; i < queue.length; i++) {
      let pos = queue.shift();
      result.push(pos);
      for (let j = 0; j < 4; j++) {
        let ni = pos[0] + di[j];
        let nj = pos[1] + dj[j];

        if (ni >= 0 && ni < N && nj >= 0 && nj < M &&
          !visited[[ni, nj]] && map[ni][nj] == 1) {
          // 해당 위치에 도달할 때마다 visited 객체값 증가
          visited[[ni, nj]] = visited[pos] + 1;
          queue.push([ni, nj]);
        }
      }
    }
  }
  // [N, M] 위치에 도달했을 때 visited 객체 값을 반환
  return visited[[N - 1, M - 1]];
}

console.log(bfs(0, 0));