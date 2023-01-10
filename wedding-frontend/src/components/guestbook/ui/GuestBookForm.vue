<template>
  <div class="w-full mx-auto bg-pale dark:bg-darkPale p-3 rounded-md shadow-sm">
    <form @submit.prevent="submitEntry" class="flex flex-col">
      <div class="flex flex-row">
        <textarea
          v-model="text"
          id="guestBookText"
          type="text"
          maxlength="280"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral dark:placeholder-darkPale placeholder-secondary border-none shadow-inner focus:ring-accent"
          :placeholder="$t('guestbook.ui.guestbookform.writeAGuestbook')"
        />
        <div class="flex flex-col">
          <span class="text-secondary ml-3 px-auto">
            {{ text?.length }}/280
          </span>
          <button
            @click.prevent="submitEntry"
            class="rounded-md bg-accent text-primary ml-3 mt-auto px-2 py-1 shadow-md"
          >
            {{ $t("guestbook.ui.guestbookform.submit") }}
          </button>
        </div>
      </div>
      <div v-if="submitError" class="flex pt-2">
        <p
          v-if="submitError?.text?.length"
          class="text-alert dark:text-darkAlert"
        >
          {{ submitError.text[0] }}
        </p>
        <p
          v-if="submitError?.non_field_errors?.length"
          class="text-alert dark:text-darkAlert"
        >
          {{ submitError.non_field_errors[0] }}
        </p>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import type { GuestBookError } from "@/models/guestbook.interface";
import { defineComponent, type PropType } from "vue";

export default defineComponent({
  name: "GuestBookForm",
  emits: ["submitEntry"],
  props: {
    submitLoading: { type: Boolean },
    submitError: { type: Object as PropType<GuestBookError> },
  },
  data() {
    return {
      text: "" as string,
    };
  },
  methods: {
    submitEntry() {
      this.$emit("submitEntry", this.text);
      this.text = "";
    },
  },
});
</script>
