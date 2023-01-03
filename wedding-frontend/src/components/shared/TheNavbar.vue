<template>
  <nav
    id="the-navbar"
    class="px-3 py-3 flex flex-initial max-w-4xl mx-auto w-full"
  >
    <div class="flex flex-wrap justify-between items-center w-full">
      <router-link to="/" class="mr-auto w-fit">
        <img class="h-12 w-48" :src="logo" aria-label="P & L logo" />
      </router-link>
      <button
        id="menu-toggle"
        type="button"
        class="z-20 inline-flex items-center p-2 ml-3 text-sm text-secondary rounded-lg md:hidden hover:ring-1 ring-secondary"
        aria-controls="navbar-default"
        aria-expanded="false"
        @click="() => {if(!menu){menu = true}}"
      >
        <span class="sr-only">{{ $t("shared.thenavbar.openMainMenu") }}</span>
        <bars-3-icon class="w-6 h-6"></bars-3-icon>
      </button>
      <OnClickOutside
        @trigger="handleTrigger"
        :ignore="[
          '#menu-toggle',
          '.shepherd-button',
          '.shepherd-button-secondary',
          '.shepherd-content',
        ]"
        id="navbar-default"
        class="z-20 w-full md:transform-none md:block md:w-auto md:opacity-100 md:max-h-full"
        style="transition: max-height 0.4s, opacity 0.2s ease-in"
        :class="{
          'invisible md:visible opacity-0 max-h-0': !menu,
          'opacity-100 max-h-96': menu,
        }"
      >
        <ul
          class="flex flex-col md:flex-row md:space-x-8 mt-4 md:mt-0 duration-500 ease-out md:transition-none"
        >
          <li>
            <router-link
              id="navbar-home"
              :to="{ name: 'home' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              aria-current="page"
              >{{ $t("shared.thenavbar.home") }}</router-link
            >
          </li>
          <li>
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
                  class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"
                ></chevron-down-icon>
              </div>
              <ul
                class="md:absolute md:left-1/2 md:-translate-x-1/2 md:top-5 flex flex-col md:flex-row z-30 md:transition-none"
                style="transition: max-height 0.4s, opacity 0.2s ease-in"
                :class="{
                  'invisible opacity-0 max-h-0': !dropInfo,
                  'opacity-100 max-h-52': dropInfo,
                }"
              >
                <li
                  v-for="type in infoTypes"
                  :key="type"
                  class="pl-5 pt-1 pb-1 md:pb-0 rounded-lg"
                >
                  <router-link
                    :to="{ name: 'info', params: { infoType: type } }"
                    class="hover:text-accent child"
                    @click="activateType(type)"
                  >
                    {{ type }}
                  </router-link>
                </li>
              </ul>
            </OnClickOutside>
          </li>
          <li>
            <router-link
              id="navbar-guestbook"
              :to="{ name: 'guestbook' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.guestbook") }}</router-link
            >
          </li>
          <li>
            <router-link
              id="navbar-inbox"
              :to="{ name: 'inbox' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.inbox") }}</router-link
            >
          </li>
          <li>
            <router-link
              id="navbar-gallery"
              :to="{ name: 'gallery' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.gallery") }}</router-link
            >
          </li>
          <li>
            <router-link
              id="navbar-profile"
              :to="{ name: 'profile' }"
              class="block py-2 pr-4 pl-3 rounded hover:text-accent md:p-0"
              >{{ $t("shared.thenavbar.profile") }}</router-link
            >
          </li>
        </ul>
      </OnClickOutside>
    </div>
  </nav>
</template>

<script lang="ts">
import { useInfoStore } from "@/stores";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import { Bars3Icon, ChevronDownIcon } from "@heroicons/vue/24/outline";
import { OnClickOutside } from "@vueuse/components";
import { useStorage, type RemovableRef } from "@vueuse/core";
import Shepherd from "shepherd.js";

export default defineComponent({
  name: "TheNavbar",
  components: {
    Bars3Icon,
    ChevronDownIcon,
    OnClickOutside,
  },
  data() {
    return {
      menu: false as boolean,
      dropInfo: false as boolean,
      logo: new URL("@/assets/logo_long.svg", import.meta.url).href as string,
      onboardingSeen: useStorage(
        "shepherd-tour",
        false
      ) as RemovableRef<boolean>,
    };
  },
  computed: {
    ...mapState(useInfoStore, ["infoTypes", "infos"]),
  },
  mounted() {
    this.getInfo();
  },
  methods: {
    getActiveTour() {
      return Shepherd.activeTour;
    },
    handleTrigger() {
      if (!this.getActiveTour()) {
        this.menu = false;
      }
    },
    ...mapActions(useInfoStore, ["getInfo", "activateType"]),
  },
});
</script>

<style scoped>
nav li .router-link-active {
  @apply cursor-pointer text-accent;
}

div:has(+ ul li .router-link-active) {
  @apply text-accent;
}
</style>
