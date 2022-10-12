<template>
  <div id="app" class="">
    <router-view name="TheNavbar"></router-view>
    <router-view :profile="profile" :loading="loading"></router-view>
  </div>
</template>

<script>
import ApiService from './services/api.service';


export default {
  name: 'App',
  components: {
  },
  data () {
    return{
      profile: null,
      error: null,
      loading: false,
    }
  },
  props: [
  ],
  computed: {},
  methods: {
    getProfile(){
      return ApiService.getProfileContent().then(
        (response) => {
          this.profile = response.data[0];
        },
      )
    }
  },
  created () {
    this.token = localStorage.getItem('token');
    if (this.token && !this.profile) {
      this.loading = true;
      this.getProfile().then(() => {
        this.loading = false
      }
      );
    }
  },
  beforeUnmount () {},
  beforeMount() {
  },
  mounted () {
  },
  provide () {
    return {
    }
  },
}
</script>

<style>
</style>
