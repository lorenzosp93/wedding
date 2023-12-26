<template>
  <div class="fixed top-0 left-0 w-full h-full">
    <OnClickOutside
      @trigger="$emit('closePhoto')"
      class="absolute w-fit h-fit top-1/2 left-1/2 z-50 -translate-x-1/2 -translate-y-1/2 rounded-lg shadow-xl"
      :style="{
        background: `url(${activePhoto?.thumbnail})`,
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
      }"
    >
      <LoadingView v-show="!isLoaded" />
      <img
        class="max-w-[90vw] max-h-[80vh] rounded-lg"
        :src="activePhoto?.picture"
        :alt="`Full-size picture of the ${activePhoto?.type}`"
        @load="() => (isLoaded = true)"
        loading="lazy"
      />
    </OnClickOutside>
    <div
      class="absolute z-40 w-screen h-screen backdrop-blur-sm cursor-pointer"
      data-test="outside"
    ></div>
  </div>
</template>

<script setup lang="ts">
import type { Photo } from "@/models/gallery.interface";
import LoadingView from "@/components/shared/LoadingView.vue";
import { ref, type PropType, watch } from "vue";
import { OnClickOutside } from "@vueuse/components";

const props = defineProps({
  activePhoto: { type: Object as PropType<Photo> },
});

const isLoaded = ref(false);

watch(
  () => props.activePhoto,
  () => {
    isLoaded.value = false;
  }
);

defineEmits(["closePhoto"]);
</script>
