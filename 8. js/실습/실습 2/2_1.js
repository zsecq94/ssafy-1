      /* 
        1. 해당 코드를 template string 을 활용하여 리팩토링하시오.
        2. 해당 코드를 arrow function 으로 리팩토링하시오.
        3. 해당 코드의 메서드 introduce 를 function 키워드 없이 리팩토링하시오.
        4. 해당 코드를 key, value를 한번씩만 작성하도록 리팩토링하시오.
      */

      // 1
      // const name = 'Tom'
      // console.log('Hi, my name is' + name)

      const name = 'Tom'
      const message = `Hi, my name is ${name}`
      console.log(message)

      // 2
      // function add(x, y) {
      //   return x + y
      // }

      const add = (x, y) => {
        return x + y
      }
      console.log(add(3, 6))

      // 3
      // const tom = {
      //   name: 'Tom',
      //   introduce: function () {
      //     console.log('Hi, my name is' + this.name)
      //   }
      // }

      const tom = {
        name: 'Tom',
        introduce() {
          console.log('Hi, my name is ' + this.name)
        }
      }
      tom.introduce()

      // 4
      // const url = 'https://test.com'
      // const data = { message: 'Hello World!' }

      // const request = { url: url, data: data }
      // console.log(request)

      const url = 'https://test.com'
      const data = { message: 'Hello World!' }

      const request = { url, data }
      console.log(request)