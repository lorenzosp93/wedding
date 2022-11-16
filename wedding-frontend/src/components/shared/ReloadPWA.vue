<template>
  <div v-if="offlineReady || needRefresh" class="lg:flex bg-pale dark:bg-darkPale text-center py-4 px-4" role="alert">
    <div class="p-3 bg-neutral dark:bg-darkNeutral items-center rounded-xl lg:rounded-full flex lg:inline-flex ml-auto">
      <span class="flex rounded-full bg-pale dark:bg-darkPale px-2 py-1 text-xl mr-3">🔔</span>
      <span v-if="offlineReady" v-t="'shared.reloadpwa.appReadyTo'" class="font-semibold mr-2 text-left flex-auto"></span>
      <span v-else v-t="'shared.reloadpwa.newContentAvailable'" class=" mr-2 text-left flex-auto"></span>
    </div>
    <div class="align-middle my-auto ml-5 mr-auto">
      <button v-if="needRefresh" v-t="'shared.reloadpwa.reload'" class="mx-3 my-2 py-1 px-3 bg-accent rounded-md text-primary" @click="updateServiceWorker()"></button>
      <button v-t="'shared.reloadpwa.close'" class="mx-3 my-2 py-1 px-3 bg-secondary dark:bg-darkNeutral rounded-md" @click="close"></button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRegisterSW } from "virtual:pwa-register/vue";
const { updateServiceWorker } = useRegisterSW();
export default defineComponent({
  name: "ReloadPWA",
  setup() {
    const { offlineReady, needRefresh, updateServiceWorker } = useRegisterSW();
    const close = async () => {
      offlineReady.value = false;
      needRefresh.value = false;
    };
    return { offlineReady, needRefresh, updateServiceWorker, close };
  },
  methods: {
    // eslint-disable-next-line vue/no-dupe-keys
    async updateServiceWorker() {
      await updateServiceWorker();
    },
  },
});
</script>