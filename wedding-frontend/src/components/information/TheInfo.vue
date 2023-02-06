<template>
  <div>
    <ListView
      :obj-list="infoStore.infosActiveType"
      :loading="infoStore.loading"
      :error="infoStore.error"
    />
  </div>
</template>

<script setup lang="ts">
import { useInfoStore } from "@/stores";
import ListView from "@/components/shared/list/ListView.vue";
import { onMounted } from "vue";
import { useRoute } from "vue-router";

const infoStore = useInfoStore();
const route = useRoute();
onMounted(() => {
  infoStore.getInfo();
  if (!infoStore.activeType) {
    infoStore.activateType(route.params.infoType as string);
  }
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
