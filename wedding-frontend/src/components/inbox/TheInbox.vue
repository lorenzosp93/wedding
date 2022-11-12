<template>
  <div>
    <list-view
      :objList="inbox"
      :loading="inboxLoading"
      :error="error"
      :submitLoading="submitLoading"
      :submitError="submitError"
      :submitSuccess="submitSuccess"
      :deleteLoading="deleteLoading"
      :deleteError="deleteError"
      :deleteSuccess="deleteSuccess"
      @submitResponse="submitResponse"
      @deleteResponses="deleteResponses"
    >
    <template v-slot:search>
    </template>
    </list-view>
  </div>
</template>

<script>
import { useInboxStore } from '@/stores/api.store'
import { mapActions, mapState} from 'pinia'
import ListView from '@/components/shared/ListView'

export default {
  name: 'TheInbox',
  data () {
    return {
    }
  },
  components: {
    ListView,
  },
  computed: {
    ...mapState(useInboxStore, [
      'inbox',
      'inboxLoading',
      'error',
      'submitLoading',
      'submitSuccess',
      'submitError',
      'deleteLoading',
      'deleteSuccess',
      'deleteError',
    ]),
  },
  methods: {
    ...mapActions(useInboxStore, [
      'getInbox',
      'submitResponse',
      'deleteResponses',
    ]),
  },
  mounted () {
    this.getInbox();
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
