<template>
  <div>
    <list-view
      :obj-list="inbox"
      :loading="inboxLoading"
      :error="error"
      :submit-loading="submitLoading"
      :submit-error="submitError"
      :submit-success="submitSuccess"
      :delete-loading="deleteLoading"
      :delete-error="deleteError"
      :delete-success="deleteSuccess"
      @submit-response="submitResponse"
      @delete-responses="deleteResponses"
    >
      <template #search> </template>
    </list-view>
  </div>
</template>

<script lang="ts">
import { useInboxStore } from "@/stores";
import { mapActions, mapState } from "pinia";
import ListView from "@/components/shared/list/ListView.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "TheInbox",
  components: {
    ListView,
  },
  computed: {
    ...mapState(useInboxStore, [
      "inbox",
      "inboxLoading",
      "error",
      "submitLoading",
      "submitSuccess",
      "submitError",
      "deleteLoading",
      "deleteSuccess",
      "deleteError",
    ]),
  },
  mounted() {
    this.getInbox();
  },
  methods: {
    ...mapActions(useInboxStore, [
      "getInbox",
      "submitResponse",
      "deleteResponses",
    ]),
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
