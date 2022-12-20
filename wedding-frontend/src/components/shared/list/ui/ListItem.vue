<template>
  <li class="py-5 border-b px-3 transition cursor-pointer">
    <div class="flex justify-between items-center">
      <img
        v-if="obj?.thumbnail"
        class="max-w-[40%] ml-5 rounded-md shadow-lg"
        :src="obj.thumbnail"
        alt="Information article thumbnail"
      />
      <div class="w-full mr-5 pl-5 text-left">
        <h3 class="text-lg font-semibold">{{ obj?.subject }}</h3>
        <div
          class="-full text-md italic text-secondary dark:text-darkSecondary"
        >
          {{ listItemContent(obj?.content ?? "", 40) }}
        </div>
      </div>
      <div v-if="hasResponses" class="group float-left relative mb-auto">
        <chat-bubble-left-right-icon class="w-6 h-6 stroke-secondary">
        </chat-bubble-left-right-icon>
        <span
          class="absolute w-48 -left-52 top-1/2 -translate-y-1/2 hidden group-hover:flex z-50 bg-pale dark:bg-darkPale px-2 py-1 rounded-md shadow-lg h-fit before:content-[''] before:absolute before:top-1/2 before:left-[100%] before:-translate-y-1/2 before:border-8 before:border-pale dark:before:border-darkPale dark:before:border-r-transparent before:border-r-transparent dark:before:border-y-transparent before:border-y-transparent select-none"
          >{{ $t("shared.list.ui.listitem.youAlreadyReplied") }}</span
        >
      </div>
      <div
        v-if="hasQuestions && !hasResponses"
        class="group float-left relative mb-auto"
      >
        <chat-bubble-left-icon class="w-6 h-6 stroke-accent">
        </chat-bubble-left-icon>
        <span
          class="absolute w-48 -left-52 top-1/2 -translate-y-1/2 hidden group-hover:flex z-50 bg-pale dark:bg-darkPale px-2 py-1 rounded-md shadow-lg h-fit before:content-[''] before:absolute before:top-1/2 before:left-[100%] before:-translate-y-1/2 before:border-8 before:border-pale dark:before:border-darkPale dark:before:border-r-transparent before:border-r-transparent dark:before:border-y-transparent before:border-y-transparent select-none"
          >{{ $t("shared.list.ui.listitem.youStillHavent") }}</span
        >
      </div>
    </div>
  </li>
</template>

<script lang="ts">
import type { ListObject, Question } from "@/models/listObjects.interface";
import { defineComponent, type PropType } from "vue";
import { marked } from "marked";
import {
  ChatBubbleLeftIcon,
  ChatBubbleLeftRightIcon,
} from "@heroicons/vue/24/outline";

export default defineComponent({
  name: "ListItem",
  components: {
    ChatBubbleLeftIcon,
    ChatBubbleLeftRightIcon,
  },
  props: {
    obj: { type: Object as PropType<ListObject> },
  },
  computed: {
    hasQuestions() {
      return !!this?.obj?.questions?.length;
    },
    hasResponses() {
      return (
        this.hasQuestions &&
        !!this?.obj?.questions?.every((q: Question) => q.response)
      );
    },
  },
  methods: {
    listItemContent(content: string, chars: number = 40): string {
      return content
        ? this.removeHtml(marked.parse(this.truncate(content, chars)))
        : "";
    },
    removeHtml(value: string): string {
      const div = document.createElement("div");
      div.innerHTML = value;
      const text = div.textContent || div.innerText || "";
      return text;
    },
    truncate(value: string, length: number): string {
      if (!value) return "";
      value = value.toString();
      if (value.length > length) {
        return value.substring(0, length) + "...";
      } else {
        return value;
      }
    },
  },
});
</script>

<style></style>
