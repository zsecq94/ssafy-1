<template>
  <div>
    <h1>LOG IN</h1>

    <form @submit.prevent="logIn">
      <label for="username">USERNAME : </label>
      <input
        type="text"
        id="username"
        v-model="username"
      >
      <br><br><br>

      <label for="password">PASSWORD : </label>
      <input
        type="password"
        id="password"
        v-model="password"
      >
      <br><br><br>

      <input type="submit" value="LOGIN">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Login',
  data: function () {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    logIn: function () {
      const username = this.username
      const password = this.password

      axios({
        method: 'post',
        url: `${API_URL}/api/token/`,
        data: {username, password,},
      })
      .then((res) => {
        localStorage.setItem('jwt', res.data.access)
        this.$emit('login')
        this.$router.push({name: 'TodoList'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
