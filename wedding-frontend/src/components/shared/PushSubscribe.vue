<template>
  <div v-if="checkTechnology && !notificationStore.isSubscribed" class="flex">
    <div id="notification-trigger" class="p-2">
      <button
        :aria-label="$t('shared.pushsubscribe.notificationsButton')"
        class="bg-neutral dark:bg-darkNeutral p-1 rounded-md"
        @click="notificationStore.askPermission"
      >
        <bell-alert-icon class="h-6 w-6 md:h-7 md:w-7" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
// https://web.dev/push-notifications-subscribing-a-user/
import { useNotificationStore } from "@/stores";
import { BellAlertIcon } from "@heroicons/vue/24/outline";
import { computed } from "vue";

const notificationStore = useNotificationStore();

const checkTechnology = computed(() => {
  return "serviceWorker" in navigator && "PushManager" in window;
});
</script>

<style></style>
