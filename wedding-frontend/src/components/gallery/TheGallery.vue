<template>
  <div class="">
    <h1 class="text-xl my-5 mx-3">Gallery</h1> 
    <div>
      <img class="m-5 border border-primary border-spacing-2" v-for="photo in gallery" src="photo.url" alt="Wedding picture" :key="photo.uuid">
    </div>

  </div>
</template>

<script>
import ApiService from '@/services/api.service'

export default {
  name: 'TheGallery',
  data () {
    return {
      gallery: [],
    }
  },
  props: {
  },
  methods: {
    getGalleryContent () {
      this.loading = true;
      ApiService.getGalleryContent().then(
        (response) => {
          this.gallery = response.data;
          this.loading = false;
        }
      )
    },
  },
  emits: [
  ],
  inject: [
  ],
  computed: {
  },
  mounted () {
    this.getGalleryContent();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
