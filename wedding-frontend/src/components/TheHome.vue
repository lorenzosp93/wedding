<template>
  <div class="flex flex-col">
    <div class="mx-auto">
      <VideoEmbed
        v-if="videoLink"
        :video-link="videoLink"
        class="rounded-md mx-auto my-3 min-h-[30vh] aspect-video"
      />
      <div
        class="max-w-2xl my-5 mx-3 p-5 rounded-md bg-pale dark:bg-darkPale dark:text-darkNeutral shadow-sm prose"
      >
        <p class="mx-auto">
          {{
            $t("thehome.hi", {
              a: authStore.profile?.user?.first_name ?? $t("thehome.guest"),
            })
          }}
        </p>
        <template v-if="authStore.isAuthenticated">
          <p class="mx-auto">{{ $t("thehome.weAreDelighted") }}</p>
        </template>
        <template v-else>
          <p class="mx-auto">
            {{ $t("thehome.readOnlyIntro") }}
          </p>
        </template>
        <p class="mx-auto">
          {{ $t("thehome.withLove") }}
        </p>
        <p class="font-fancy text-2xl my-0 mx-auto">
          {{ $t("thehome.brideAndGroom") }}
        </p>
      </div>
      <CountDown
        v-if="endDate > new Date()"
        :end-date="endDate"
        class="my-10 mx-auto"
      />
      <div
        id="invite-link"
        class="flex w-fit mx-auto my-8 bg-accent text-primary px-2 rounded-md shadow-md"
      >
        <RouterLink :to="{ name: 'invitation' }" class="flex my-1">
          <EnvelopeIcon class="w-5 h-5 mr-1 my-auto" />
          <p class="mx-1 my-auto">
            {{ $t("thehome.openYourInvitation") }}
          </p>
        </RouterLink>
        <RouterLink
          v-if="!authStore.isAuthenticated"
          :to="{ name: 'login' }"
          class="flex border-l-2 dark:border-darkNeutral border-neutral pl-2 ml-2"
        >
          <UserIcon class="w-5 h-5 mr-1 my-auto" />
          <p class="mx-1 my-auto">
            {{ $t("shared.thenavbar.login") }}
          </p>
        </RouterLink>
      </div>
    </div>
    <OnboardingTour v-if="authStore.isAuthenticated" />
    <TheFooter />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useAuthStore } from "@/stores";
import TheFooter from "./ui/TheFooter.vue";
import CountDown from "@/components/shared/CountDown.vue";
import OnboardingTour from "./shared/OnboardingTour.vue";
import VideoEmbed from "./shared/VideoEmbed.vue";
import { EnvelopeIcon, UserIcon } from "@heroicons/vue/24/outline";

const videoLink = import.meta.env.VITE_APP_VIDEO_URL;
const authStore = useAuthStore();
const endDate = ref(new Date("2023-10-01T14:30:00.00Z"));
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
