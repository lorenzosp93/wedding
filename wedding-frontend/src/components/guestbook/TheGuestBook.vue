<template>
  <div class="max-w-5xl mx-auto">
    <div
      class="sticky top-0 bg-neutral dark:bg-darkNeutral w-full px-3 py-0.5 my-5"
    >
      <GuestBookForm
        @submit-entry="(text: string) => {guestBookStore.submitEntry(text)}"
        :submitLoading="guestBookStore.submitLoading"
        :submitError="guestBookStore.submitError"
        v-if="authStore.isAuthenticated"
      />
    </div>
    <div class="px-5">
      <div
        class="flex flex-wrap gap-5 rounded-md bg-pale dark:bg-darkPale p-5 mb-5 shadow-sm"
      >
        <GuestBookItem
          v-for="entry in guestBookStore.entries"
          :key="entry.uuid"
          :entry="entry"
          :own="entry.user == authStore.profile?.user?.id"
          @delete-entry="guestBookStore.deleteEntry(entry.uuid)"
        />
        <InfiniteScrolling
          @get-more-content="getMoreContent"
          :next="guestBookStore.next ?? undefined"
          :loading="guestBookStore.loading"
          class="m-auto cursor-pointer"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useGuestBookStore, useAuthStore } from "@/stores";
import GuestBookItem from "./ui/GuestBookItem.vue";
import GuestBookForm from "./ui/GuestBookForm.vue";
import InfiniteScrolling from "../shared/InfiniteScrolling.vue";
import { GUESTBOOK_LIMIT } from "@/stores";

const guestBookStore = useGuestBookStore();
const authStore = useAuthStore();

function getMoreContent() {
  if (guestBookStore.next && !guestBookStore.loading) {
    guestBookStore.getEntries({
      force: true,
      next: true,
      limit: GUESTBOOK_LIMIT,
    });
  }
}

onMounted(() => {
  guestBookStore.getEntries({ limit: GUESTBOOK_LIMIT, force: false });
});
</script>
