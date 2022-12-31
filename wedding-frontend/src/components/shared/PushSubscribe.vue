<template>
  <div v-if="checkTechnology && !isSubscribed" class="flex">
    <div id="notification-trigger" class="p-2">
      <button
        :aria-label="$t('shared.pushsubscribe.notificationsButton')"
        class="bg-neutral dark:bg-darkNeutral p-1 rounded-md"
        @click="askPermission"
      >
        <bell-alert-icon class="h-6 w-6 md:h-7 md:w-7" />
      </button>
    </div>
  </div>
</template>

<script lang="ts">
// https://web.dev/push-notifications-subscribing-a-user/
import { useNotificationStore } from "@/stores";
import { mapState, mapActions } from "pinia";
import { BellAlertIcon } from "@heroicons/vue/24/outline";
import { defineComponent } from "vue";

export default defineComponent({
  name: "PushSubscribe",
  components: {
    BellAlertIcon,
  },
  data() {
    return {};
  },
  computed: {
    checkTechnology() {
      return "serviceWorker" in navigator && "PushManager" in window;
    },
    ...mapState(useNotificationStore, ["isSubscribed", "loading", "error"]),
  },
  methods: {
    ...mapActions(useNotificationStore, ["askPermission"]),
  },
});
</script>

<style></style>
