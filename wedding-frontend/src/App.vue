<template>
  <div class="" >
    <the-navbar />
    <router-view />
  </div>
</template>

<script>
import TheNavbar from './components/shared/TheNavbar.vue'

export default {
  name: 'App',
  components: {
    TheNavbar,
  },
  data () {
    return{
    }
  },
  computed: {},
  methods: {},
  created () {},
  beforeUnmount () {},
  mounted () {},
  provide () {
    return {}
  },
}
</script>

<style>
</style>
