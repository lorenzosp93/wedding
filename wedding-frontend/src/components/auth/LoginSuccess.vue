<template>
  <div class="py-5 flex">
    <div class="bg-pale dark:bg-darkPale border-2 p-5 rounded-2xl mx-auto" >
      <p>{{ $t('auth.loginsuccess.loginWasSuccessful') }}</p>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: 'LoginSuccess',
    data () {
      return {
        data: [],
      }
    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>
  