<template>
    <div class="flex flex-col mx-auto max-w-2xl">
      <h1 class="text-xl my-3 font-extrabold">Welcome</h1>
      <div class="max-w-xl mx-auto">
        <div class="max-w-xl my-3 mx-3 p-5 rounded-md bg-pale dark:bg-darkPale ring-1 ring-accent shadow-md">
          <p class="mx-auto mt-2">Hi {{ profile?.user.first_name }},</p>
          <p class="mx-auto mt-2 font-thin">we are delighted to invite you to our wedding in Rome.
            The Eternal City is where we found each other and fell in love, and we would love to have you join us in the celebration!</p>
          <p class="mx-auto mt-2 font-thin">with love,</p>
          <p class="mx-auto mt-2 font-thin">Priscilla and Lorenzo</p>
      </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TheHome',
    data () {
      return {
      }
    },
    props: [
      'authStore',
    ],
    emits: [
    ],
    inject: [
    ],
    computed: {
      profile(){
        return this.authStore.profile
      },
    },
    mounted () {
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>
  