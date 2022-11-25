<template>
  <div class="m-auto max-w-5xl py-5">
    <div class="mx-3 p-3 bg-pale dark:bg-darkPale rounded-md flex flex-wrap">
      <div class="flex-[100%] sm:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit">
        <div v-for="photo in gallery.filter((_,idx)=>idx%4==0)" :key="photo.id" class="mx-auto w-full cursor-pointer py-1.5" @click="activePhoto = photo">
          <img :src="photo.thumbnail" :alt="`Picture ${photo.id} thumbnail`" class="shadow-lg w-full">
        </div>
      </div>
      <div class="flex-[100%] sm:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit max-lg:md:mt-auto">
        <div v-for="photo in gallery.filter((_,idx)=>idx%4==1)" :key="photo.id" class="mx-auto w-full cursor-pointer py-1.5" @click="activePhoto = photo">
          <img :src="photo.thumbnail" :alt="`Picture ${photo.id} thumbnail`" class="shadow-lg w-full">
        </div>
      </div>
      <div class="flex-[100%] sm:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit">
        <div v-for="photo in gallery.filter((_,idx)=>idx%4==2)" :key="photo.id" class="mx-auto w-full cursor-pointer py-1.5" @click="activePhoto = photo">
          <img :src="photo.thumbnail" :alt="`Picture ${photo.id} thumbnail`" class="shadow-lg w-full">
        </div>
      </div>
      <div class="flex-[100%] sm:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit max-lg:md:mb-auto">
        <div v-for="photo in gallery.filter((_,idx)=>idx%4==3)" :key="photo.id" class="mx-auto w-full cursor-pointer py-1.5" @click="activePhoto = photo">
          <img :src="photo.thumbnail" :alt="`Picture ${photo.id} thumbnail`" class="shadow-lg w-full">
        </div>
      </div>
      <div class="relative flex w-full mx-auto min-h-[50px]">
        <button v-if="next && !loading" class="m-auto px-2 py-1 bg-accent test-primary rounded-md shadow-lg" @click.once="getGalleryContent(true)">{{ $t('thegallery.loadMore') }}</button>
        <loading-view v-if="loading"></loading-view>
      </div>
    </div>
    <div v-if="activePhoto" class="fixed top-0 left-0 w-full h-full">
      <div class="absolute w-fit h-fit top-1/2 left-1/2 z-50 -translate-x-1/2 -translate-y-1/2 p-2 bg-secondary rounded-lg shadow-2xl">
        <img class="max-w-[90vw] max-h-[85vh] rounded-lg" :src="activePhoto.picture" alt="Full-size picture">
      </div>
      <div class="absolute z-40 w-screen h-screen backdrop-blur-sm" @click="activePhoto = null" ></div>
    </div>
  </div>

</template>

<script>
import { mapActions, mapState } from 'pinia';
import { useGalleryStore } from '@/stores/api.store';
import LoadingView from '@/components/shared/LoadingView.vue';


export default {
  name: 'TheGallery',
  components: {
    LoadingView
  },
  props: {
  },
  data () {
    return {
      activePhoto: null,
    }
  },
  computed: {
    ...mapState(useGalleryStore, [
      'gallery',
      'loading',
      'error',
      'next',
    ])
  },
  mounted () {
    this.getGalleryContent();
  },
  beforeUnmount () {
    this.tl?.kill;
  },
  methods: {
    ...mapActions(useGalleryStore, ['getGalleryContent']),
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
