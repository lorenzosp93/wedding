<template>
  <nav class="sticky bg-neutral border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-darkNeutral">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <router-link to="/" class="flex items-center">
          <img src="" class="mr-3 h-6 sm:h-9" alt="Website logo">
          <span class="hidden md:block self-center text-xl font-semibold italic whitespace-nowrap dark:text-white">Priscilla & Lorenzo </span>
          <span class="hidden lg:block self-center text-xl font-semibold italic whitespace-nowrap dark:text-white"> - 1/10/2023</span>
      </router-link>
      <button type="button" @click="toggleMenu" class="z-30 inline-flex items-center p-2 ml-3 text-sm text-secondary rounded-lg md:hidden hover:bg-pale hover:text-neutral focus:outline-none focus:ring-1 focus:ring-accent dark:text-darkPrimary dark:hover:bg-darkPale dark:focus:ring-darkSecondary dark:hover:text-darkNeutral" aria-controls="navbar-default" aria-expanded="false">
        <span class="sr-only">{{ $t('shared.thenavbar.openMainMenu') }}</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
      </button>
      <div :class="{hidden: !menu}" class="z-30 w-full md:block md:w-auto top-10 left-0" id="navbarDefault">
        <ul class="flex flex-col py-4 mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-neutral md:dark:bg-darkNeutral">
          <li>
            <router-link @click="dropInfo = false" to="/" class="block py-2 pr-4 pl-3 text-primary rounded md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary   dark:hover:text-darkPrimary" aria-current="page">{{ $t('shared.thenavbar.home') }}</router-link>
          </li>
          <li>
            <div class="relative text-primary rounded  md:border-0  dark:text-darkPrimary   dark:hover:text-darkPrimary z-40">
              <div @click="dropInfo = !dropInfo" class="flex flex-row items-center  md:hover:text-accent">
                <div class="block py-2 pr-4 pl-3 md:p-0 ">{{ $t('shared.thenavbar.information') }}</div>
                <svg fill="currentColor" viewBox="0 0 20 20" :class="{'rotate-180': dropInfo, 'rotate-0': !dropInfo}" class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
              </div>
              <div v-show="dropInfo" class="md:absolute right-0 pt-2 origin-top-right bg-neutral dark:bg-darkNeutral text-primary md:flex md:flex-row">
                <router-link v-for="type in infoTypes" :to="`/info/${type}`" :key="type" @click="{activateType(type); dropInfo = false}" class="block md:flex px-5 py-2 text-sm rounded-lg  md:hover:text-accent  dark:text-darkPrimary   dark:hover:text-darkPrimary" >
                  {{ type }}
                </router-link>
              </div>
            </div>
          </li>
          <li>
            <router-link @click="dropInfo = false" to="/inbox" class="block py-2 pr-4 pl-3 text-primary rounded  md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary   dark:hover:text-darkPrimary">{{ $t('shared.thenavbar.inbox') }}</router-link>
          </li>
          <li>
            <router-link @click="dropInfo = false" to="/gallery" class="block py-2 pr-4 pl-3 text-primary rounded  md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary   dark:hover:text-darkPrimary">{{ $t('shared.thenavbar.gallery') }}</router-link>
          </li>
          <li>
            <router-link @click="dropInfo = false" to="/profile" class="block py-2 pr-4 pl-3 text-primary rounded  md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary   dark:hover:text-darkPrimary">{{ $t('shared.thenavbar.profile') }}</router-link>
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
nav li :hover, nav li .router-link-active, nav li .router-link-exact-active {
  cursor: pointer;
  @apply text-accent dark:text-darkAccent
}
</style>