<!-- eslint-disable vue/no-v-html -->
<template>
  <div class="w-full mx-auto max-w-5xl">
    <loading-view v-if="loading"></loading-view>
    <main v-show="!loading" class="flex w-full">
      <section id="list-view" class="flex flex-col w-full py-3 px-3 md:w-[40%] lg:w-[35%]  bg-neutral dark:bg-darkNeutral h-full max-h-[82.5vh] short:max-h-[70vh] overflow-y-auto">
        <label class="flex">
          <push-subscribe></push-subscribe>
          <input v-model="search" class="rounded-lg my-auto p-3 bg-pale dark:bg-darkPale transition duration-200 focus:outline-none focus:ring-2 w-full placeholder-neutral dark:placeholder-darkNeutral" :placeholder="$t('shared.listview.search')" />
        </label>
        <ul class="mt-1 overflow-y-scroll">
          <li v-for="(obj, idx) in searchedList" :key="obj.uuid" class="py-5 border-b px-3 transition hover:bg-pale hover:dark:bg-darkPale cursor-pointer" @click="setActive(idx)">
                <div class="flex justify-between items-center">
                  <img v-if="obj?.thumbnail" class="max-w-[40%] ml-5 rounded-md shadow-lg" :src="obj.thumbnail" alt="Information article thumbnail">
                  <div class="w-full mr-5 pl-5 text-right">
                    <h3 class=" text-lg font-semibold">{{ obj?.subject }}</h3>
                    <div class="-full text-md italic text-secondary dark:text-darkSecondary" >{{ listItemContent(obj?.content, 40) }}</div>
                  </div>
                </div>
            </li>
          <li v-if="searchedList?.length == 0 && objList.length">
            <p class="p-3">{{ $t('shared.listview.noMessage') }}</p>
          </li>
          <li v-if="!objList.length">
            <p class="p-3">{{ $t('shared.listview.done') }}</p>
          </li>
        </ul>
      </section>
      <detail-view id="detail-view" :active="active" :active-object="activeObject" :searched-list="searchedList" :responses="responses" :class="{hidden: !viewDetail}" @hide-detail="hideDetail" @set-active="setActive" @submit-response="(response) => $emit('submitResponse', response, activeObject.uuid)" @delete-responses="(response) => $emit('deleteResponses', activeObject.uuid)"></detail-view>
    </main>
  </div> 
</template>

<script>
import { marked } from 'marked';
import LoadingView from '@/components/shared/LoadingView.vue';
import PushSubscribe from '@/components/shared/PushSubscribe.vue';
import DetailView from './DetailView.vue';


export default {
  name: 'ListView',
  components: {
    LoadingView,
    DetailView,
    PushSubscribe,
  },
  props: {
    objList: {type: Array},
    loading: {type: Boolean},
    error: {type: Object},
    submitLoading: {type: Boolean},
    submitError: {type:Object},
    submitSuccess: {type: Boolean},
    deleteLoading: {type: Boolean},
    deleteError: {type: Object},
    deleteSuccess: {type: Boolean},
  },
emits: ['submitResponse', 'deleteResponses'],
  data () {
    return {
      active: 0,
      viewDetail: false,
      responses: JSON.parse(localStorage.getItem('responses') ?? "[]"),
      search: '',
    };
  },
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
    $route() {
      this.refreshActive();
    }
  },
  mounted () {
    this.responseSetup();
    this.refreshActive();
  },
  beforeUnmount () {
    localStorage.setItem('responses', JSON.stringify(this.responses));
  },
  methods: {
    refreshActive () {
      this.viewDetail = !!this.$route.params.active;
      let parseActive = parseInt(this.$route.params.active);
      if (Number.isSafeInteger(parseActive)) {
        this.setActive(parseInt(this.$route.params.active));
      }
    },
    setActive(n){
      if (n < 0) {
        n = 0;
      }
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
    listItemContent(content, chars=40) {
      return content ? this.removeHtml(marked.parse(this.truncate(content, chars))) : null
    },
    hideDetail () {
      this.viewDetail = false;
      this.$route.params.active = null;
      this.$router.push({name: this.$route.name, params: {...this.$route.params}})
    },
    responseSetup () {
      this.responses = [];
      this.objList.forEach(obj => {
        if (obj.questions?.length){
          obj.questions.forEach(question => {
              this.responses = [...this.responses, {
              question: question.uuid,
              option: question?.response?.option ?? [],
              text: question?.response?.text ?? '',
              }]
          })
        }
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>