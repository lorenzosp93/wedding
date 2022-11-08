<template>
  <div class="md:mt-20 w-11/12 mx-auto text-primary dark:text-darkPrimary">
    <main class="flex w-full h-full shadow-inner rounded-3xl">
      <section class="flex flex-col w-full min-h-full py-5 md:w-1/3  bg-neutral dark:bg-darkNeutral h-full overflow-y-scroll">
        <label class="px-3">
          <input v-model="search" class="rounded-lg p-4 bg-pale dark:bg-darkPale transition duration-200 focus:outline-accent focus:ring-2 w-full dark:placeholder-darkNeutral"
            placeholder="Search..." />
        </label>
        <ul class="mt-6">
          <li v-for="(message, idx) in searchedInbox" :key="message.uuid" @click="setActive(idx)" class="py-5 border-b px-3 transition hover:bg-pale hover:dark:bg-darkPale cursor-pointer">
            <div class="flex justify-between items-center">
              <h3 class="text-lg font-semibold">{{ message.subject }}</h3>
              <p class="text-md text-secondary dark:text-darkSecondary ml-2">{{ formattedDate(message.modified_at) }}</p>
            </div>
            <div class="text-md italic text-secondary dark:text-darkSecondary" >{{ truncate(removeHtml(message.content), 50) }}</div>
          </li>
          <div v-if="searchedInbox?.length == 0 && inbox?.length != 0">
            <p>Couldn't find any message that matches your search.</p>
          </div>
          <div v-if="inbox?.length == 0">
            <p>You're all done for the day!</p>
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
              <h3 class="font-semibold text-2xl py-5">{{ activeMessage?.subject }}</h3>
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
              <li v-show="active != searchedInbox?.length - 1" @click="active ++" class="w-6 h-6 rotate-90">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </li>
            </ul>
          </div>
        </div>
        <div>
          <article v-html="activeMessage?.content" class="my-3 leading-7 tracking-wider">
          </article>
          <form v-if="activeMessage?.questions.length && responses">
            <div v-if="!activeMessage?.questions.some(q => !q.response)">
              <p class="my-5 text-accent" >You have already answered these questions.</p>
              <button class="bg-accent dark:bg-accent rounded-md px-2 py-1 mx-auto my-3" @click.prevent="deleteResponses">Change your responses</button>
            </div>
            <div v-for="(question, idx) in activeMessage?.questions" :key="question.uuid">
              <h1 class="text-lg">{{ idx + 1 }}. {{ question.subject }}</h1>
              <p>{{ question.content }}</p>
              <ul v-if="question.options" :multiple="question.multi_select" class="w-full my-2 mx-3 bg-pale dark:bg-darkPale rounded-md">
                <li v-for="option in question.options" :key="option.uuid" >
                  <input
                    :name="question.uuid"
                    :type="question.multi_select ? 'checkbox' : 'radio'"
                    :value="option.uuid"
                    :id="option.uuid"
                    class="my-2 bg-neutral dark:bg-darkNeutral text-accent"
                    v-model="responses.find(r => r.question == question.uuid).option"
                    :disabled="question.response ? (question.multi_select ? true : question?.response?.option != option.uuid) : false"
                    :required="question.mandatory">
                  <label :for="option.uuid" class="ml-3">{{ option.content }}</label>
                </li>
              </ul>
              <div v-if="question.free_text" class="mb-5">
                <label for="input" class="ml-3 my-1">Other:</label>
                <input type="text" class="w-full rounded-md bg-pale dark:bg-darkPale px-2 py-1 ml-3" v-model="responses.find(r => r.question == question.uuid).text" :readonly="question.response" :required="question.mandatory && question.options.length == 0" >
              </div>
              <p v-if="question.uuid == submitError?.find(e => e.q == question)">{{ submitError?.find(e => e.q == question)?.e }}</p>
            </div>
            <button v-if="!submitLoading && activeMessage?.questions.some(q => !q.response)" class="bg-accent dark:bg-accent rounded-md px-2 py-1 mx-auto my-3" @click.prevent="submitResponse">Submit</button>
            <p v-if="submitLoading">Loading</p>
            <p v-if="submitSuccess">Success</p>
          </form>
        </div>
      </section>
    </main> 
  </div>
</template>

<script>
import { useInboxStore } from '@/stores/api.store'
import { mapActions, mapState, mapWritableState } from 'pinia'
import formatting from '@/mixins/formatting'

export default {
  name: 'TheInbox',
  data () {
    return {
    }
  },
  props: {
  },
  emits: [
  ],
  inject: [
  ],
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
      'viewDetail',
    ]),
  },
  methods: {
    ...mapActions(useInboxStore, [
      'getInbox',
      'submitResponse',
      'deleteResponses',
      'setActive',
    ]),
  },
  mounted () {
    this.getInbox();
  },
  mixins: [
    formatting,
  ]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
