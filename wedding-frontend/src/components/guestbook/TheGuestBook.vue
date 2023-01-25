<template>
  <div class="max-w-5xl mx-auto">
    <div
      class="sticky top-0 bg-neutral dark:bg-darkNeutral w-full px-3 py-0.5 my-5"
    >
      <guest-book-form
        @submit-entry="(text: string) => {submitEntry(text)}"
        :submitLoading="submitLoading"
        :submitError="submitError"
      />
    </div>
    <div class="px-5">
      <div
        class="flex flex-wrap gap-5 rounded-md bg-pale dark:bg-darkPale p-5 mb-5 shadow-sm"
      >
        <guest-book-item
          v-for="entry in entries"
          :key="entry.uuid"
          :entry="entry"
          :own="entry.user == profile?.user?.id"
          @delete-entry="deleteEntry(entry.uuid)"
        />
        <infinite-scrolling
          @get-more-content="getMoreContent"
          :next="next ?? undefined"
          :loading="loading"
          class="m-auto cursor-pointer"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions, mapState } from "pinia";
import { useGuestBookStore, useAuthStore } from "@/stores";
import GuestBookItem from "./ui/GuestBookItem.vue";
import GuestBookForm from "./ui/GuestBookForm.vue";
import LoadingView from "../shared/LoadingView.vue";
import InfiniteScrolling from "../shared/InfiniteScrolling.vue";
import { GUESTBOOK_LIMIT } from "@/stores";

export default defineComponent({
  name: "TheGuestBook",
  components: {
    GuestBookItem,
    GuestBookForm,
    LoadingView,
    InfiniteScrolling,
  },
  data() {
    return {
      text: "" as string,
    };
  },
  computed: {
    ...mapState(useGuestBookStore, [
      "entries",
      "loading",
      "error",
      "next",
      "submitLoading",
      "submitError",
      "submitSuccess",
    ]),
    ...mapState(useAuthStore, ["profile"]),
  },
  methods: {
    ...mapActions(useGuestBookStore, [
      "getEntries",
      "submitEntry",
      "deleteEntry",
    ]),
    getMoreContent() {
      if (this.next && !this.loading) {
        this.getEntries({ force: true, next: true, limit: GUESTBOOK_LIMIT });
      }
    },
  },
  mounted() {
    this.getEntries({ limit: GUESTBOOK_LIMIT, force: false });
  },
});
</script>
