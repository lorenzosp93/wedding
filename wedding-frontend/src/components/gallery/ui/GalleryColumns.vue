<template>
  <div
    v-for="col in 4"
    :key="col"
    class="flex-[100%] md:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit"
    data-test="gallery-cols"
  >
    <ThumbnailItem
      v-for="photo in gallery?.filter((_,idx:number)=>{ return idx%(breakpoint == 'md' ? 1 : breakpoint == 'lg' ? 2 : 4) == col - 1 })"
      :key="photo.id"
      :photo="photo"
      @click="emit('activatePhoto', photo)"
    />
  </div>
</template>

<script setup lang="ts">
import { useBreakpoints } from "@/components/composables/breakpoints";
import ThumbnailItem from "./ThumbnailItem.vue";
import type { Photo } from "@/models/gallery.interface";

const breakpoint = useBreakpoints();

const emit = defineEmits(["activatePhoto"]);
defineProps({
  gallery: { type: Array<Photo> },
});
</script>
