<template>
  <div class="m-auto max-w-5xl py-5">
    <div class="mx-3 p-3 bg-pale dark:bg-darkPale rounded-md flex flex-wrap">
      <GalleryFilters
        :photo-types="photoTypes"
        :active-type="activeType"
        @update:active-type="($event) => (activeType = $event)"
        class="flex"
      />
      <GalleryColumns
        :gallery="filteredGallery"
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
import { useEventListener } from "@vueuse/core";
import { type Ref, ref, onMounted, computed } from "vue";
import type { Photo } from "@/models/gallery.interface";
import GalleryColumns from "./ui/GalleryColumns.vue";
import GalleryFilters from "./ui/GalleryFilters.vue";
import PhotoItem from "./ui/PhotoItem.vue";
import InfiniteScrolling from "../shared/InfiniteScrolling.vue";

const galleryStore = useGalleryStore();

const activePhoto: Ref<Photo | undefined> = ref(undefined);

const photoTypes: Ref<string[]> = computed(() => {
  return [...new Set(galleryStore.gallery.map((photo) => photo.type))];
});

const activeType: Ref<string> = ref("");

const filteredGallery: Ref<Photo[]> = computed(() => {
  return galleryStore.gallery.filter(
    (photo) => photo.type === activeType.value || activeType.value === ""
  );
});

function getMoreContent() {
  if (galleryStore.next && !galleryStore.loading) {
    galleryStore.getGalleryContent({
      force: true,
      next: true,
      limit: GALLERY_LIMIT,
    });
  }
}

const activePhotoIndex: Ref<number> = computed(() => {
  if (activePhoto.value === undefined) return -1;
  return filteredGallery.value.findIndex(
    (photo) => photo.id === activePhoto.value?.id
  );
});

function handleKeydownGallery(event: KeyboardEvent) {
  if (activePhotoIndex.value === -1) return;

  switch (event.key) {
    case "Escape":
      activePhoto.value = undefined;
      break;
    case "ArrowRight":
      seekGallery(1);
      break;
    case "ArrowLeft":
      seekGallery(-1);
      break;
  }
}

function seekGallery(indexChange: number) {
  let newIndex =
    (activePhotoIndex.value + indexChange + filteredGallery.value.length) %
    filteredGallery.value.length;
  activePhoto.value = filteredGallery.value[newIndex];
}

onMounted(() => {
  galleryStore.getGalleryContent({ force: false, limit: GALLERY_LIMIT });
  useEventListener("keydown", handleKeydownGallery);
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
