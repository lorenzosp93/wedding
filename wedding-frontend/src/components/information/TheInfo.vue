<template>
  <div>
    <list-view
      :objList="infosActiveType"
      :loading="loading"
      :error="error"
    />
  </div>
</template>

<script>
import { mapActions, mapState} from 'pinia';
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
