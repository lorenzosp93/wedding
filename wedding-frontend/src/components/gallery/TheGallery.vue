<template>
  <div class="m-auto max-w-5xl py-5">
    <div class="mx-3 p-3 bg-pale dark:bg-darkPale rounded-md flex flex-wrap">
      <div v-for="col in 4" :key="col" class="flex-[100%] md:flex-[50%] lg:flex-[25%] max-w-full md:max-w-[50%] lg:max-w-[25%] px-1.5 h-fit">
        <div v-for="photo in gallery.filter((_,idx)=>{ return idx%(breakpoint == 'md' ? 1 : breakpoint == 'lg' ? 2 : 4) == col - 1 })" :key="photo.id" class="mx-auto w-full cursor-pointer my-3 rounded-md overflow-hidden shadow-lg" @click="activePhoto = photo">
          <img :src="photo.thumbnail" :alt="`Picture ${photo.id} thumbnail`" class="w-full">
          <div v-if="photo?.caption" class="bg-neutral dark:bg-darkNeutral px-3 py-3">
            {{ photo.caption }}
          </div>
        </div>
      </div>
      <div v-show="loading || next" class="relative flex w-full mx-auto min-h-[50px]">
        <div v-show="next && !loading" class="m-auto">
          <chevron-double-down-icon class="h-10 w-10 md:h-12 md:w-12 pt-3.5 animate-bounce stroke-accent stroke-2"/>
        </div>
        <loading-view v-show="loading"></loading-view>
      </div>
    </div>
    <div v-if="activePhoto" class="fixed top-0 left-0 w-full h-full">
      <div class="absolute w-fit h-fit top-1/2 left-1/2 z-50 -translate-x-1/2 -translate-y-1/2 p-2 bg-secondary rounded-lg shadow-2xl">
        <img class="max-w-[90vw] max-h-[85vh] rounded-lg" :src="activePhoto.picture" alt="Full-size picture">
      </div>
      <div class="absolute z-40 w-screen h-screen backdrop-blur-sm cursor-pointer" @click="activePhoto = null" ></div>
    </div>
  </div>

</template>

<script>
import { debounce, throttle } from 'underscore';
import { mapActions, mapState } from 'pinia';
import { useGalleryStore } from '@/stores/api.store';
import LoadingView from '@/components/shared/LoadingView.vue';
import { ChevronDoubleDownIcon } from '@heroicons/vue/24/outline';


export default {
  name: 'TheGallery',
  components: {
    LoadingView,
    ChevronDoubleDownIcon
  },
  props: {
  },
  data () {
    return {
      activePhoto: null,
      breakpointMap: [
        {name: 'md', value: 768},
        {name: 'lg', value: 1024},
      ],
      breakpoint: 'xl',
    }
  },
  computed: {
    ...mapState(useGalleryStore, [
      'gallery',
      'loading',
      'error',
      'next',
    ]),
  },
  mounted () {
    this.getGalleryContent();
    this.setupGalleryColumns();
    this.updateBreakpoint();
    this.setupInfiniteScroll();
  },
  beforeUnmount () {
    window.removeEventListener('scroll', this.scrollEventListener());
    window.removeEventListener('resize', this.updateBreakpoint());
  },
  methods: {
    ...mapActions(useGalleryStore, ['getGalleryContent']),
    getMoreGalleryContent () {
      if (this.next && !this.loading) {
        this.getGalleryContent(true);
      };
    },
    setupInfiniteScroll () {
      window.addEventListener('scroll', this.scrollEventListener()); 
    },
    scrollEventListener () {
      return debounce(() => {
        let condition = window.innerHeight + window.pageYOffset >= document.documentElement.offsetHeight;
        if (condition) {
          throttle(()=>{
            this.getMoreGalleryContent();
          }, 500, {leading: true})();
        }
      }, 200)
    },
    setupGalleryColumns () {
      window.addEventListener('resize', this.resizeEventListener());
    },
    resizeEventListener () {
      return debounce(() => {
        this.updateBreakpoint()
      }, 100)
    },
    updateBreakpoint () {
      this.breakpoint = this.breakpointMap.find(bp => bp.value >= window.outerWidth)?.name ?? 'xl';
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
