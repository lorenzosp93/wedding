<template>
  <div id="invitation-wrapper">
    <div
      id="the-invitation"
      :class="{ 'h-[200vh]': loaded }"
      class="overflow-y-hidden bg-neutral dark:bg-darkNeutral"
    >
      <div id="invitation-content" class="flex">
        <loading-view v-if="!loaded"></loading-view>
        <div
          id="envelopeContainer"
          :class="{ invisible: !loaded }"
          class="relative w-full mx-auto max-w-3xl aspect-[1.41384211] max-h-[80vh] top-20 sm:-top-24 px-1"
        >
          <img
            id="base"
            :src="images.find((img) => img.name == 'base')?.url"
            alt="Envelope base"
            class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] z-0 px-0.5"
            @load="loadImage('base')"
          />
          <img
            id="letterBase"
            :src="images.find((img) => img.name == 'letterBase')?.url"
            alt="Invitation base"
            class="max-w-[95%] max-h-[95%] aspect-auto absolute left-1/2 -translate-x-1/2 top-[37%] z-10 px-1"
            @load="loadImage('letterBase')"
          />
          <the-message class="font-[Tangerine]" />
          <img
            id="sideFlaps"
            :src="images.find((img) => img.name == 'sideFlaps')?.url"
            alt="Envelope side flaps"
            class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] z-20 px-0.5"
            @load="loadImage('sideFlaps')"
          />
          <img
            id="bottomFlap"
            :src="images.find((img) => img.name == 'bottomFlap')?.url"
            alt="Envelope bottom flap"
            class="absolute aspect-auto max-w-full max-h-[59.35%] left-1/2 -translate-x-1/2 top-[73%] z-30 px-0.5"
            @load="loadImage('bottomFlap')"
          />
          <img
            id="envelopeFlap"
            class="max-w-full max-h-[59.35%] absolute left-1/2 -translate-x-1/2 top-[32.6%] origin-top z-40 px-0.5"
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
        <chevron-double-down-icon
          class="h-10 w-10 md:h-12 md:w-12 pt-3.5 animate-bounce stroke-accent stroke-2"
        />
      </div>
      <router-link
        id="rsvp"
        :to="{ name: 'inbox' }"
        v-show="loaded"
        class="fixed w-fit bottom-0 right-1/2 short:right-0 translate-x-1/2 short:translate-x-0 z-30 rounded-md bg-accent text-primary shadow-lg px-2 py-1 mb-5 short:mr-5 opacity-0 font-[Tangerine] text-2xl cursor-pointer"
      >
        R.S.V.P.
      </router-link>
    </Teleport>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import LoadingView from "@/components/shared/LoadingView.vue";
import { ChevronDoubleDownIcon } from "@heroicons/vue/24/outline";
import TheMessage from "./shared/ui/TheMessage.vue";

gsap.registerPlugin(ScrollTrigger);

type ImageDef = {
  name: string;
  url: string;
  loaded: boolean;
};

export default defineComponent({
  name: "TheInvitation",
  components: {
    LoadingView,
    ChevronDoubleDownIcon,
    TheMessage,
  },
  data() {
    return {
      loaded: false as Boolean,
      tl: null as GSAPTimeline | null,
      images: [
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
      ] as Array<ImageDef>,
    };
  },
  beforeUnmount() {
    this.cleanup();
  },
  methods: {
    loadImage(img: string) {
      const image = this.images.find((image) => image.name == img);
      if (image) {
        image.loaded = true;
      }
      if (this.images.every((image) => image.loaded)) {
        this.loaded = true;
        this.setupEnvelopeAnimation();
      }
    },
    cleanup() {
      this.tl?.kill();
    },
    setupEnvelopeAnimation() {
      this.cleanup();
      ScrollTrigger.config({
        ignoreMobileResize: true,
      });

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: "#main",
          scrub: true,
          start: "top top",
          end: "bottom bottom",
          pin: "#envelopeContainer",
          anticipatePin: 1,
        },
      });
      tl.to("#waxSeal", {
        opacity: 0,
        duration: 0.2,
      })
        .to(
          "#envelopeFlap",
          {
            rotationX: 180,
            duration: 0.3,
          },
          0.2
        )
        .set("#envelopeFlap", { zIndex: 0 }, 0.5)
        .to(
          "#envelopeFlap, #sideFlaps, #bottomFlap, #base",
          {
            y: `+=${window.outerHeight}`,
            duration: 0.5,
            ease: "none",
          },
          0.5
        )
        .set("#scroller", { autoAlpha: 0 }, 0.5)
        .to("#rsvp", { autoAlpha: 1, duration: 0.1 }, 0.9);
      this.tl = tl;
    },
    scrollToBottom() {
      window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: "Tangerine";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: local("Tangerine"),
    url("@/assets/Tangerine-Regular.ttf") format("truetype");
}
</style>
