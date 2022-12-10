<template>
  <div id="main" class="min-h-screen bg-neutral dark:bg-darkNeutral text-primary dark:text-darkPrimary font-serif bg-[url('@/assets/backdrop.webp')] bg-repeat-y bg-scroll bg-contain">
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
</style>
