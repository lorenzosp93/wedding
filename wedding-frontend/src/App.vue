<template>
  <div id="app" class="">
    <router-view name="TheNavbar"></router-view>
    <router-view :authStore="authStore"></router-view>
  </div>
</template>

<script>
import { mapStores } from 'pinia'
import { useAuthStore } from '@/stores'


export default {
  name: 'App',
  components: {
  },
  data () {
    return{
    }
  },
  props: [
  ],
  computed: {
    ...mapStores(useAuthStore),
  },
  methods: {
  },
  created () {
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
