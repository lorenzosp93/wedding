<template>
  <div id="app" class="bg-neutral dark:bg-darkNeutral">
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data () {
    return{
      profile: null,
    }
  },
  computed: {},
  methods: {
    loadData: (url, self, isPaginated) => {
      self.isLoading = true;
      let backendUrl = process.env.VUE_APP_BACKEND_URL;
      return fetch(backendUrl + url).then(
        response => {
          if (response.ok) {
            return response.json();
          }
          else if (response.status == '401') {
            this.$router.push("landing")
          }
        }
      ).then(
        data => {
          if (data) {
            self.isLoading = false;
            if (isPaginated) {
              self.total = data.count;
              self.data.push(...data.results);
            } else {
              self.data = data;
            }
          }
        }
      ).catch(
        error => {
          self.isLoading = false;
          self.error = "Something went wrong when loading the site data...";
          console.log(error);
        }
      )
    },
    loadProfile: {
      this.loadData(url='/api/user/profile', self)
    }
  },
  created () {
    this.loadData('', )
  },
  beforeUnmount () {},
  mounted () {},
  provide () {
    return {}
  },
}
</script>

<style>
</style>
