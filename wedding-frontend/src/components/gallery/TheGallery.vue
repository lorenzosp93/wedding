<template>
  <div class="m-auto max-w-2xl">
    <loading-view v-if="loading"></loading-view>
    <div v-show="!loading" class="flex flex-wrap mx-5 my-5 p-5 bg-pale dark:bg-darkPale rounded-md">
      <img v-for="photo in gallery" :key="photo.id" class="mx-auto max-w-[160px] shadow-md cursor-pointer" :src="photo.thumbnail" alt="Picture thumbnail" @click="activePhoto = photo">
      <div v-if="activePhoto" class="fixed top-0 left-0 w-screen h-screen">
        <img class="absolute max-w-[80%] max-h-[90%] top-1/2 left-1/2 z-50 transform -translate-x-1/2 -translate-y-1/2" :src="activePhoto.picture" alt="Full-size picture">
        <div class="absolute z-40 w-screen h-screen backdrop-blur-sm" @click="activePhoto = null" />
      </div>
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
    ])
  },
  mounted () {
    this.getGalleryContent();
  },
  methods: {
    ...mapActions(useGalleryStore, ['getGalleryContent'])
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
