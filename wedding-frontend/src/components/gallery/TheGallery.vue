<template>
  <div class="">
    <h1 class="text-xl my-5 mx-3">{{ $t('gallery.thegallery.gallery') }}</h1> 
    <div class="flex flex-wrap m-3 p-5 bg-pale dark:bg-darkPale rounded-md border-accent">
      <img class="mx-auto my-5 max-w-[160px] border border-secondary dark:border-darkSecondary border-spacing-2 shadow-md cursor-pointer" v-for="photo in gallery" :src="photo.thumbnail" alt="Wedding picture" :key="photo.id">
    </div>

  </div>
</template>

<script>
import { mapActions, mapState } from 'pinia';
import { useGalleryStore } from '@/stores/api.store';

export default {
  name: 'TheGallery',
  data () {
    return {
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
