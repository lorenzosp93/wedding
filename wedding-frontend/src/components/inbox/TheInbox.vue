<template>
  <div>
    <list-view
      :searchedList="searchedInbox"
      :isListEmpty="inbox.length == 0"
      :activeObject="activeMessage"
      :responsesInit="responses"
      :loading="inboxLoading"
      :error="error"
      :submitLoading="submitLoading"
      :submitError="submitError"
      :submitSuccess="submitSuccess"
      :deleteLoading="deleteLoading"
      :deleteError="deleteError"
      :deleteSuccess="deleteSuccess"
      @active="(n) => active = n"
      @submitResponse="callSubmitResponse"
      @deleteResponses="deleteResponses"
    >
    <template v-slot:search>
      <input v-model="search" class="rounded-lg p-4 bg-pale dark:bg-darkPale transition duration-200 focus:outline-none focus:ring-2 w-full placeholder-neutral dark:placeholder-darkNeutral" :placeholder="$t('inbox.theinbox.search')" />
    </template>
    </list-view>
  </div>
</template>

<script>
import { useInboxStore } from '@/stores/api.store'
import { mapActions, mapState, mapWritableState } from 'pinia'
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
      'activeMessage',
      'searchedInbox',
      'inboxLoading',
      'error',
      'submitLoading',
      'submitSuccess',
      'submitError',
      'deleteLoading',
      'deleteSuccess',
      'deleteError',
    ]),
    ...mapWritableState(useInboxStore, [
      'responses',
      'search',
      'active',
    ]),
  },
  methods: {
    ...mapActions(useInboxStore, [
      'getInbox',
      'submitResponse',
      'deleteResponses',
    ]),
    callSubmitResponse (responses) {
      this.responses = responses;
      this.submitResponse();
    },
  },
  mounted () {
    this.getInbox();
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
