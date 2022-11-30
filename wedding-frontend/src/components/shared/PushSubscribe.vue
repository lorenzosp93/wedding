<template>
<div v-if="checkTechnology">
    <div class="fixed bottom-0 right-0 p-3  fill-secondary dark:fill-darkPale" aria-label="tour button">
        <button id="notification-trigger" @click="askPermission">
          <svg id="Layer_1" class="w-8" style="enable-background:new 0 0 512 512;" version="1.1" viewBox="0 0 512 512" width="512px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g><path d="M381.7,225.9c0-97.6-52.5-130.8-101.6-138.2c0-0.5,0.1-1,0.1-1.6c0-12.3-10.9-22.1-24.2-22.1c-13.3,0-23.8,9.8-23.8,22.1   c0,0.6,0,1.1,0.1,1.6c-49.2,7.5-102,40.8-102,138.4c0,113.8-28.3,126-66.3,158h384C410.2,352,381.7,339.7,381.7,225.9z"/><path d="M256.2,448c26.8,0,48.8-19.9,51.7-43H204.5C207.3,428.1,229.4,448,256.2,448z"/></g></svg>
        </button>
    </div>
</div>
</template>
<script>
// https://web.dev/push-notifications-subscribing-a-user/
import { request, API_URL } from '@/services/api.service'

export default {
  name: 'PushSubscribe',
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