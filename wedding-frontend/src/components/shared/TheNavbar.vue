<template>
  <nav
    id="the-navbar"
    class="px-3 py-3 flex flex-initial max-w-4xl mx-auto w-full"
  >
    <div class="flex flex-wrap justify-between items-center w-full">
      <RouterLink to="/" class="mr-auto w-fit">
        <img class="h-12 w-48" :src="logo" aria-label="P & L logo" />
      </RouterLink>
      <button
        id="menu-toggle"
        type="button"
        class="z-20 inline-flex items-center p-2 ml-3 text-sm text-secondary rounded-lg md:hidden hover:ring-1 ring-secondary"
        aria-controls="navbar-default"
        aria-expanded="false"
        ref="menuToggle"
        @click="menu = !menu"
      >
        <span class="sr-only">{{ $t("shared.thenavbar.openMainMenu") }}</span>
        <bars-3-icon class="w-6 h-6"></bars-3-icon>
      </button>
      <OnClickOutside
        @trigger="(event: Event) => handleTrigger(event.target as HTMLElement)"
        id="navbar-default"
        class="z-20 w-full md:transform-none md:block md:w-auto md:opacity-100 md:max-h-full"
        style="transition: max-height 0.4s, opacity 0.2s ease-in"
        :class="{
          'invisible md:visible opacity-0 max-h-0': !menu,
          'opacity-100 max-h-screen': menu,
        }"
      >
        <ul
          class="flex flex-col md:flex-row md:space-x-8 mt-4 md:mt-0 duration-500 ease-out md:transition-none bg-neutral dark:bg-darkNeutral rounded-sm"
        >
          <li>
            <RouterLink
              id="navbar-home"
              :to="{ name: 'home' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              aria-current="page"
              >{{ $t("shared.thenavbar.home") }}</RouterLink
            >
          </li>
          <li v-if="authStore.isAuthenticated">
            <OnClickOutside
              id="navbar-information"
              @trigger="dropInfo = false"
              class="relative rounded"
            >
              <div
                class="flex flex-row items-center cursor-pointer"
                @click="dropInfo = !dropInfo"
              >
                <div class="block py-2 pr-4 pl-3 md:p-0 hover:text-accent">
                  {{ $t("shared.thenavbar.information") }}
                </div>
                <chevron-down-icon
                  :class="{ 'rotate-180': dropInfo, 'rotate-0': !dropInfo }"
                  class="inline h-4 ml-1 transition-transform duration-200 transform md:mt-1"
                ></chevron-down-icon>
              </div>
              <ul
                class="md:absolute md:left-0 md:top-7 flex flex-col md:flex-row z-30 md:transition-none md:space-x-6"
                style="transition: max-height 0.4s, opacity 0.2s ease-in"
                :class="{
                  'invisible opacity-0 max-h-0': !dropInfo,
                  'opacity-100 max-h-52': dropInfo,
                }"
              >
                <li
                  v-for="type in infoStore.infoTypes"
                  :key="type"
                  class="pl-5 md:p-0 py-1 rounded-lg"
                >
                  <RouterLink
                    :to="{ name: 'info', params: { infoType: type } }"
                    class="hover:text-accent child capitalize"
                    @click="infoStore.activateType(type)"
                  >
                    {{ type }}
                  </RouterLink>
                </li>
              </ul>
            </OnClickOutside>
          </li>
          <li>
            <RouterLink
              id="navbar-guestbook"
              :to="{ name: 'guestbook' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.guestbook") }}</RouterLink
            >
          </li>
          <li v-if="authStore.isAuthenticated">
            <RouterLink
              id="navbar-inbox"
              :to="{ name: 'inbox' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.inbox") }}</RouterLink
            >
          </li>
          <li>
            <RouterLink
              id="navbar-gallery"
              :to="{ name: 'gallery' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.gallery") }}</RouterLink
            >
          </li>
          <li v-if="authStore.isAuthenticated">
            <RouterLink
              id="navbar-profile"
              :to="{ name: 'profile' }"
              class="flex py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.profile") }}
            </RouterLink>
          </li>
          <li v-else>
            <RouterLink
              id="navbar-login"
              :to="{ name: 'login' }"
              class="flex py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.login") }}
            </RouterLink>
          </li>
        </ul>
      </OnClickOutside>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useAuthStore, useInfoStore } from "@/stores";
import { type Ref, onMounted, ref } from "vue";
import { Bars3Icon, ChevronDownIcon } from "@heroicons/vue/24/outline";
import { OnClickOutside } from "@vueuse/components";
import Shepherd from "shepherd.js";
import { RouterLink } from "vue-router";

const infoStore = useInfoStore();
const authStore = useAuthStore();

const menu = ref(false);
const dropInfo = ref(false);
const logo = ref(
  new URL("@/assets/logo_long.svg", import.meta.url).href as string
);
const menuToggle: Ref<HTMLElement | null> = ref(null);

onMounted(() => {
  if (authStore.isAuthenticated) {
    infoStore.getInfo();
  }
});

function handleTrigger(target: HTMLElement) {
  let isTour = !!Shepherd.activeTour;
  let isMenuButton = menuToggle.value
    ? (menuToggle.value as HTMLElement).contains(target)
    : false;
  if (isTour || isMenuButton) {
    return;
  }
  menu.value = false;
}
</script>

<style scoped>
nav li .router-link-active {
  @apply cursor-pointer text-accent;
}

div:has(+ ul li .router-link-active) {
  @apply text-accent;
}
</style>
