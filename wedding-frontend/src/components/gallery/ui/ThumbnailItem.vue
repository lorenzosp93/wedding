<template>
  <div
    class="mx-auto w-full cursor-pointer my-3 rounded-md overflow-hidden shadow-lg"
  >
    <img
      :src="photo?.thumbnail"
      :alt="`Picture ${photo?.id} thumbnail`"
      class="w-full"
    />
    <div
      v-if="photo?.content"
      class="bg-neutral dark:bg-darkNeutral dark:text-secondary px-3 py-3"
    >
      {{ photo.content }}
    </div>
  </div>
</template>

<script lang="ts">
import type { Photo } from "@/models/gallery.interface";
import { defineComponent, type PropType } from "vue";

export default defineComponent({
  name: "ThumbnailItem",
  props: {
    photo: { type: Object as PropType<Photo> },
  },
});
</script>
