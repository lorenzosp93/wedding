<template>
  <div class="bg-gray-200 border-2 p-10 m-20 rounded-2xl">
      <h1>{{ $t('auth.loginpage.loginPage') }}</h1>
      <form class="">
        <label class="" for="email_input">{{ $t('auth.loginpage.emailAddress') }}</label>
        <input v-model="email" class="flex bg-gray-600 border-2 border-white rounded-md mx-auto" id="email_input" type="email">
        <button @click.prevent="handleLogin(email)" class="flex border-2 border-white mx-auto my-4 px-2 py-1 rounded-lg" type="submit">{{ $t('auth.loginpage.submit') }}</button>
      </form>
  </div>
</template>

<script>
import AuthService from '../../services/auth.service'

export default {
name: 'LoginPage',
data () {
  return {
    data: {
      'loading': false,
      'email': ''
    },
  }
},
props: {
},
emits: [
],
inject: [
],
computed: {
},
methods: {
  handleLogin(email) {
    this.loading = true;
    AuthService.login(email).then(
      (data) => console.log(data)
    ).catch(
      (error) => console.log(error)
    )
  }
},
mounted () {
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
