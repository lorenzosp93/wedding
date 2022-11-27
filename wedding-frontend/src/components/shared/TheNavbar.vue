<!-- eslint-disable vue/require-prop-types -->
<template>
  <nav id="the-navbar" class="px-3 py-2">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <router-link to="/" class="">
          <img class="h-12" :src="logo" aria-label="P & L logo">
      </router-link>
      <button id="menu-toggle" type="button" class="z-20 inline-flex items-center p-2 ml-3 text-sm text-secondary rounded-lg md:hidden hover:ring-1 ring-secondary" aria-controls="navbar-default" aria-expanded="false" @click="toggleMenu">
        <span class="sr-only">{{ $t('shared.thenavbar.openMainMenu') }}</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
      </button>
      <div id="navbar-default" class="z-20 w-full md:transform-none md:block md:w-auto md:opacity-100 md:max-h-full" style="transition: max-height 0.4s, opacity 0.2s ease-in;" :class="{'invisible md:visible opacity-0 max-h-0': !menu, 'opacity-100 max-h-96': menu}">
        <ul class="flex flex-col md:flex-row md:space-x-8 mt-4 md:mt-0 duration-500 ease-out md:transition-none">
          <li>
            <router-link id="navbar-home" :to="{name:'home'}" class="block py-2 pr-4 pl-3  rounded  hover:text-accent md:p-0" aria-current="page" @click="dropInfo = false">{{ $t('shared.thenavbar.home') }}</router-link>
          </li>
          <li>
            <div id="navbar-information" class="relative rounded cursor-pointer">
              <div class="flex flex-row items-center " @click="dropInfo = !dropInfo">
                <div class="block py-2 pr-4 pl-3 md:p-0 hover:text-accent ">{{ $t('shared.thenavbar.information') }}</div>
                <svg fill="currentColor" viewBox="0 0 20 20" :class="{'rotate-180': dropInfo, 'rotate-0': !dropInfo}" class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </div>
              <ul class="md:absolute md:left-1/2 md:-translate-x-1/2 md:top-5 bg-neutral dark:bg-darkNeutral flex flex-col md:flex-row z-30 md:transition-none" style="transition: max-height 0.4s, opacity 0.2s ease-in;" :class="{'invisible opacity-0 max-h-0': !dropInfo, 'opacity-100 max-h-52': dropInfo}">
                <li v-for="type in infoTypes" :key="type" class="pl-5 py-1 md:py-2 rounded-lg" >
                  <router-link :to="{name: 'info', params: {infoType: type}}" class=" hover:text-accent child" @click="{activateType(type); dropInfo = false}" >
                    {{ type }}
                  </router-link>
                </li>
              </ul>
            </div>
          </li>
          <li>
            <router-link id="navbar-inbox" :to="{name: 'inbox'}" class="block py-2 pr-4 pl-3  rounded hover:text-accent md:p-0  " @click="dropInfo = false">{{ $t('shared.thenavbar.inbox') }}</router-link>
          </li>
          <li>
            <router-link id="navbar-gallery" :to="{name: 'gallery'}" class="block py-2 pr-4 pl-3  rounded   hover:text-accent md:p-0    " @click="dropInfo = false">{{ $t('shared.thenavbar.gallery') }}</router-link>
          </li>
          <li>
            <router-link id="navbar-profile" :to="{name: 'profile'}" class="block py-2 pr-4 pl-3  rounded   hover:text-accent md:p-0    " @click="dropInfo = false">{{ $t('shared.thenavbar.profile') }}</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { useInfoStore } from '@/stores/api.store';
import { mapActions, mapState } from 'pinia';

export default {
  name: 'TheNavbar',
  props: {
    infoType: {type: Array},
    tour: {type: Object},
  },
  data () {
    return {
      menu: false,
      dropInfo: false,
      logo: new URL("@/assets/logo_long.svg", import.meta.url).href,
    };
  },
  computed: {
    ...mapState(useInfoStore, [
      'infoTypes',
      'infos',
    ]),
  },
  mounted () {
    this.getInfo();
  },
  methods: {
    toggleMenu(){
      this.menu = !this.menu;
    },
    ...mapActions(useInfoStore, [
      'getInfo',
      'activateType',
    ])
  },
}
</script>

<style scoped>
nav li .router-link-active{
  @apply cursor-pointer text-accent;
}

div:has(+ ul li .router-link-active) {
  @apply text-accent
}

</style>