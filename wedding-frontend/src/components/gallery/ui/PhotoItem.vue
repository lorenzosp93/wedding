<template>
  <div class="fixed top-0 left-0 w-full h-full">
    <div
      class="absolute w-fit h-fit top-1/2 left-1/2 z-50 -translate-x-1/2 -translate-y-1/2 p-2 bg-secondary rounded-lg shadow-2xl"
    >
      <img
        v-on-click-outside="$emit('closePhoto')"
        class="max-w-[90vw] max-h-[80vh] rounded-lg"
        :src="activePhoto?.picture"
        alt="Full-size picture"
      />
    </div>
    <div
      class="absolute z-40 w-screen h-screen backdrop-blur-sm cursor-pointer"
      data-test="outside"
    ></div>
  </div>
</template>

<script lang="ts">
import type { Photo } from "@/models/gallery.interface";
import { defineComponent, type PropType } from "vue";
import { vOnClickOutside } from "@vueuse/components";

export default defineComponent({
  name: "PhotoItem",
  props: {
    activePhoto: { type: Object as PropType<Photo> },
  },
  emits: ["closePhoto"],
});
</script>
