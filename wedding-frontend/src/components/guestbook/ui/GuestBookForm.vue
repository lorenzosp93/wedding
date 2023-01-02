<template>
  <div class="max-w-lg w-full mx-auto">
    <form @submit.prevent="submitEntry" class="flex flex-col">
      <label for="guestBookText"></label>
      <textarea
        v-model="text"
        id="guestBookText"
        type="text"
        class="w-full rounded-md bg-pale dark:bg-darkPale dark:placeholder-darkNeutral placeholder-secondary border-none shadow-inner focus:ring-accent"
        :placeholder="$t('guestbook.ui.guestbookform.writeAGuestbook')"
      />
      <p
        v-if="submitError?.text?.length"
        class="text-alert dark:text-darkAlert"
      >
        {{ submitError.text[0] }}
      </p>
      <button
        @click.prevent="submitEntry"
        class="rounded-md bg-accent text-primary mx-auto my-2 px-2 py-1 shadow-lg"
      >
        {{ $t("guestbook.ui.guestbookform.submit") }}
      </button>
      <p
        v-if="submitError?.non_field_errors?.length"
        class="text-alert dark:text-darkAlert"
      >
        {{ submitError.non_field_errors[0] }}
      </p>
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
