<template>
  <div class="">
    <!-- show information-types in tabs -->
    <ul class="mx-auto flex flex-col md:flex-wrap p-4 mt-4 bg-pale rounded-lg border border-accent md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium  dark:bg-darkPale md:dark:bg-darkNeutral dark:border-darkAccent">
      <li class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent cursor-pointer" :class="{'text-accent': infoType == activeType}" v-for="infoType in infoTypes" :key="infoType" @click="activateType(infoType)">{{ infoType }}</li>
    </ul>
    <div class="block">
      <div id="infoList" class="bg-pale rounded-md m-3"> <ul>
          <li class="border-primary px-3 py-1 cursor-pointer" :class="{'text-accent': information == activeInfo}" @click="activeInfo = information" v-for="information in infosActiveType" :key="information.uuid">
            {{ information.subject }}
          </li>
        </ul>
      </div>
      <div class="m-5 p-3 bg-secondary border-accent rounded-md" id="infoDetail">
        <h1 class="text-xl">{{ activeInfo?.subject }}</h1>
        <p class="font-thin" v-html="activeInfo?.content"></p>
      </div>
    </div>
    
  </div>
</template>

<script>
import { mapActions, mapState, mapWritableState } from 'pinia';
import { useInfoStore } from '@/stores/api.store';

export default {
  name: 'TheInfo',
  data () {
    return {
    }
  },
  props: {
  },
  computed: {
    ...mapState(useInfoStore, [
      'infos',
      'activeType',
      'infosActiveType',
      'infoTypes',
    ]),
    ...mapWritableState(useInfoStore, [
      'activeInfo'
    ])
  },
  methods: {
    ...mapActions(useInfoStore, [
      'getInfo',
      'activateType',
    ]),
  },
  emits: [
  ],
  inject: [
  ],
  mounted () {
    this.getInfo();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
