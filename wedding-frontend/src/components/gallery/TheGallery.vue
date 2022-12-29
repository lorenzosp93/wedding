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
      <infinite-scrolling
        @get-more-content="getMoreContent"
        :next="next ?? undefined"
        :loading="loading"
        class="m-auto cursor-pointer"
      />
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
import { debounce } from "underscore";
import { mapActions, mapState } from "pinia";
import { useGalleryStore } from "@/stores/api.store";
import LoadingView from "@/components/shared/LoadingView.vue";
import { defineComponent } from "vue";
import type { Photo } from "@/models/gallery.interface";
import ThumbnailItem from "./ui/ThumbnailItem.vue";
import PhotoItem from "./ui/PhotoItem.vue";
import InfiniteScrolling from "../shared/InfiniteScrolling.vue";
import { GALLERY_LIMIT } from "@/stores/api.store";

type Breakpoint = {
  name: "sm" | "md" | "lg" | "xl";
  value: number;
};

export default defineComponent({
  name: "TheGallery",
  components: {
    LoadingView,
    InfiniteScrolling,
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
    this.getGalleryContent({ force: false, limit: GALLERY_LIMIT });
    this.setupGalleryColumns();
    this.updateBreakpoint();
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.resizeEventListener());
  },
  methods: {
    ...mapActions(useGalleryStore, ["getGalleryContent"]),
    getMoreContent() {
      if (this.next && !this.loading) {
        this.getGalleryContent({
          force: true,
          next: true,
          limit: GALLERY_LIMIT,
        });
      }
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
