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
        class="max-w-[40%] rounded-md shadow-sm"
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

<script setup lang="ts">
import ListItemWidgets from "./ListItemWidgets.vue";
import type { IListObject, IQuestion } from "@/models/listObjects.interface";
import { computed, type PropType } from "vue";
import { itemContent } from "@/components/composables/truncation";

const props = defineProps({
  obj: { type: Object as PropType<IListObject> },
  active: { type: Boolean },
});

const hasQuestions = computed(() => {
  return !!props.obj?.questions?.length;
});
const hasResponses = computed(() => {
  return (
    hasQuestions && !!props.obj?.questions?.every((q: IQuestion) => q.response)
  );
});
</script>
