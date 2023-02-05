<template>
  <div class="m-auto max-w-5xl py-5">
    <div class="mx-3 p-3 bg-pale dark:bg-darkPale rounded-md flex flex-wrap">
      <div
        v-for="col in 4"
        :key="col"
        class="flex-[100%] md:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit"
        data-test="gallery-cols"
      >
        <thumbnail-item
          v-for="photo in galleryStore.gallery.filter((_,idx:number)=>{ return idx%(breakpoint == 'md' ? 1 : breakpoint == 'lg' ? 2 : 4) == col - 1 })"
          :key="photo.id"
          :photo="photo"
          @click="activePhoto = photo"
        />
      </div>
      <infinite-scrolling
        @get-more-content="getMoreContent"
        :next="galleryStore.next ?? undefined"
        :loading="galleryStore.loading"
        class="m-auto cursor-pointer"
      />
    </div>
    <photo-item
      @close-photo="activePhoto = undefined"
      v-if="activePhoto"
      :activePhoto="activePhoto"
      class="fixed top-0 left-0 w-full h-full"
    ></photo-item>
  </div>
</template>

<script setup lang="ts">
import { useGalleryStore, GALLERY_LIMIT } from "@/stores";
import { type Ref, ref, onMounted } from "vue";
import type { Photo } from "@/models/gallery.interface";
import ThumbnailItem from "./ui/ThumbnailItem.vue";
import PhotoItem from "./ui/PhotoItem.vue";
import InfiniteScrolling from "../shared/InfiniteScrolling.vue";
import { useBreakpoints } from "@/components/composables/breakpoints";

const breakpoint = useBreakpoints();

const galleryStore = useGalleryStore();

const activePhoto: Ref<Photo | undefined> = ref(undefined);

function getMoreContent() {
  if (galleryStore.next && !galleryStore.loading) {
    galleryStore.getGalleryContent({
      force: true,
      next: true,
      limit: GALLERY_LIMIT,
    });
  }
}

onMounted(() => {
  galleryStore.getGalleryContent({ force: false, limit: GALLERY_LIMIT });
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
