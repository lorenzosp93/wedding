<template>
  <div
    v-show="loading || next"
    class="relative flex w-full mx-auto min-h-[50px]"
  >
    <div
      v-show="next && !loading"
      @click="getMoreContent"
      class="m-auto cursor-pointer"
    >
      <chevron-double-down-icon
        class="h-10 w-10 md:h-12 md:w-12 pt-3.5 animate-bounce stroke-accent stroke-2"
      />
    </div>
    <loading-view v-show="loading"></loading-view>
  </div>
</template>

<script setup lang="ts">
import { ChevronDoubleDownIcon } from "@heroicons/vue/24/outline";
import { onMounted } from "vue";
import LoadingView from "./LoadingView.vue";
import { useEventListener } from "@vueuse/core";
import { useDebounceFn, useThrottleFn } from "@vueuse/core";

defineProps({
  loading: { type: Boolean },
  next: { type: String },
});
const emit = defineEmits(["getMoreContent"]);

onMounted(() => {
  setupInfiniteScroll();
});

function getMoreContent() {
  emit("getMoreContent");
}

function setupInfiniteScroll() {
  useEventListener("scroll", scrollEventListener());
}

function scrollEventListener() {
  return useDebounceFn(() => {
    let condition =
      window.innerHeight + window.pageYOffset >=
      document.documentElement.offsetHeight;
    if (condition) {
      useThrottleFn(
        () => {
          getMoreContent();
        },
        500,
        false,
        true
      )();
    }
  }, 200);
}
</script>
