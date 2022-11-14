<template>
  <div class="py-5">
    <div class="bg-pale dark:bg-darkPale border-2 p-5 mx-3 rounded-2xl text-primary dark:text-darkPrimary">
      <h1 class="text-xl font-bold my-2 ">{{ $t('auth.loginpage.loginPage') }}</h1>
      <form class="flex flex-col">
        <label class="block mx-auto my-2" for="email_input">{{ $t('auth.loginpage.emailAddress') }}</label>
        <input v-model="email" class="block bg-neutral dark:bg-darkNeutral rounded-md mx-auto px-2 w-full max-w-xs" id="email_input" type="email">
        <button v-if="!loading" @click.prevent="handleLogin(email)" class="flex border-2 border-white mx-auto my-4 px-2 py-1 rounded-lg bg-neutral dark:bg-darkNeutral" type="submit">{{ $t('auth.loginpage.submit') }}</button>
        <div v-if="loading" class="relative w-10 h-10 my-1 mx-auto">
          <loading-view >{{ $t('auth.loginpage.loading') }}</loading-view>
        </div>
        <p v-if="!!error" class="text-alert font-bold text-sm mx-auto py-2">{{ $t('auth.loginpage.thereWasAn', { 'a': JSON.stringify(error) }) }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import LoginService from '@/services/login.service'
import LoadingView from '@/components/shared/LoadingView';

export default {
name: 'LoginPage',
components: {
  LoadingView
},
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
        this.loading = false;
        this.error = error.response?.data ?? "Unable to return response";
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
