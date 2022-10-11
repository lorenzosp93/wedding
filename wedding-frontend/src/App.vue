<template>
  <div id="app" class="bg-neutral dark:bg-darkNeutral">
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>
import apiService from './services/api.service';


export default {
  name: 'App',
  components: {
  },
  data () {
    return{
      profile: null,
    }
  },
  props: [
  ],
  computed: {},
  methods: {
  },
  created () {
  },
  beforeUnmount () {},
  mounted () {
    if (this.token) {
      apiService.getProfileContent().then(
        (response) => {
          this.profile = response.data;
        },
        (error) => {
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      )
    }
  },
  provide () {
    return {
      profile: this.profile
    }
  },
}
</script>

<style>
</style>
