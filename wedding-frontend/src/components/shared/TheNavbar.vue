<template>
  <nav class="border-gray-200 px-2 sm:px-4 py-2.5 rounded">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <router-link to="/" class="flex items-center">
          <img class="h-10 block self-center text-xl font-semibold italic whitespace-nowrap dark:text-white" :src="require('@/assets/logo_long.svg')">
      </router-link>
      <button type="button" @click="toggleMenu" class="z-30 inline-flex items-center p-2 ml-3 text-sm text-secondary rounded-lg md:hidden hover:bg-pale hover:text-neutral focus:outline-none  dark:hover:bg-darkPale dark:focus:ring-darkSecondary dark:hover:text-darkNeutral" aria-controls="navbar-default" aria-expanded="false">
        <span class="sr-only">{{ $t('shared.thenavbar.openMainMenu') }}</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
      </button>
      <div class="z-30 w-full md:transform-none md:block md:w-auto md:opacity-100 md:max-h-full" style="transition: max-height 0.4s, opacity 0.2s ease-in;" :class="{'invisible md:visible opacity-0 max-h-0': !menu, 'opacity-100 max-h-96': menu}" id="navbarDefault">
        <ul class="flex flex-col py-4 mt-4 md:flex-row md:space-x-8 md:mt-0 font-medium  duration-500 ease-out md:transition-none">
          <li>
            <router-link @click="dropInfo = false" :to="{name:'home'}" class="block py-2 pr-4 pl-3  rounded  hover:text-accent md:p-0    " aria-current="page">{{ $t('shared.thenavbar.home') }}</router-link>
          </li>
          <li>
            <div class=" relative  rounded        cursor-pointer">
              <div @click="dropInfo = !dropInfo" class="flex flex-row items-center ">
                <div class="block py-2 pr-4 pl-3 md:p-0 hover:text-accent ">{{ $t('shared.thenavbar.information') }}</div>
                <svg fill="currentColor" viewBox="0 0 20 20" :class="{'rotate-180': dropInfo, 'rotate-0': !dropInfo}" class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </div>
              <ul v-show="dropInfo" class="md:absolute right-0 top-5 pt-2 origin-top-right bg-neutral dark:bg-darkNeutral flex flex-row z-40">
                <li class="block md:flex">
                  <router-link v-for="type in infoTypes" :to="{name: 'info', params: {infoType: type}}" :key="type" @click="{activateType(type); dropInfo = false}" class="pl-5 py-1 text-sm rounded-lg   hover:text-accent child block md:flex" >
                    {{ type }}
                  </router-link>

                </li>
              </ul>
            </div>
          </li>
          <li>
            <router-link @click="dropInfo = false" :to="{name: 'inbox'}" class="block py-2 pr-4 pl-3  rounded hover:text-accent md:p-0  ">{{ $t('shared.thenavbar.inbox') }}</router-link>
          </li>
          <li>
            <router-link @click="dropInfo = false" :to="{name: 'gallery'}" class="block py-2 pr-4 pl-3  rounded   hover:text-accent md:p-0    ">{{ $t('shared.thenavbar.gallery') }}</router-link>
          </li>
          <li>
            <router-link @click="dropInfo = false" :to="{name: 'profile'}" class="block py-2 pr-4 pl-3  rounded   hover:text-accent md:p-0    ">{{ $t('shared.thenavbar.profile') }}</router-link>
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
  data () {
    return {
      menu: false,
      dropInfo: false,
    };
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
  computed: {
    ...mapState(useInfoStore, [
      'infoTypes',
      'infos',
    ]),
  },
  mounted () {
    this.getInfo();
  },
  props: ['infoType']
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