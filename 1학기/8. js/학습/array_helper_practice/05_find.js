// 1. people에서 admin 권한을 가진 요소를 찾으세요.
const people = [
  { id: 1, admin: false },
  { id: 2, admin: false },
  { id: 3, admin: true },
]

// answer
const result = people.find((V) => {return V.admin === true})
console.log(result)



// 2. accounts에서 잔액이 24,000인 사람을 찾으세요.
const accounts = [
  { name: 'justin', balance: 1200 },
  { name: 'harry', balance: 50000 },
  { name: 'jason', balance: 24000 },
]

// answer
const result1 = accounts.find((account) => {return account.balance === 24000})
console.log(result1)