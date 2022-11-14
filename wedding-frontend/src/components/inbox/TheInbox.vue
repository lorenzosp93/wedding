<template>
  <div>
    <list-view
      :obj-list="inbox"
      :loading="inboxLoading"
      :error="error"
      :submit-loading="submitLoading"
      :submit-error="submitError"
      :submit-success="submitSuccess"
      :delete-loading="deleteLoading"
      :delete-error="deleteError"
      :delete-success="deleteSuccess"
      @submit-response="submitResponse"
      @delete-responses="deleteResponses"
    >
    <template #search>
    </template>
    </list-view>
  </div>
</template>

<script>
import { useInboxStore } from '@/stores/api.store'
import { mapActions, mapState} from 'pinia'
import ListView from '@/components/shared/ListView.vue'

export default {
  name: 'TheInbox',
  components: {
    ListView,
  },
  data () {
    return {
    }
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
  mounted () {
    this.getInbox();
  },
  methods: {
    ...mapActions(useInboxStore, [
      'getInbox',
      'submitResponse',
      'deleteResponses',
    ]),
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
