<template>
  <div class="p-2 dark:bg-darkNeutral bg-neutral rounded-md w-full">
    <FunnelIcon class="w-6 h-6 stroke-2 my-auto stroke-accent mr-3" />
    <div class="overflow-x-scroll gap-2 flex flex-row ml-auto">
      <div
        v-for="type in photoTypes"
        :key="type"
        class="px-2 py-1 rounded-md cursor-pointer text-primary"
        :class="{
          'bg-accent dark:bg-darkAccent': type === activeType,
          'bg-pale dark:bg-darkPale': type !== activeType,
        }"
        @click="handleTypeUpdate(type)"
      >
        {{ type }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { FunnelIcon } from "@heroicons/vue/24/outline";
import type { PropType } from "vue";

const props = defineProps({
  photoTypes: {
    type: Array as PropType<string[]>,
    required: true,
  },
  activeType: {
    type: String,
    required: true,
    default: "",
  },
});

const emit = defineEmits(["update:activeType"]);
function handleTypeUpdate(type: string) {
  if (type === props.activeType) {
    type = "";
  }
  emit("update:activeType", type);
}
</script>
