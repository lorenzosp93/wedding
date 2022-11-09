<template>
  <div>
    <list-view
      :searchedList="infosActiveType"
      :isListEmpty="infos.length == 0"
      :activeObject="activeInfo"
      :loading="loading"
      :error="error"
      @active="(n) => active = n"
    >
    <template v-slot:search>
      <input v-model="search" class="rounded-lg p-4 bg-pale dark:bg-darkPale transition duration-200 focus:outline-none focus:ring-2 w-full placeholder-neutral dark:placeholder-darkNeutral" :placeholder="$t('information.theinfo.search')" />
    </template>
    </list-view>
  </div>
</template>

<script>
import { mapActions, mapState, mapWritableState } from 'pinia';
import { useInfoStore } from '@/stores/api.store';
import ListView from '@/components/shared/ListView';

export default {
  name: 'TheInfo',
  data () {
    return {
    }
  },
  components: {
    ListView
  },
  computed: {
    ...mapState(useInfoStore, [
      'infos',
      'activeType',
      'infosActiveType',
      'infoTypes',
      'loading',
      'error',
    ]),
    ...mapWritableState(useInfoStore, [
      'activeInfo',
      'search',
      'active',
    ])
  },
  methods: {
    ...mapActions(useInfoStore, [
      'getInfo',
      'activateType',
    ]),
  },
  mounted () {
    this.getInfo();
    if (!this.activeType) {
      this.activateType(this.$route.params.infoType)
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
