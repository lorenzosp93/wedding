<template>
  <div class="bg-neutral dark:bg-darkNeutral border-2 p-5 mx-3 rounded-2xl">
    <p>{{ $t('auth.loginsuccess.loginWasSuccessful') }}</p>
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
    props: {
    },
    emits: [
    ],
    inject: [
    ],
    computed: {
    },
    mounted () {
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>
  