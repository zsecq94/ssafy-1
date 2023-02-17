<template>
  <div></div>
</template>

<script>
export default {
  name: 'Logout',
  data() {
    return {}
  },
  methods: {
    logOut() {
      if (localStorage.getItem('jwt')) {
        localStorage.removeItem('jwt')
        this.$router.push({name: 'Login'})
      } else {
        this.$router.push({name: 'Login'})
      }
    }
  },
  created() {
    this.logOut()
  },

}
</script>

<style>

</style>