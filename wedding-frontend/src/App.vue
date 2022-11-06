<template>
  <div id="app" class="">
    <router-view name="TheNavbar"></router-view>
    <router-view v-if="!authStore.loading" :authStore="authStore"></router-view>
    <loading-view class="m-auto" v-if="authStore.loading" />
  </div>
</template>

<script>
import { mapStores } from 'pinia'
import { useAuthStore } from '@/stores'
import LoadingView from './components/shared/LoadingView.vue'


export default {
  name: 'App',
  components: {
    LoadingView
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
