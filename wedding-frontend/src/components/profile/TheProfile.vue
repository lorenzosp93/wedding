<template>
    <div class="">
      <p>{{ $t('profile.theprofile.someProfileContent') }}</p>
      
    </div>
  </template>
  
  <script>
  export default {
    name: 'TheProfile',
    data () {
      return {
        data: [],
      }
    },
    props: {
    },
    methods: {
      getProfile() {
        this.$http.get(

        )
      }
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
  