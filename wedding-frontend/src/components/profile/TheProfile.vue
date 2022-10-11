<template>
  <div class="">
    <p>{{ $t('profile.theprofile.someProfileContent') }}</p>
    <h1>{{ profile.user.first_name }}</h1>
    <h1>{{ profile.user.last_name }}</h1>
    <h1>{{ profile.user.email }}</h1>
    <h1>{{ profile.plusone }}</h1>
    <h1>{{ profile.language }}</h1>

    
  </div>
</template>

<script>
export default {
  
  name: 'TheProfile',
  data () {
    return {
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
    'profile'
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
