<template>
  <div id="app">
    <div id="nav">
      <span>
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
      </span>
      <span>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> |
        <router-link :to="{ name: 'Logout' }">Logout</router-link>

      </span>
    </div>
    <router-view
      @login="logIn"
    />
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLoggedIn: false,
    }
  },
  methods: {
    logIn() {
      this.isLoggedIn = true
    },
    checkJWT() {
      if (localStorage.getItem('jwt')) {
        this.isLoggedIn = true
      }
    }
  },
  created() {
    this.checkJWT()
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
