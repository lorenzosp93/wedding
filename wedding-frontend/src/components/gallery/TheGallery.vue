<template>
  <div class="m-auto max-w-2xl">
    <loading-view v-if="loading"></loading-view>
    <div v-show="!loading" class="flex flex-wrap mx-5 my-5 p-5 bg-pale dark:bg-darkPale rounded-md">
      <img class="mx-auto max-w-[160px] shadow-md cursor-pointer" v-for="photo in gallery" :src="photo.thumbnail" alt="Picture thumbnail" :key="photo.id" @click="activePhoto = photo">
      <div v-if="activePhoto" class="fixed top-0 left-0 w-screen h-screen">
        <img class="absolute max-w-[80%] max-h-[90%] top-1/2 left-1/2 z-50 transform -translate-x-1/2 -translate-y-1/2" :src="activePhoto.picture" alt="Full-size picture">
        <div @click="activePhoto = null" class="absolute z-40 w-screen h-screen backdrop-blur-sm" />
      </div>
    </div>

  </div>

</template>

<script>
import { mapActions, mapState } from 'pinia';
import { useGalleryStore } from '@/stores/api.store';
import LoadingView from '@/components/shared/LoadingView';

export default {
  name: 'TheGallery',
  components: {
    LoadingView
  },
  data () {
    return {
      activePhoto: null,
    }
  },
  props: {
  },
  methods: {
    ...mapActions(useGalleryStore, ['getGalleryContent'])
  },
  emits: [
  ],
  inject: [
  ],
  computed: {
    ...mapState(useGalleryStore, [
      'gallery',
      'loading',
      'error',
    ])
  },
  mounted () {
    this.getGalleryContent();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
