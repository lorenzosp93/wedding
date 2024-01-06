<template>
  <iframe
    class="w-full"
    :src="videoLink"
    title="Video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
  ></iframe>
</template>

<script setup lang="ts">
defineProps<{ videoLink: string }>();
</script>
