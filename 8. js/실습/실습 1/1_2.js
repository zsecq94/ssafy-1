function palindrome(str) {
  let str1 = reversed(str)
  return str === str1
}

function reversed(str) {
  let reversed = '';
  for(let i = str.length - 1; i >= 0; i--) {
    reversed = reversed + str[i];
  }
  return reversed;
};

console.log(palindrome('level'))
console.log(palindrome('hi'))



// 출력
// palindrome('level') => true
// palindrome('hi') => false
