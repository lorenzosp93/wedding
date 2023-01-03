<!-- eslint-disable vue/no-v-html -->
<template>
  <article
    class="@container md:flex absolute left-0 z-10 md:relative w-full mx-auto md:w-[60%] lg:w-[65%] px-3 flex flex-col bg-neutral dark:bg-darkNeutral h-full max-h-rest"
  >
    <header
      id="object-header"
      class="flex flex-initial justify-between items-center border-b-2 mb-1 px-1"
    >
      <div
        class="p-1 mr-2 md:hidden select-none cursor-pointer"
        @click="$emit('hideDetail')"
      >
        <arrow-left-icon class="h-6 w-6" />
      </div>
      <div id="header-title" class="w-full flex py-3">
        <h3 class="font-semibold text-2xl mr-1">{{ activeObject?.subject }}</h3>
      </div>
      <div>
        <ul
          class="flex text-primary dark:text-darkPrimary ml-1 space-x-4 order-last"
        >
          <li
            :class="{ 'invisible cursor-none': !(active != 0) }"
            class="p-1 cursor-pointer select-none"
            @click="$emit('setActive', (active ?? 0) - 1)"
          >
            <arrow-up-icon class="h-6 w-6" />
          </li>
          <li
            :class="{
              'invisible cursor-none': !(
                active != (searchedList?.length ?? 0) - 1 &&
                searchedList?.length
              ),
            }"
            class="p-1 cursor-pointer select-none"
            @click="$emit('setActive', (active ?? 0) + 1)"
          >
            <arrow-down-icon class="h-6 w-6" />
          </li>
        </ul>
      </div>
    </header>
    <article class="pt-3 flex-auto overflow-y-scroll px-1">
      <section
        v-if="activeObject?.picture"
        id="object-picture"
        class="w-full @md:max-w-[60%] float-right px-3 mb-3"
      >
        <img
          :src="activeObject?.picture"
          alt="Information article picture"
          class="rounded-lg shadow-md"
        />
      </section>
      <section
        id="object-content"
        class="my-3 prose dark:prose-invert"
        v-html="markdown"
      ></section>
      <widgets-view
        v-if="activeObject?.widget?.length && loadWidgets"
        :active-object="activeObject"
      ></widgets-view>
      <question-view
        v-if="activeObject?.questions?.length"
        :questions="activeObject.questions"
        :submit-loading="submitLoading"
        :submit-error="submitError"
        :submit-success="submitSuccess"
        :delete-loading="deleteLoading"
        :delete-error="deleteError"
        :delete-success="deleteSuccess"
        @submit-response="(responses: Response[]) => $emit('submitResponse', responses)"
        @delete-responses="$emit('deleteResponses')"
      ></question-view>
    </article>
  </article>
</template>

<script lang="ts">
import { marked } from "marked";
import QuestionView from "./QuestionView.vue";
import WidgetsView from "./ui/WidgetsView.vue";
import {
  ArrowLeftIcon,
  ArrowUpIcon,
  ArrowDownIcon,
} from "@heroicons/vue/24/outline";
import { defineComponent, type PropType } from "vue";
import type {
  ListObject,
  Response,
  ResponseErrors,
} from "@/models/listObjects.interface";
import { useEventListener } from "@vueuse/core";

export default defineComponent({
  components: {
    QuestionView,
    WidgetsView,
    ArrowDownIcon,
    ArrowLeftIcon,
    ArrowUpIcon,
  },
  props: {
    viewDetail: { type: Boolean, default: false },
    activeObject: { type: Object as PropType<ListObject> },
    active: { type: Number },
    searchedList: { type: Array<ListObject> },
    submitLoading: { type: Boolean },
    submitError: { type: Array<ResponseErrors> },
    submitSuccess: { type: Boolean },
    deleteLoading: { type: Boolean },
    deleteError: { type: Array<ResponseErrors> },
    deleteSuccess: { type: Boolean },
  },
  emits: ["hideDetail", "setActive", "deleteResponses", "submitResponse"],
  data() {
    return {
      loadWidgets: false as boolean,
    };
  },
  computed: {
    markdown() {
      return marked.parse(this.activeObject?.content ?? "");
    },
  },
  mounted() {
    useEventListener("keydown", (event: KeyboardEvent) => {
      if (
        event.key == "ArrowRight" &&
        this.active &&
        this.active < (this.searchedList?.length ?? 0) - 1
      ) {
        this.$emit("setActive", this.active + 1);
      }
      if (event.key == "ArrowLeft" && this.active && this.active > 0) {
        this.$emit("setActive", this.active - 1);
      }
    });
    this.loadWidgets = true;
  },
});
</script>

<style scoped>
.max-h-rest {
  max-height: 90vh;
  max-height: calc(100vh - 4.5rem);
  max-height: calc(100svh - 4.5rem);
}
</style>
