    // 이곳에 코드를 작성합니다.
    const inputs = [
      [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
      [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
      [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
    ]

    function solution(K, N, M, chargers) {
      let bus = 0
      let cnt = 0
      while (bus+K < N) {
        bus += K
        if (chargers.includes(bus)) {
          cnt += 1
        } else {
          a = 1
          while (a != K) {
            bus -= 1
            if (chargers.includes(bus)) {
              cnt += 1
              break
            }
            a += 1
          }
        }
      }
      if (a == K) {
        cnt = 0
        return console.log(cnt)
      } else {
        console.log(cnt)
      }
    }

    for (const input of inputs) {
      solution(input[0], input[1], input[2], input[3])
    }