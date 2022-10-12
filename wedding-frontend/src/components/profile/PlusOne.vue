<template>
  <div @click="toggle" class="z-20 absolute left-0 top-0 backdrop-blur-sm h-screen w-screen">
  </div>
  <div class="z-30 absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2
 rounded-lg max-w-md shadow-md bg-pale dark:bg-darkPale ring-1 ring-accent p-3">
    <form class="flex flex-wrap">

      <label class="w-full ml-3 mt-2" for="email">Email</label>
      <input class="w-full px-2 mx-3 rounded-md bg-neutral dark:bg-darkNeutral" v-model="email" type="email">
      <label class="w-full ml-3 mt-2" for="firstName">First Name</label>
      <input class="w-full px-2 mx-3 rounded-md bg-neutral dark:bg-darkNeutral" v-model="firstName" type="text">
      <label class="w-full ml-3 mt-2" for="lastName">Last Name(s)</label>
      <input class="w-full px-2 mx-3 rounded-md bg-neutral dark:bg-darkNeutral" v-model="lastName" type="text">
      <p v-if="error" class="text-alert">{{ error }}</p>
      <button v-if="!loading & !success" class="px-2 py-1 bg-accent mx-auto rounded-md my-5" @click.prevent="setupPlusOne">Submit</button>
      <p v-if="loading">Loading</p>
      <p v-if="success">Success!</p>
    </form>


  </div>
</template>

<script>
import ApiService from './../../services/api.service';

export default {
  
  name: 'PlusOne',
  data () {
    return {
      email: null,
      firstName: null,
      lastName: null,
      error: null,
      loading: false,
      success: false,
    }
  },
  props: [
    'toggle'
  ],
  methods: {
    setupPlusOne(){
      this.loading = true;
      ApiService.setupPlusOne(this.email, this.firstName, this.lastName).then(
        (response) => {
          if(response.status == 200){
            this.loading = false;
            this.success = true;
            setTimeout(() => this.toggle(), 2000)
          }
        },
        (error) => {
          console.log(error);
          this.loading = false;
          this.error = error.response.data;
        }
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
