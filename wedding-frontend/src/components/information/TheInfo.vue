<template>
  <div class="md:mt-20 w-11/12 mx-auto text-primary dark:text-darkPrimary">
    <main class="flex w-full h-full shadow-inner rounded-3xl">
      <section class="flex flex-col w-full min-h-full py-5 md:w-1/3  bg-neutral dark:bg-darkNeutral h-full overflow-y-scroll">
        <label class="px-3">
          <input v-model="search" class="rounded-lg p-4 bg-pale dark:bg-darkPale transition duration-200 focus:outline-none focus:ring-2 w-full placeholder-neutral dark:placeholder-darkNeutral"
            placeholder="Search..." />
        </label>

        <ul class="mt-6">
          <li v-for="(info, idx) in infosActiveType" :key="info.uuid" @click="setActive(idx)" class="py-5 border-b px-3 transition hover:bg-pale hover:dark:bg-darkPale cursor-pointer">
            <div class="flex flex-row justify-between items-center">
              <img v-if="info.thumbnail" class="max-w-[40%] ml-5 rounded-md shadow-lg" :src="info.thumbnail" alt="Information article thumbnail">
              <div class="mr-5 pl-5">
                <h3 class="text-lg font-semibold">{{ info.subject }}</h3>
                <div class="text-md italic text-secondary dark:text-darkSecondary" >{{ truncate(removeHtml(info.content), 50) }}</div>
              </div>
            </div>
          </li>
          <div v-if="infosActiveType?.length == 0">
            <p>Couldn't find any {{ activeType }} that matches your search.</p>
          </div>
        </ul>
      </section>
      <section :class="{hidden: !viewDetail}" class="md:block absolute left-0 z-10 md:relative w-full mx-auto min-h-screen md:w-1/2 px-4 flex flex-col bg-neutral dark:bg-darkNeutral overflow-y-scroll">
        <div class="flex justify-between items-center border-b-2 mb-8">
          <div class="flex space-x-4 items-center">
            <div @click="viewDetail = false" class="h-6 w-6 md:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
                </svg>
            </div>
            <div class="flex flex-col">
              <h3 class="font-semibold text-2xl py-5">{{ activeInfo?.subject }}</h3>
            </div>
          </div>
          <div>
            <ul class="flex text-primary dark:text-darkPrimary space-x-4 cursor-pointer">
              <li v-show="active != 0" @click="active --" class="w-6 h-6 rotate-90">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
                </svg>
              </li>
              <li v-show="active != infosActiveType?.length - 1" @click="active ++" class="w-6 h-6 rotate-90">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </li>
            </ul>
          </div>
        </div>
        <div v-if="activeInfo?.picture" class="w-full px-5 rounded-lg shadow-md">
          <img :src="activeInfo?.picture" alt="Information article picture" >
        </div>
        <article v-html="activeInfo?.content" class="my-3 leading-7 tracking-wider">
        </article>
      </section>
    </main> 
  </div>
</template>

<script>
import { mapActions, mapState, mapWritableState } from 'pinia';
import { useInfoStore } from '@/stores/api.store';
import formatting from '@/mixins/formatting';

export default {
  name: 'TheInfo',
  data () {
    return {
    }
  },
  computed: {
    ...mapState(useInfoStore, [
      'infos',
      'activeType',
      'infosActiveType',
      'infoTypes',
    ]),
    ...mapWritableState(useInfoStore, [
      'activeInfo',
      'search',
      'viewDetail',
      'active',
    ])
  },
  methods: {
    ...mapActions(useInfoStore, [
      'getInfo',
      'activateType',
      'setActive',
    ]),
  },
  mounted () {
    this.getInfo();
    if (!this.activeType) {
      this.activateType(this.$route.params.infoType)
    }
  },
  mixins: [
    formatting
  ],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
