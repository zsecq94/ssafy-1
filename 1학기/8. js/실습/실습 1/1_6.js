// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log(nums[i])
}

// for (const i = 0; i < nums.length; i++) {
// 최초 정의한 i 를 재할당 하면서 사용하기 때문에 const를 사용하면 에러 발생(let으로 교체)

// TypeError: Assignment to constant variable.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}
// for ...in은 속성 이름을 통해 반복하기 때문에 속성 값을 통해 반복하는 of로 교체
// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string