<template>
  <div class="w-11/12 mx-auto text-primary dark:text-darkPrimary">
    <main class="flex w-full h-full shadow-inner rounded-3xl">
  <section class="flex flex-col w-full min-h-full py-5 md:w-1/2  bg-pale dark:bg-darkPale h-full overflow-y-scroll">
    <label class="px-3">
      <input v-model="search" class="rounded-lg p-4 bg-neutral dark:bg-darkNeutral transition duration-200 focus:outline-none focus:ring-2 w-full"
        placeholder="Search..." />
    </label>

    <ul class="mt-6">
      <li v-for="(message, idx) in searchedInbox(search)" :key="message.uuid" @click="setActive(idx)" class="py-5 border-b px-3 transition hover:bg-indigo-100">
        <a href="#" class="flex justify-between items-center">
          <h3 class="text-lg font-semibold">{{ message.subject }}</h3>
          <p class="text-md text-gray-400 ml-2">{{ formattedDate(message.modified_at) }}</p>
        </a>
        <div class="text-md italic text-gray-400" >{{ truncate(removeHtml(message.content), 50) }}</div>
      </li>
      <div v-if="inbox.length == 0">
        <p>You're all done for the day!</p>
      </div>
    </ul>
  </section>
  <section :class="{hidden: !viewDetail}" class="md:block fixed left-0 z-10 md:relative w-full mx-auto min-h-screen md:w-1/2 px-4 flex flex-col bg-neutral dark:bg-darkNeutral">
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
        <ul class="flex text-primary dark:text-darkPrimary space-x-4">
          <li v-show="active != 0" @click="active --" class="w-6 h-6 rotate-90">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
            </svg>
          </li>
          <li v-show="active != inbox.length - 1" @click="active ++" class="w-6 h-6 rotate-90">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </li>

        </ul>
      </div>
    </div>
    <section>
      <article v-html="activeMessage?.content" class="my-3 text-gray-500 leading-7 tracking-wider">
      </article>
      <form v-if="activeMessage?.questions.length">
        <p class="my-5" v-if="!activeMessage?.questions.some(q => !q.response)">You have already answered these questions.</p>
        <div v-for="(question, idx) in activeMessage?.questions" :key="question.uuid">
          <h1 class="text-lg">{{ idx + 1 }}. {{ question.subject }}</h1>
          <p>{{ question.content }}</p>
          <ul v-if="question.options" :multiple="question.multi_select" class="my-2 ml-3">
            <li v-for="option in question.options" :key="option.uuid" >
              <input
                :name="question.uuid"
                :type="question.multi_select ? 'checkbox' : 'radio'"
                :value="option.uuid"
                :id="option.uuid"
                class="my-2"
                v-model="responses.filter(r => r.question == question.uuid)[0].option"
                :disabled="question.multi_select ? !question?.response?.option.includes(option.uuid) : question?.response?.option != option.uuid"
                :required="question.mandatory">
              <label :for="option.uuid" class="mx-2">{{ option.content }}</label>
            </li>
          </ul>
          <input v-if="question.free_text" type="text" class="w-full rounded-md bg-pale dark:bg-darkPale px-2 py-1" v-model="responses.filter(r => r.question == question.uuid)[0].text" :readonly="question.response" :required="question.mandatory && question.options.length == 0">
        </div>
        <button v-if="!submitLoading && activeMessage?.questions.some(q => !q.response)" class="bg-acccent dark:bg-accent rounded-md px-2 py-1 mx-auto my-3" @click.prevent="submitResponse">Submit</button>
        <p v-if="submitLoading">Loading</p>
        <p v-if="submitSuccess">Success</p>
      </form>
    </section>
  </section>
</main> 
  </div>
</template>

<script>
import ApiService from '@/services/api.service'



export default {
  name: 'TheInbox',
  data () {
    return {
      loading: false,
      inbox: [],
      responses: [],
      active: 0,
      submitLoading: false,
      submitSuccess: false,
      viewDetail: false,
      search: '',
    }
  },
  props: {
  },
  emits: [
  ],
  inject: [
  ],
  computed: {
    activeMessage(){
      return this.inbox[this.active]
    },
  },
  methods: {
    getInbox () {
      this.loading = true;
      ApiService.getInboxContent().then(
        (response) => {
          this.inbox = response.data;
          this.responseSetup();
          this.loading = false;
        }
      )
    },
    responseSetup () {
      this.inbox.forEach(message => {
        if (message.questions.length){
          message.questions.forEach(question => {
            this.responses = [...this.responses, {
              question: question.uuid,
              option: question?.response?.option ?? (question.multi_select ? [] : null),
              text: question?.response?.text ?? '',
            }]
          })
        }
      })
    },
    submitResponse () {
      this.submitLoading = true;
      const out = this.responses.some(
        response => {
          if(this.activeMessage.questions.some(q => q.uuid == response.question && !q.response)){
            ApiService.postInboxResponse(
              response.question,
              Array.isArray(response.option) ? response.option : response.option ? [response.option] : [],
              response.text,
            ).then(
              () => false
            )
          }
        }
      )
      this.submitLoading = false;
      if (!out) {
        this.submitSuccess = true;
      }
    },
    removeHtml (value) {
      const div = document.createElement('div')
      div.innerHTML = value
      const text = div.textContent || div.innerText || ''
      return text
    },
    truncate (value, length) {
      if (!value) return "";
      value = value.toString();
      if (value.length > length) {
          return value.substring(0, length) + "...";
      } else {
          return value;
      }
    },
    formattedDate (date) {
      date = new Date(date);
      const yyyy = date.getYear() + 1900;
      const mm = date.getMonth() + 1;
      const dd = date.getDate();
      return `${yyyy}.${mm}.${dd}`
    },
    setActive (n) {
      this.active = n;
      this.viewDetail = true;
    },
    searchedInbox(search){
      if (!search) {
        return this.inbox
      }

      return this.inbox.filter(message => {
        return (message.subject + message.content).toLowerCase()
          .search(search.toLowerCase()) != -1
      })
    }
  },
  mounted () {
    this.getInbox();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
