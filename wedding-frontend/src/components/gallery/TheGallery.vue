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
      <div v-show="loading || next" class="relative flex w-full mx-auto min-h-[50px]">
        <div v-show="next" class="m-auto">
          <svg class="h-10 w-10 block m-auto pt-3.5 animate-bounce fill-secondary dark:fill-darkNeutral" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 1000 1000" xml:space="preserve">
              <g>
                <path
                  d="M34.6,228.4L472,481c8.8,5.1,18.5,7.1,28,6.4c9.5,0.7,19.2-1.3,28-6.4l437.4-252.6c23.7-13.7,31.6-44.3,17.7-68.4c-13.9-24.1-44.4-32.5-68.1-18.8L500,380.9L84.9,141.2C61.2,127.5,30.8,136,16.9,160C2.9,184.1,10.9,214.7,34.6,228.4z" />
                <path
                  d="M915.1,519L500,758.7L84.9,519c-23.7-13.7-54.2-5.2-68.1,18.8c-13.9,24.1-6,54.7,17.7,68.4L472,858.8c8.8,5.1,18.5,7.1,28,6.4c9.5,0.7,19.2-1.3,28-6.4l437.4-252.6c23.7-13.7,31.6-44.3,17.7-68.4C969.2,513.8,938.8,505.4,915.1,519z" />
              </g>
          </svg>
        </div>
        <loading-view v-show="loading"></loading-view>
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
import { debounce, throttle } from 'underscore';
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
    this.setupInfiniteScroll();
  },
  beforeUnmount () {
    this.tl?.kill;
  },
  methods: {
    ...mapActions(useGalleryStore, ['getGalleryContent']),
    getMoreGalleryContent () {
      if (this.next) {
        this.getGalleryContent(true);
      };
    },
    setupInfiniteScroll () {
      window.onscroll = debounce(() => {
        let condition = window.innerHeight + window.pageYOffset >= document.documentElement.offsetHeight;
        if (condition) {
          throttle(()=>{
            this.getMoreGalleryContent();
          }, 500, {leading: true})();
        }
      }, 300)
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
