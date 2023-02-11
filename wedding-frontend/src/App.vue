<template>
  <div id="main">
    <RouterView name="TheNavbar" />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { useRegisterSW } from "virtual:pwa-register/vue";

if ("serviceWorker" in navigator) {
  useRegisterSW({ immediate: true });
}
</script>

<style></style>
