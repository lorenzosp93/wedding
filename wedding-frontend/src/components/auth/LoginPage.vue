<template>
  <div class="bg-pale dark:bg-darkPale border-2 p-10 m-20 rounded-2xl text-primary dark:text-darkPrimary">
      <h1 class="text-xl font-bold my-2 ">{{ $t('auth.loginpage.loginPage') }}</h1>
      <form class="flex flex-col">
        <label class="block mx-auto" for="email_input">{{ $t('auth.loginpage.emailAddress') }}</label>
        <input v-model="email" class="block bg-neutral dark:bg-darkNeutral border-2 border-white rounded-md mx-auto px-2 " id="email_input" type="email">
        <p v-if="!!error" class="text-alert font-bold mx-auto">There was an error sending you the access code: {{ error }}</p>
        <button v-if="!loading" @click.prevent="handleLogin(email)" class="flex border-2 border-white mx-auto my-4 px-2 py-1 rounded-lg bg-neutral dark:bg-darkNeutral" type="submit">{{ $t('auth.loginpage.submit') }}</button>
        <p v-else>Loading</p>
      </form>
  </div>
</template>

<script>
import LoginService from '@/services/login.service'

export default {
name: 'LoginPage',
data () {
  return {
    loading: false,
    email: '',
    error: null,
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
    LoginService.login(email)
    .catch(
      (error) => {
        this.error = error.response?.data?.detail ?? "Unable to return response";
      }
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
