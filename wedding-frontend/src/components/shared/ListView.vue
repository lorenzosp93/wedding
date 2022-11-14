<template>
  <div class=" w-11/12 mx-auto text-primary dark:text-darkPrimary">
    <loading-view v-if="loading"></loading-view>
    <main v-show="!loading" class="flex w-full h-full rounded-3xl">
      <section class="flex flex-col w-full min-h-full py-5 md:w-1/3  bg-neutral dark:bg-darkNeutral h-full overflow-y-scroll">
        <label class="px-3">
          <input v-model="search" class="rounded-lg p-4 bg-pale dark:bg-darkPale transition duration-200 focus:outline-none focus:ring-2 w-full placeholder-neutral dark:placeholder-darkNeutral" :placeholder="$t('shared.listview.search')" />
        </label>
        <ul class="mt-6">
          <li v-for="(obj, idx) in searchedList" :key="obj.uuid" @click="setActive(idx)" class="py-5 border-b px-3 transition hover:bg-pale hover:dark:bg-darkPale cursor-pointer">
                <div class="flex justify-between items-center">
                  <img v-if="obj?.thumbnail" class="max-w-[40%] ml-5 rounded-md shadow-lg" :src="obj.thumbnail" alt="Information article thumbnail">
                  <div class="mr-5 pl-5">
                    <h3 class="text-lg font-semibold">{{ obj?.subject }}</h3>
                    <div class="text-md italic text-secondary dark:text-darkSecondary" >{{ truncate(removeHtml(obj?.content), 50) }}</div>
                  </div>
                </div>
            </li>
          <div v-if="searchedList?.length == 0 && objList.length">
            <p>{{ $t('shared.listview.noMessage') }}</p>
          </div>
          <div v-if="!objList.length">
            <p>{{ $t('shared.listview.done') }}</p>
          </div>
        </ul>
      </section>
      <section :class="{hidden: !viewDetail}" class="md:block absolute left-0 z-10 md:relative w-full mx-auto min-h-screen md:w-1/2 px-4 flex flex-col bg-neutral dark:bg-darkNeutral overflow-y-scroll">
        <div class="flex justify-between items-center border-b-2 mb-8">
          <div class="flex space-x-4 items-center">
            <div @click="hideDetail" class="h-6 w-6 md:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
                </svg>
            </div>
            <div class="flex flex-col">
              <h3 class="font-semibold text-2xl py-5">{{ activeObject?.subject }}</h3>
            </div>
          </div>
          <div>
            <ul class="flex text-primary dark:text-darkPrimary space-x-4 cursor-pointer">
              <li v-show="active != 0" @click="setActive(active - 1)" class="w-6 h-6 rotate-90">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
                </svg>
              </li>
              <li v-show="active != searchedList?.length - 1" @click="setActive(active + 1)" class="w-6 h-6 rotate-90">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </li>
            </ul>
          </div>
        </div>
        <div>
          <div v-if="activeObject?.picture" class="w-full">
            <img :src="activeObject?.picture" alt="Information article picture" class="rounded-lg shadow-md" >
          </div>
          <article v-html="activeObject?.content" class="my-3 leading-7 tracking-wider" />
          <form v-if="activeObject?.questions?.length && responses?.length">
            <div v-if="!activeObject?.questions.some(q => !q.response)">
              <p class="my-5 text-accent" >{{ $t('shared.listview.alreadyAnswered') }}</p>
              <button class="bg-accent dark:bg-accent rounded-md px-2 py-1 mx-auto my-3" @click.prevent="$emit('deleteResponses')">{{ $t('shared.listview.changeResponses') }}</button>
            </div>
            <div v-for="(question, idx) in activeObject?.questions" :key="question.uuid">
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
                <label for="input" class="ml-3 my-1">{{ $t('shared.listview.other') }}</label>
                <input type="text" class="w-full rounded-md bg-pale dark:bg-darkPale px-2 py-1 ml-3" v-model="responses.find(r => r.question == question.uuid).text" :readonly="question.response" :required="question.mandatory && question.options.length == 0" >
              </div>
              <p v-if="question.uuid == submitError?.find(e => e.q == question)">{{ submitError?.find(e => e.q == question)?.e }}</p>
            </div>
            <button v-if="!submitLoading && activeObject?.questions.some(q => !q.response)" class="bg-accent dark:bg-accent rounded-md px-2 py-1 mx-auto my-3" @click.prevent="$emit('submitResponse', responses)">{{ $t('shared.listview.submit') }}</button>
            <p v-if="submitLoading">{{ $t('shared.listview.loading') }}</p>
            <p v-if="submitSuccess">{{ $t('shared.listview.success') }}</p>
          </form>
        </div>
      </section>
    </main>
  </div> 
</template>

<script>
import LoadingView from '@/components/shared/LoadingView';
export default {
  name: 'ListView',
  components: {
    LoadingView
  },
  data () {
    return {
      active: 0,
      viewDetail: false,
      responses: JSON.parse(localStorage.getItem('responses') ?? "[]"),
      search: '',
    };
  },
  props: [
    'objList',
    'loading',
    'error',
    'submitLoading',
    'submitError',
    'submitSuccess',
    'deleteLoading',
    'deleteError',
    'deleteSuccess',
  ],
  computed: {
    searchedList () {
        if (!this.search) {
            return this.objList
        }
        return this.objList.filter(obj => {
            return (obj?.subject + obj?.content).toLowerCase()
            .search(this.search.toLowerCase()) != -1
        })
    },
    activeObject () {
      return this.objList ? this.objList[this.active] : null
    },
  },
  watch: {
    objList() {
      this.responseSetup();
    },
  },
  methods: {
    setActive(n){
      this.$router.push(
        {
          name: this.$route.name,
          params: {...this.$route.params, active: `${n}`},
        }
      )
      this.active = n;
      this.viewDetail = true;
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
    hideDetail () {
      this.viewDetail = false;
      this.$router.push({name: this.$route.name, params: {...this.$route.params}})
    },
    responseSetup () {
      this.responses = [];
      this.objList.forEach(obj => {
        if (obj.questions?.length){
          obj.questions.forEach(question => {
              this.responses = [...this.responses, {
              question: question.uuid,
              option: question?.response?.option ?? (question.multi_select ? [] : null),
              text: question?.response?.text ?? '',
              }]
          })
        }
      })
    },
  },
  mounted () {
    this.viewDetail = !!this.$route.params.active;
    if (this.viewDetail) {
      let parseActive = parseInt(this.$route.params.active);
      if (Number.isSafeInteger(parseActive)) {
        this.setActive(parseInt(this.$route.params.active));
      }
    }
  },
  beforeUnmount () {
    localStorage.setItem('responses', JSON.stringify(this.responses));
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>