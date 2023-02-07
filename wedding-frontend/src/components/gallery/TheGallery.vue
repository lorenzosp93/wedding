<template>
  <div class="m-auto max-w-5xl py-5">
    <div class="mx-3 p-3 bg-pale dark:bg-darkPale rounded-md flex flex-wrap">
      <GalleryColumns
        :gallery="galleryStore.gallery"
        @activate-photo="
          (photo) => {
            activePhoto = photo;
          }
        "
      />
      <InfiniteScrolling
        @get-more-content="getMoreContent"
        :next="galleryStore.next ?? undefined"
        :loading="galleryStore.loading"
        class="m-auto cursor-pointer"
      />
    </div>
    <PhotoItem
      @close-photo="activePhoto = undefined"
      v-if="activePhoto"
      :activePhoto="activePhoto"
      class="fixed top-0 left-0 w-full h-full"
    />
  </div>
</template>

<script setup lang="ts">
import { useGalleryStore, GALLERY_LIMIT } from "@/stores";
import { type Ref, ref, onMounted } from "vue";
import type { Photo } from "@/models/gallery.interface";
import GalleryColumns from "./ui/GalleryColumns.vue";
import PhotoItem from "./ui/PhotoItem.vue";
import InfiniteScrolling from "../shared/InfiniteScrolling.vue";

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
