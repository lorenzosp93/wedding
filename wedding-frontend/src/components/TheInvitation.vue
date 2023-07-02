<template>
  <div id="invitation-wrapper">
    <div
      id="the-invitation"
      :class="{ 'h-[400vh]': loaded }"
      class="overflow-y-hidden bg-neutral dark:bg-darkNeutral"
    >
      <div id="invitation-content" class="flex">
        <LoadingView v-if="!loaded" />
        <div
          id="envelopeContainer"
          :class="{ invisible: !loaded }"
          class="relative w-full mx-auto max-w-5xl aspect-[1.41384211] max-h-[72.5vh] top-20 sm:-top-24 px-1"
        >
          <img
            id="base"
            :src="images.find((img) => img.name == 'base')?.url"
            alt="Envelope base"
            class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] px-0.5"
            @load="loadImage('base')"
          />
          <div id="inviteCard">
            <img
              id="inviteBase"
              :src="images.find((img) => img.name == 'letterBase')?.url"
              alt="Invitation base"
              class="max-w-[65%] max-h-[65%] aspect-auto absolute left-1/2 -translate-x-1/2 top-[47%] z-10 px-1"
              @load="loadImage('letterBase')"
            />
            <InviteMessage
              class="max-w-[65%] max-h-[65%] font-[ClassicScriptMN] z-10 top-[47%]"
            />
          </div>
          <div id="participationCard">
            <img
              id="participationBase"
              :src="images.find((img) => img.name == 'letterBase')?.url"
              alt="Invitation base"
              class="max-w-[95%] max-h-[95%] aspect-auto absolute left-1/2 -translate-x-1/2 top-[37%] z-20 px-1"
              @load="loadImage('letterBase')"
            />
            <ParticipationMessage
              id="participationMessage"
              class="font-[ClassicScriptMN] z-20 top-[34%]"
            />
          </div>
          <img
            id="sideFlaps"
            :src="images.find((img) => img.name == 'sideFlaps')?.url"
            alt="Envelope side flaps"
            class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] z-30 px-0.5"
            @load="loadImage('sideFlaps')"
          />
          <img
            id="bottomFlap"
            :src="images.find((img) => img.name == 'bottomFlap')?.url"
            alt="Envelope bottom flap"
            class="absolute aspect-auto max-w-full max-h-[59.35%] left-1/2 -translate-x-1/2 top-[73%] z-40 px-0.5"
            @load="loadImage('bottomFlap')"
          />
          <img
            id="envelopeFlap"
            class="max-w-full max-h-[59.35%] absolute left-1/2 -translate-x-1/2 top-[32.6%] origin-top z-50 px-0.5"
            :src="images.find((img) => img.name == 'envelopeFlap')?.url"
            :aria-label="$t('theinvitation.envelopeFlap')"
            @load="loadImage('envelopeFlap')"
          />
          <img
            id="waxSeal"
            class="absolute top-[88%] -translate-y-1/2 left-1/2 -translate-x-1/2 max-h-[25%] max-w-[25%] z-50"
            :src="images.find((img) => img.name == 'waxSeal')?.url"
            :aria-label="$t('theinvitation.waxSealOn')"
            @load="loadImage('waxSeal')"
          />
        </div>
      </div>
    </div>

    <Teleport to="body">
      <div
        id="scroller"
        v-show="loaded"
        class="fixed w-fit bottom-0 right-1/2 short:right-0 translate-x-1/2 short:translate-x-0 short:mr-5 py-2 flex z-20 cursor-pointer"
        @click="scrollToBottom"
      >
        <ChevronDoubleDownIcon
          class="h-10 w-10 md:h-12 md:w-12 pt-3.5 animate-bounce stroke-accent stroke-2"
        />
      </div>
      <RouterLink
        id="rsvp"
        :to="{ name: 'inbox', params: { active: 'rsvp' } }"
        v-show="loaded"
        class="fixed w-fit bottom-0 right-1/2 short:right-0 translate-x-1/2 short:translate-x-0 z-30 rounded-md bg-accent text-primary shadow-md px-2 py-1 mb-5 short:mr-5 opacity-0 font-[ClassicScriptMN] text-2xl cursor-pointer"
        >{{ $t("theinvitation.rsvp") }}</RouterLink
      >
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import LoadingView from "@/components/shared/LoadingView.vue";
import { ChevronDoubleDownIcon } from "@heroicons/vue/24/outline";
import InviteMessage from "./shared/ui/InviteMessage.vue";
import ParticipationMessage from "./shared/ui/ParticipationMessage.vue";
import { type Ref, ref, onBeforeUnmount } from "vue";

ScrollTrigger.config({
  ignoreMobileResize: true,
});
gsap.registerPlugin(ScrollTrigger);

type ImageDef = {
  name: string;
  url: string;
  loaded: boolean;
};

const loaded = ref(false);
const tl: Ref<GSAPTimeline | null> = ref(null);

const images: Ref<ImageDef[]> = ref([
  {
    name: "waxSeal",
    url: new URL("@/assets/waxSeal.webp", import.meta.url).href,
    loaded: false,
  },
  {
    name: "envelopeFlap",
    url: new URL("@/assets/envelopeFlap.webp", import.meta.url).href,
    loaded: false,
  },
  {
    name: "base",
    url: new URL("@/assets/base.webp", import.meta.url).href,
    loaded: false,
  },
  {
    name: "bottomFlap",
    url: new URL("@/assets/bottomFlap.webp", import.meta.url).href,
    loaded: false,
  },
  {
    name: "sideFlaps",
    url: new URL("@/assets/sideFlaps.webp", import.meta.url).href,
    loaded: false,
  },
  {
    name: "letterBase",
    url: new URL("@/assets/letterBase.webp", import.meta.url).href,
    loaded: false,
  },
]);

function loadImage(img: string) {
  const image = images.value.find((image) => image.name == img);
  if (image) {
    image.loaded = true;
  }
  if (images.value.every((image) => image.loaded)) {
    loaded.value = true;
    setupEnvelopeAnimation();
  }
}

function cleanup() {
  tl.value?.kill();
  ScrollTrigger.normalizeScroll(false);
}

onBeforeUnmount(() => {
  cleanup();
});

function setupEnvelopeAnimation() {
  ScrollTrigger.normalizeScroll(true);

  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: "#main",
      scrub: true,
      start: "top top",
      end: "bottom bottom",
      pin: "#envelopeContainer",
    },
  });
  tl.to("#waxSeal", {
    opacity: 0,
    duration: 0.15,
  })
    .to(
      "#envelopeFlap",
      {
        rotationX: 180,
        duration: 0.2,
      },
      0.15
    )
    .set("#envelopeFlap", { zIndex: 0 }, 0.35)
    .set("#scroller", { autoAlpha: 0 }, 0.35)
    .to(
      "#envelopeFlap, #sideFlaps, #bottomFlap, #base",
      {
        y: `+=${window.outerHeight}px`,
        duration: 0.3,
        ease: "linear",
      },
      0.35
    )
    .to(
      "#participationBase, #participationMessage",
      {
        x: `-=${window.outerHeight}px`,
        duration: 0.3,
        ease: "linear",
      },
      0.7
    )
    .to("#rsvp", { scale: 1.2, autoAlpha: 1, duration: 0.2 }, 0.8);
  tl.value = tl;
}

function scrollToBottom() {
  window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: "ClassicScriptMN";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: local("Classic Script MN"),
    url("@/assets/ClassicScript.ttf") format("truetype");
}
</style>
