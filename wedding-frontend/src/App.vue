<template>
  <div id="main">
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "App",
});
</script>

<style></style>
