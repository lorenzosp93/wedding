<template>
  <div>
    <list-view
      :obj-list="inboxStore.inbox"
      :loading="inboxStore.inboxLoading"
      :error="inboxStore.error"
      :submit-loading="inboxStore.submitLoading"
      :submit-error="inboxStore.submitError"
      :submit-success="inboxStore.submitSuccess"
      :delete-loading="inboxStore.deleteLoading"
      :delete-error="inboxStore.deleteError"
      :delete-success="inboxStore.deleteSuccess"
      @submit-response="inboxStore.submitResponse"
      @delete-responses="inboxStore.deleteResponses"
    >
      <template #search> </template>
    </list-view>
  </div>
</template>

<script setup lang="ts">
import { useInboxStore } from "@/stores";
import ListView from "@/components/shared/list/ListView.vue";
import { onMounted } from "vue";

const inboxStore = useInboxStore();

onMounted(() => {
  inboxStore.getInbox();
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
