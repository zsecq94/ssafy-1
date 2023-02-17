    /* 
      1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
      2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
      3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
    */

    // 1-1
    const savedFile = {
      name: 'profile',
      extension: 'jpg',
      size: 29930
    }
    const { name } = savedFile
    const { extension } = savedFile
    const { size } = savedFile
    function fileSummary() {
        console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
    }
    fileSummary();

    // 1-2
    const data = {
      username: 'myName',
      password: 'myPassword',
      email: 'my@mail.com',
    }

    const { username } = data
    const { password } = data
    const { email } = data

    // 2
    function addNumbers(...rest) {
      const numbers = [...rest];
      return numbers.reduce((sum, number) => { 
        return sum + number
      }, 0)
    }
    console.log(addNumbers(1, 2, 3, 4, 5, 6, 7))

    // 3-1
    const defaultColors = ['red', 'green', 'blue'];
    const favoriteColors = ['navy', 'black', 'gold', 'white']
    const myFavoriteColors = [...defaultColors, ...favoriteColors]
    const palette = defaultColors.concat(myFavoriteColors);
    console.log(palette)

    // 3-2
    const info1 = { name: 'Tom', age: 30 }
    const info2 = { ...info1, isMarried: true, balance: 3000 }
    console.log(info2)