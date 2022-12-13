<!-- eslint-disable no-useless-escape -->
<template>
<div v-if="checkTechnology">
    <div id="notification-trigger" class="fixed bottom-0 right-0 p-3 z-50 fill-secondary dark:fill-darkPale">
        <button aria-label="notifications button" class="bg-neutral dark:bg-darkNeutral p-1 rounded-md" @click="askPermission">
          <bell-alert-icon class="h-6 w-6 md:h-7 md:w-7" />
        </button>
    </div>
</div>
</template>
<script>
// https://web.dev/push-notifications-subscribing-a-user/
import { request, API_URL } from '@/services/api.service'
import { BellAlertIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'PushSubscribe',
  components: {
    BellAlertIcon,
  },
  data () {
    return{
      pushSubscription: null,
    }
  },
  computed:{
    checkTechnology () {
      return 'serviceWorker' in navigator && 'PushManager' in window
    }
  },
  methods: {
    publishSubscription() {
      request(true).post(`${API_URL}/api/user/subscription/`, this.pushSubscription.toJSON())
    },
    askPermission() {
      return new Promise((resolve, reject) => {
        const permissionResult = Notification.requestPermission(function (result) {
          resolve(result);
        });

        if (permissionResult) {
          permissionResult.then(resolve, reject);
        }
      }).then((permissionResult) => {
        if (permissionResult !== 'granted') {
          throw new Error("We weren't granted permission.");
        }
        this.subscribeUserToPush();
      });
    },
    subscribeUserToPush() {
      return navigator.serviceWorker
        .getRegistration()
        .then((registration) => {
          const subscribeOptions = {
            userVisibleOnly: true,
            applicationServerKey: this.urlBase64ToUint8Array(import.meta.env.VITE_APP_KEY),
          };
          return registration.pushManager.subscribe(subscribeOptions);
        })
        .then((pushSubscription) => {
          this.pushSubscription = pushSubscription;
          this.publishSubscription();
        });
    },
    urlBase64ToUint8Array(base64String) {
        var padding = '='.repeat((4 - base64String.length % 4) % 4);
        var base64 = (base64String + padding)
            .replace(/-/g, '+')
            .replace(/_/g, '/');

        var rawData = window.atob(base64);
        var outputArray = new Uint8Array(rawData.length);

        for (var i = 0; i < rawData.length; ++i) {
            outputArray[i] = rawData.charCodeAt(i);
        }
        return outputArray;
    }
  },
}

</script>

<style>
</style>