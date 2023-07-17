<template>
  <div id="main">
    <RouterView name="TheNavbar" />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { registerSW } from "virtual:pwa-register";

registerSW({ immediate: true });
</script>

<style></style>
