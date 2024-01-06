<template>
  <iframe
    class="w-full"
    :src="`${videoLink}?quality=high&modestbranding=1&playsinline=1&loop=1`"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
  ></iframe>
</template>

<script setup lang="ts">
defineProps<{ videoLink: string }>();
</script>
