<template>
<nav class="sticky bg-neutral border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-darkNeutral">
  <div class="container flex flex-wrap justify-between items-center mx-auto">
    <a href="" class="flex items-center">
        <img src="" class="mr-3 h-6 sm:h-9" alt="Website logo">
        <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">{{ $t('shared.thenavbar.priscillaELorenzo') }}</span>
    </a>
    <button type="button" @click="toggleMenu" class="inline-flex items-center p-2 ml-3 text-sm text-secondary rounded-lg md:hidden hover:bg-pale hover:text-neutral focus:outline-none focus:ring-1 focus:ring-accent dark:text-darkPrimary dark:hover:bg-darkPale dark:focus:ring-darkSecondary dark:hover:text-darkNeutral" aria-controls="navbar-default" aria-expanded="false">
      <span class="sr-only">{{ $t('shared.thenavbar.openMainMenu') }}</span>
      <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
    </button>
    <div :class="{hidden: !menu, block: menu}" class="w-full md:block md:w-auto" id="navbarDefault">
      <ul class="flex flex-wrap p-4 mt-4 bg-pale rounded-lg border border-accent md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-neutral dark:bg-darkPale md:dark:bg-darkNeutral dark:border-darkAccent">
        <li>
          <router-link to="/" class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent" aria-current="page">{{ $t('shared.thenavbar.home') }}</router-link>
        </li>
        <li>
          <router-link to="info" class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent">{{ $t('shared.thenavbar.information') }}</router-link>
        </li>
        <li>
          <router-link to="inbox" class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent">{{ $t('shared.thenavbar.inbox') }}</router-link>
        </li>
        <li>
          <router-link to="gallery" class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent">{{ $t('shared.thenavbar.gallery') }}</router-link>
        </li>
        <li>
          <router-link to="profile" class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent">{{ $t('shared.thenavbar.profile') }}</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>


</template>

<script>
export default {
  name: 'TheNavbar',
  data () {
    return {
      menu: false,
    };
  },
  props: [
  ],
  inject: [
  ],
  methods: {
    toggleMenu(){
      this.menu = !this.menu;
    }
  },
  computed:{
  },
  beforeUnmount () {
  },
  mounted () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
nav li :hover, nav li .router-link-active, nav li .router-link-exact-active {
  cursor: pointer;
  @apply text-accent dark:text-darkAccent
}
</style>