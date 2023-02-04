<template>
  <div
    class="flex flex-col p-2 m-auto rounded-md shadow-sm bg-neutral dark:bg-darkNeutral w-fit max-w-md"
  >
    <div class="flex">
      <div class="flex flex-col">
        <p class="px-2" :class="{ 'text-accent': own }">
          {{ entry?.user_fullname }}
        </p>
        <p class="px-2 text-accent">{{ dateForDisplay }}</p>
      </div>
      <trash-icon
        @click="$emit('deleteEntry')"
        v-if="own"
        class="w-5 h-5 float-right ml-auto cursor-pointer"
      ></trash-icon>
    </div>

    <p class="px-2 py-1 rounded-md bg-pale dark:bg-darkPale mt-3 shadow-inner">
      {{ entry?.text }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { type PropType, computed } from "vue";
import type { GuestBookEntry } from "@/models/guestbook.interface";
import { TrashIcon } from "@heroicons/vue/24/outline";
import i18n from "@/i18n";

const props = defineProps({
  entry: { type: Object as PropType<GuestBookEntry> },
  own: { type: Boolean },
});
defineEmits(["deleteEntry"]);

const dateForDisplay = computed(() => {
  let date = new Date(props.entry?.created_at ?? "");
  return date.toLocaleDateString(i18n.global.locale.value, {
    dateStyle: "medium",
  });
});
</script>
