<template>
  <div class="flex flex-col">
    <div class="mx-auto">
      <div
        class="max-w-2xl my-5 mx-3 p-5 rounded-md bg-pale dark:bg-darkPale dark:text-darkNeutral shadow-sm prose"
      >
        <p class="mx-auto">
          {{ $t("thehome.hi", { a: authStore.profile?.user?.first_name }) }}
        </p>
        <p class="mx-auto">{{ $t("thehome.weAreDelighted") }}</p>
        <p class="mx-auto">
          {{ $t("thehome.withLove") }} <br />
          {{ $t("thehome.brideAndGroom") }}
        </p>
      </div>
      <CountDown :end-date="endDate" class="my-10 mx-auto" />
      <div
        id="invite-link"
        class="flex w-fit mx-auto my-8 bg-accent text-primary px-2 py-1 rounded-md shadow-md"
      >
        <RouterLink :to="{ name: 'invitation' }" class="flex">
          <EnvelopeIcon class="w-5 h-5 mr-1 my-auto" />
          {{ $t("thehome.openYourInvitation") }}
        </RouterLink>
      </div>
    </div>
    <OnboardingTour v-if="authStore.profile" />
    <footer class="px-2 pb-2 text-sm text-secondary absolute bottom-0 left-0">
      © Lorenzo Spinelli, 2023
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useAuthStore } from "@/stores";
import CountDown from "@/components/shared/CountDown.vue";
import OnboardingTour from "./shared/OnboardingTour.vue";
import { EnvelopeIcon } from "@heroicons/vue/24/outline";

const authStore = useAuthStore();
const endDate = ref(new Date("2023-10-01T14:30:00.00Z"));
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
