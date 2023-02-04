<template>
  <div
    class="mx-auto w-full cursor-pointer my-3 rounded-md overflow-hidden shadow-sm"
  >
    <img
      :src="photo?.thumbnail"
      :alt="`Picture ${photo?.id} thumbnail`"
      class="w-full"
    />
    <div
      v-if="photo?.content"
      class="bg-neutral dark:bg-darkNeutral dark:text-secondary px-3 py-3"
      test-data="content"
    >
      {{ photo.content }}
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Photo } from "@/models/gallery.interface";
import { type PropType } from "vue";
defineProps({
  photo: { type: Object as PropType<Photo> },
});
</script>
