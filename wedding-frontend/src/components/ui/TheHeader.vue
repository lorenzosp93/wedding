<template>
  <div class="flex">
    <img
      class="mx-auto pt-3 px-5 max-w-lg w-full"
      :src="logo"
      aria-label="P & L logo"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const logo = ref(
  new URL("@/assets/logo_long.svg", import.meta.url).href as string
);
</script>
