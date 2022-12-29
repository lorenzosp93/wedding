<template>
  <div class="m-auto max-w-5xl py-5">
    <div class="mx-3 p-3 bg-pale dark:bg-darkPale rounded-md flex flex-wrap">
      <div
        v-for="col in 4"
        :key="col"
        class="flex-[100%] md:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit"
      >
        <thumbnail-item
          v-for="photo in gallery.filter((_,idx:number)=>{ return idx%(breakpoint == 'md' ? 1 : breakpoint == 'lg' ? 2 : 4) == col - 1 })"
          :key="photo.id"
          :photo="photo"
          @click="activePhoto = photo"
        />
      </div>
      <div
        v-show="loading || next"
        class="relative flex w-full mx-auto min-h-[50px]"
      >
        <div
          v-show="next && !loading"
          @click="getMoreGalleryContent"
          class="m-auto cursor-pointer"
        >
          <chevron-double-down-icon
            class="h-10 w-10 md:h-12 md:w-12 pt-3.5 animate-bounce stroke-accent stroke-2"
          />
        </div>
        <loading-view v-show="loading"></loading-view>
      </div>
    </div>
    <photo-item
      @close-photo="activePhoto = null"
      v-if="activePhoto"
      :activePhoto="activePhoto"
      class="fixed top-0 left-0 w-full h-full"
    ></photo-item>
  </div>
</template>

<script lang="ts">
import { debounce, throttle } from "underscore";
import { mapActions, mapState } from "pinia";
import { useGalleryStore } from "@/stores/api.store";
import LoadingView from "@/components/shared/LoadingView.vue";
import { ChevronDoubleDownIcon } from "@heroicons/vue/24/outline";
import { defineComponent } from "vue";
import type { Photo } from "@/models/listObjects.interface";
import ThumbnailItem from "./ui/ThumbnailItem.vue";
import PhotoItem from "./ui/PhotoItem.vue";

const GALLERY_LIMIT = 16; // images per load

type Breakpoint = {
  name: "sm" | "md" | "lg" | "xl";
  value: number;
};

export default defineComponent({
  name: "TheGallery",
  components: {
    LoadingView,
    ChevronDoubleDownIcon,
    ThumbnailItem,
    PhotoItem,
  },
  props: {},
  data() {
    return {
      activePhoto: null as Photo | null,
      breakpointMap: [
        { name: "md", value: 768 },
        { name: "lg", value: 1024 },
      ] as Array<Breakpoint>,
      breakpoint: "xl" as string,
    };
  },
  computed: {
    ...mapState(useGalleryStore, ["gallery", "loading", "error", "next"]),
  },
  mounted() {
    this.getGalleryContent({ force: false, galleryLimit: GALLERY_LIMIT });
    this.setupGalleryColumns();
    this.updateBreakpoint();
    this.setupInfiniteScroll();
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.scrollEventListener());
    window.removeEventListener("resize", this.resizeEventListener());
  },
  methods: {
    ...mapActions(useGalleryStore, ["getGalleryContent"]),
    getMoreGalleryContent() {
      if (this.next && !this.loading) {
        this.getGalleryContent({ force: true, galleryLimit: GALLERY_LIMIT });
      }
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
              this.getMoreGalleryContent();
            },
            500,
            { leading: true }
          )();
        }
      }, 200);
    },
    setupGalleryColumns() {
      window.addEventListener("resize", this.resizeEventListener());
    },
    resizeEventListener() {
      return debounce(() => {
        this.updateBreakpoint();
      }, 100);
    },
    updateBreakpoint() {
      this.breakpoint =
        this.breakpointMap.find((bp) => bp.value >= window.innerWidth)?.name ??
        "xl";
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
