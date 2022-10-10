<template>
  <div id="app" class="bg-neutral dark:bg-darkNeutral">
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>
import apiService from './service/api.service';


export default {
  name: 'App',
  components: {
  },
  data () {
    return{
      profile: null,
      requestFactory: null,
    }
  },
  props: [
  ],
  computed: {},
  methods: {
  },
  created () {
    this.token = this.$router.query.get('token');
    localStorage.setItem('token', this.token);
  },
  beforeUnmount () {},
  mounted () {
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
