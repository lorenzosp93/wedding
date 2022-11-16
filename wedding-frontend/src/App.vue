<template>
  <div id="app" class="font-serif">
    <ReloadPWA />
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>
import ReloadPWA from '@/components/shared/ReloadPWA.vue'

export default {
  name: 'App',
  components: {
    ReloadPWA
  },
}
</script>

<style>
</style>
