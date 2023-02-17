<template>
  <div>
    <h1>SIGN UP</h1>

    <form @submit.prevent="signUp">
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

      <label for="password_check">PASSWORD AGAIN : </label>
      <input
        type="password"
        id="password_check"
        v-model="password_check"
      >
      <br><br><br>
      <input type="submit" value="JOIN">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Signup',
  data: function () {
    return {
      username: null,
      password: null,
      password_check: null,
    }
  },
  methods: {
    signUp: function () {
      const username = this.username
      const password = this.password
      const password_check = this.password_check

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {username, password, password_check},
      })
      .then(() => {
        this.$router.push({name: 'Login'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
