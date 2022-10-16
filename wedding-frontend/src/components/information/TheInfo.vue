<template>
  <div class="">
    <!-- show information types in tabs -->
    <ul class="mx-auto flex flex-col md:flex-wrap p-4 mt-4 bg-pale rounded-lg border border-accent md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium  dark:bg-darkPale md:dark:bg-darkNeutral dark:border-darkAccent">
      <li class="block py-2 pr-4 pl-3 text-primary rounded hover:bg-secondary md:hover:bg-transparent md:border-0 md:hover:text-accent md:p-0 dark:text-darkPrimary  dark:hover:bg-darkNeutral dark:hover:text-darkPrimary md:dark:hover:bg-transparent cursor-pointer" :class="{'text-accent': infoType == activeType}" v-for="infoType in types" :key="infoType" @click="activateType(infoType)">{{ infoType }}</li>
    </ul>
    <div class="block">
      <div id="infoList"> <ul>
          <li @click="activeInfo = information" v-for="information in infosActiveType" :key="information.uuid">
            {{ information.subject }}
          </li>
        </ul>
      </div>
      <div id="infoDetail">
        <h1 class="text-xl">{{ activeInfo?.subject }}</h1>
        <p class="font-thin" v-html="activeInfo?.content"></p>

      </div>
    </div>
    
  </div>
</template>

<script>
import ApiService from '@/services/api.service'

export default {
  name: 'TheInfo',
  data () {
    return {
      loading: false,
      infos: [],
      activeType: null,
      activeInfo: null
    }
  },
  props: {
  },
  methods: {
    getInfo () {
      this.loading = true;
      ApiService.getInfoContent().then(
        (response) => {
          this.infos = response.data;
          this.loading = false;
          this.activeInfo = this.infos.find(info => info);
          this.activeType = this.activeInfo.type;
        }
      )
    },
    activateType(type){
      this.activeType = type;
      this.activeInfo = this.infos.find(info => info.type == this.activeType);
    }
  },
  emits: [
  ],
  inject: [
  ],
  computed: {
    types () {
      var types = [];
      this.infos.forEach(info => {
        if (!types.includes(info.type)) {
          types = [...types, info.type]
        }
      })
      return types
    },
    infosActiveType () {
      return this.infos.filter(info => {
        return info.type == this.activeType
      })
    },
  },
  mounted () {
    this.getInfo()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
