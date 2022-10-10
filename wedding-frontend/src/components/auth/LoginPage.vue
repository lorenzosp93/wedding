<template>
  <div class="bg-gray-200 border-2 p-10 m-20 rounded-2xl">
      <h1>{{ $t('auth.loginpage.loginPage') }}</h1>
      <form class="" action="">
        <label class="" for="email_input">{{ $t('auth.loginpage.emailAddress') }}</label>
        <input class="flex bg-gray-600 border-2 border-white rounded-md mx-auto" id="email_input" type="email">
        <button class="flex border-2 border-white mx-auto my-4 px-2 py-1 rounded-lg" type="submit">{{ $t('auth.loginpage.submit') }}</button>
      </form>
    </div>
</template>
  
  <script>
  export default {
    name: 'LoginPage',
    data () {
      return {
        data: [
          'loading'
        ],
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
      handleLogin(email){
        this.loading = true;
        this.$store.dispatch("auth/login", email).then(
          ()=>{},
          (error) => {
            this.loading = false;
            this.message = (error.response &&
              error.response.data &&
              error.response.data.message) ||
              error.message ||
              error.toString();
          })
      }
    },
    mounted () {
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>
  