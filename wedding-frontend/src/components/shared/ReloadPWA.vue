<template>
    <div v-if="offlineReady || needRefresh" class="flex flex-wrap" role="alert">
      <div class="message mt-1">
        <span v-if="offlineReady">{{ $t('shared.reloadpwa.appReadyTo') }}</span>
        <span v-else>{{ $t('shared.reloadpwa.newContentAvailable') }}</span>
      </div>
      <div class="buttons flex align-middle mt-2 md:mt-0">
        <button v-if="needRefresh" class="button" @click="updateServiceWorker()">{{ $t('shared.reloadpwa.reload') }}</button>
        <button class="button" @click="close">{{ $t('shared.reloadpwa.close') }}</button>
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