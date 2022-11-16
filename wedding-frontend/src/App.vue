<template>
  <div id="app" class="font-serif">
    <ReloadPWA />
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
}
</script>

<style>
</style>
