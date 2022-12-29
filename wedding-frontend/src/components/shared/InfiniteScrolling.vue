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

<script lang="ts">
import { ChevronDoubleDownIcon } from "@heroicons/vue/24/outline";
import { debounce, throttle } from "underscore";
import { defineComponent } from "vue";
import LoadingView from "./LoadingView.vue";

export default defineComponent({
  name: "InfiniteScrolling",
  props: {
    loading: { type: Boolean },
    next: { type: String },
  },
  emits: ["getMoreContent"],
  components: {
    ChevronDoubleDownIcon,
    LoadingView,
  },
  mounted() {
    this.setupInfiniteScroll();
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.scrollEventListener());
  },
  methods: {
    getMoreContent() {
      this.$emit("getMoreContent");
    },
    setupInfiniteScroll() {
      window.addEventListener("scroll", this.scrollEventListener());
    },
    scrollEventListener() {
      return debounce(() => {
        let condition =
          window.innerHeight + window.pageYOffset >=
          document.documentElement.offsetHeight;
        if (condition) {
          throttle(
            () => {
              this.getMoreContent();
            },
            500,
            { leading: true }
          )();
        }
      }, 200);
    },
  },
});
</script>
