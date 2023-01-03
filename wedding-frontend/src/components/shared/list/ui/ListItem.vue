<template>
  <li class="py-5 border-b px-3 transition cursor-pointer">
    <div class="flex justify-between items-center">
      <div class="w-full px-3 text-left">
        <h3 class="text-lg font-semibold" :class="{ 'text-accent': active }">
          {{ obj?.subject }}
        </h3>
        <div
          class="w-full text-md italic text-secondary dark:text-darkSecondary pt-1"
        >
          {{ itemContent(obj?.content ?? "", 40) }}
        </div>
      </div>
      <img
        v-if="obj?.thumbnail"
        class="max-w-[40%] rounded-md shadow-lg"
        :src="obj.thumbnail"
        alt="Information article thumbnail"
      />
      <list-item-widgets
        :has-questions="hasQuestions"
        :has-responses="hasResponses"
      />
    </div>
  </li>
</template>

<script lang="ts">
import ListItemWidgets from "./ListItemWidgets.vue";
import type { ListObject, Question } from "@/models/listObjects.interface";
import { defineComponent, type PropType } from "vue";
import truncation from "@/components/mixins/truncation";

export default defineComponent({
  name: "ListItem",
  components: {
    ListItemWidgets,
  },
  props: {
    obj: { type: Object as PropType<ListObject> },
    active: { type: Boolean },
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
  mixins: [truncation],
});
</script>
