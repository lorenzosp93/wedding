<template>
  <div v-if="checkTechnology" class="flex">
    <div id="notification-trigger" class="p-2">
      <button
        aria-label="notifications button"
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
import { request, API_URL } from "@/services/api.service";
import { BellAlertIcon } from "@heroicons/vue/24/outline";
import { defineComponent } from "vue";

export default defineComponent({
  name: "PushSubscribe",
  components: {
    BellAlertIcon,
  },
  data() {
    return {
      pushSubscription: undefined as PushSubscription | undefined,
    };
  },
  computed: {
    checkTechnology() {
      return "serviceWorker" in navigator && "PushManager" in window;
    },
  },
  methods: {
    publishSubscription() {
      request(true).post(
        `${API_URL}/api/user/subscription/`,
        this.pushSubscription?.toJSON()
      );
    },
    askPermission() {
      return new Promise((resolve, reject) => {
        const permissionResult = Notification.requestPermission(function (
          result
        ) {
          resolve(result);
        });

        if (permissionResult) {
          permissionResult.then(resolve, reject);
        }
      }).then((permissionResult) => {
        if (permissionResult !== "granted") {
          throw new Error("We weren't granted permission.");
        }
        this.subscribeUserToPush();
      });
    },
    subscribeUserToPush() {
      return navigator.serviceWorker
        .getRegistration()
        .then((registration: ServiceWorkerRegistration | undefined) => {
          const subscribeOptions = {
            userVisibleOnly: true,
            applicationServerKey: this.urlBase64ToUint8Array(
              import.meta.env.VITE_APP_KEY
            ),
          };
          return registration?.pushManager.subscribe(subscribeOptions);
        })
        .then((pushSubscription: PushSubscription | undefined) => {
          this.pushSubscription = pushSubscription;
          this.publishSubscription();
        });
    },
    urlBase64ToUint8Array(base64String: string): Uint8Array {
      var padding = "=".repeat((4 - (base64String.length % 4)) % 4);
      var base64 = (base64String + padding)
        .replace(/-/g, "+")
        .replace(/_/g, "/");

      var rawData = window.atob(base64);
      var outputArray = new Uint8Array(rawData.length);

      for (var i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
      }
      return outputArray;
    },
  },
});
</script>

<style></style>
