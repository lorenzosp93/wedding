<!-- eslint-disable vue/no-v-html -->
<template>
  <div class="w-full mx-auto max-w-5xl">
    <loading-view v-if="loading"></loading-view>
    <main v-show="!loading" class="flex w-full">
      <section
        id="list-view"
        class="flex flex-col w-full py-3 px-3 md:w-[40%] lg:w-[35%] bg-neutral dark:bg-darkNeutral h-full max-h-[82.5vh] short:max-h-[70vh] overflow-y-auto"
      >
        <label class="flex">
          <push-subscribe></push-subscribe>
          <input
            v-model.trim="search"
            class="rounded-lg my-auto p-3 bg-pale dark:bg-darkPale transition duration-200 focus:outline-none focus:ring-2 w-full placeholder-neutral dark:placeholder-darkNeutral"
            :placeholder="$t('shared.listview.search')"
          />
        </label>
        <ul class="mt-1 overflow-y-scroll">
          <list-item
            v-for="(obj, idx) in searchedList"
            :key="obj.uuid"
            @click="setActive(idx)"
            :obj="obj"
            :active="active == idx"
          />
          <li v-if="searchedList?.length == 0 && objList?.length">
            <p class="p-3">{{ $t("shared.listview.noMessage") }}</p>
          </li>
          <li v-if="!objList?.length">
            <p class="p-3">{{ $t("shared.listview.done") }}</p>
          </li>
        </ul>
      </section>
      <detail-view
        id="detail-view"
        :active="active"
        :active-object="activeObject"
        :searched-list="searchedList"
        :responses="responses"
        :class="{ hidden: !viewDetail }"
        :submit-error="submitError"
        :delete-error="deleteError"
        :submit-loading="submitLoading"
        :delete-loading="deleteLoading"
        :submit-success="submitSuccess"
        :delete-success="deleteSuccess"
        @hide-detail="hideDetail"
        @set-active="setActive"
        @submit-response="
          (response) => $emit('submitResponse', response, activeObject?.uuid)
        "
        @delete-responses="(_) => $emit('deleteResponses', activeObject?.uuid)"
      ></detail-view>
    </main>
  </div>
</template>

<script lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import PushSubscribe from "@/components/shared/PushSubscribe.vue";
import DetailView from "./DetailView.vue";
import ListItem from "./ui/ListItem.vue";
import { defineComponent, type PropType } from "vue";
import type {
  ResponseErrors,
  ListObject,
  Response,
} from "@/models/listObjects.interface";
import type { AxiosError } from "axios";

export default defineComponent({
  name: "ListView",
  components: {
    LoadingView,
    DetailView,
    PushSubscribe,
    ListItem,
  },
  props: {
    objList: { type: Array<ListObject> },
    loading: { type: Boolean },
    error: { type: Object as PropType<AxiosError> },
    submitLoading: { type: Boolean },
    submitError: { type: Array<ResponseErrors> },
    submitSuccess: { type: Boolean },
    deleteLoading: { type: Boolean },
    deleteError: { type: Array<ResponseErrors> },
    deleteSuccess: { type: Boolean },
  },
  emits: ["submitResponse", "deleteResponses"],
  data() {
    return {
      active: 0 as number,
      viewDetail: false as boolean,
      responses: JSON.parse(
        localStorage.getItem("responses") ?? "[]"
      ) as Array<Response>,
      search: "" as string,
    };
  },
  computed: {
    searchedList(): Array<ListObject> | undefined {
      if (!this.search) {
        return this.objList;
      }
      return this.objList?.filter((obj) => {
        return (
          (obj?.subject + obj?.content)
            .toLowerCase()
            .search(this.search.toLowerCase()) != -1
        );
      });
    },
    activeObject(): ListObject | undefined {
      return this.objList ? this.objList[this.active] : undefined;
    },
  },
  watch: {
    objList() {
      this.responseSetup();
    },
    $route() {
      this.refreshActive();
    },
  },
  mounted() {
    this.responseSetup();
    this.refreshActive();
  },
  beforeUnmount() {
    localStorage.setItem("responses", JSON.stringify(this.responses));
  },
  methods: {
    refreshActive() {
      this.viewDetail = !!this.$route.params.active;
      let parseActive = parseInt(this.$route.params.active as string);
      if (Number.isSafeInteger(parseActive)) {
        this.setActive(parseInt(this.$route.params.active as string));
      }
    },
    setActive(n: number) {
      if (n < 0) {
        n = 0;
      }
      this.$router.push({
        name: this.$route.name ?? undefined,
        params: { ...this.$route.params, active: `${n}` },
      });
      this.active = n;
      this.viewDetail = true;
    },
    hideDetail() {
      this.viewDetail = false;
      this.$route.params.active = "";
      this.$router.push({
        name: this.$route.name ?? undefined,
        params: { ...this.$route.params },
      });
    },
    responseSetup() {
      this.responses = new Array<Response>();
      this.objList?.forEach((obj) => {
        if (obj.questions?.length) {
          obj.questions.forEach((question) => {
            this.responses = [
              ...this.responses,
              {
                question: question.uuid,
                option: question?.response?.option ?? [],
                text: question?.response?.text ?? "",
              },
            ];
          });
        }
      });
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
