<template>
  <div>
    <list-view :obj-list="infosActiveType" :loading="loading" :error="error" />
  </div>
</template>

<script lang="ts">
import { mapActions, mapState } from "pinia";
import { useInfoStore } from "@/stores";
import ListView from "@/components/shared/list/ListView.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "TheInfo",
  components: {
    ListView,
  },
  computed: {
    ...mapState(useInfoStore, [
      "infos",
      "activeType",
      "infosActiveType",
      "infoTypes",
      "loading",
      "error",
    ]),
  },
  mounted() {
    this.getInfo();
    if (!this.activeType) {
      this.activateType(this.$route.params.infoType as string);
    }
  },
  methods: {
    ...mapActions(useInfoStore, ["getInfo", "activateType"]),
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
