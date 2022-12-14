<template>
<div>
  <div id="the-invitation" :class="{'h-[200vh]': loaded}" class="overflow-y-hidden">
    <div id="invitation-content" class="flex ">
      <loading-view v-if="!loaded"></loading-view>
      <div id="envelopeContainer" :class="{invisible: !loaded}" class="relative w-full mx-auto max-w-3xl aspect-[1.41384211] max-h-[80vh] top-40 sm:-top-24 px-1">
        <img id="base" :src="images.find(img => img.name == 'base').url" alt="Envelope base" class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] z-0 px-0.5" @load="loadImage('base')">
        <img id="letterBase" :src="images.find(img => img.name == 'letterBase').url" alt="Invitation base" class="max-w-[95%] max-h-[95%] aspect-auto absolute left-1/2 -translate-x-1/2 top-[37%] z-10 px-1" @load="loadImage('letterBase')">
        <svg class="z-10 w-full max-h-full p-3 absolute left-1/2 -translate-x-1/2 top-[33%]" viewBox="0 0 543 384" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <defs>
        </defs>
        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g id="invite" transform="translate(1.661885, 1.729770)">
                  <text id="Daniel-Cabrera-Uscan" font-family="Tangerine-Regular, Tangerine" font-size="18" font-weight="normal" letter-spacing="0.00145161749" fill="#1F4045">
                      <tspan x="135.75" text-anchor="middle" y="55">{{ $t('theinvitation.danielCabreraUscangaAndReginaMatos') }}</tspan>
                      <tspan x="135.75" text-anchor="middle" y="73">{{ $t('theinvitation.canoCommunicateTheWeddingOfTheirDaughter') }}</tspan>
                      <tspan x="135.75" text-anchor="middle" y="91">{{ $t('theinvitation.priscillaWith') }}</tspan>
                  </text>
                  <text id="Renato-R.-Spinelli-e" font-family="Tangerine-Regular, Tangerine" font-size="18" font-weight="normal" letter-spacing="0.00145161749" fill="#1F4045">
                      <tspan x="407.25" text-anchor="middle" y="55">{{ $t('theinvitation.renatoRSpinelliAndVincenzaAlessio') }}</tspan>
                      <tspan x="407.25" text-anchor="middle" y="73">{{ $t('theinvitation.ruffoDiCalabriaCommunicateTheWeddingOf') }}</tspan>
                      <tspan x="407.25" text-anchor="middle" y="91">{{ $t('theinvitation.theirSonLorenzoWith') }}</tspan>
                  </text>
                  <text id="Lorenzo-Spinelli" font-family="Tangerine-Regular, Tangerine" font-size="21" font-weight="normal" letter-spacing="0.00169355374" fill="#1F4045">
                      <tspan x="135.75" text-anchor="middle" y="145">{{ $t('theinvitation.lorenzoSpinelli') }}</tspan>
                  </text>
                  <text id="Priscilla-Cabrera-Ma" font-family="Tangerine-Regular, Tangerine" font-size="21" font-weight="normal" letter-spacing="0.00169355374" fill="#1F4045">
                      <tspan x="407.25" text-anchor="middle" y="145">{{ $t('theinvitation.priscillaCabreraMatos') }}</tspan>
                  </text>
                  <text id="Domenica,-1-ottobre" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="271.5" text-anchor="middle" y="193">{{ $t('theinvitation.sundayOct1st2023h1630') }}</tspan>
                  </text>
                  <text id="Roma" font-family="Tangerine-Regular, Tangerine" font-size="16" font-weight="normal" letter-spacing="0.00129032666" fill="#1F4045">
                      <tspan x="271.5" text-anchor="middle" y="244">{{ $t('theinvitation.rome') }}</tspan>
                  </text>
                  <text id="Amsterdam,-the-Nethe" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="271.5" text-anchor="middle"  y="310">{{ $t('theinvitation.amsterdamTheNetherlands') }}</tspan>
                      <tspan x="271.5" text-anchor="middle" y="325">{{ $t('theinvitation.witteDeWithstraat1601') }}</tspan>
                  </text>
                  <text id="Roma,-Italia-via-Ett" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="470" text-anchor="middle" y="338.5">{{ $t('theinvitation.romeItaly') }}</tspan>
                      <tspan x="470" text-anchor="middle" y="353">{{ $t('theinvitation.viaEttorePetrolini11') }}</tspan>
                  </text>
                  <text id="Puebla,-Messico-Pase" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="73" text-anchor="middle" y="331">{{ $t('theinvitation.pueblaMexico') }}</tspan>
                      <tspan x="73" text-anchor="middle" y="346">{{ $t('theinvitation.paseoToscana165Cluster') }}</tspan>
                      <tspan x="73" text-anchor="middle" y="361">{{ $t('theinvitation.888LomasDeAngelopolis') }}</tspan>
                  </text>
                  <text id="Basilica-dei-Santi-G" font-family="Tangerine-Regular, Tangerine" font-size="21" font-weight="normal" letter-spacing="0.00169355374" fill="#1F4045">
                      <tspan x="271.5" text-anchor="middle" y="219">{{ $t('theinvitation.basilicaDeiSantiGiovanniEPaoloAlCelio') }}</tspan>
                  </text>
              </g>
          </g>
        </svg>
        <img id="sideFlaps" :src="images.find(img => img.name == 'sideFlaps').url" alt="Envelope side flaps" class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] z-20 px-0.5" @load="loadImage('sideFlaps')">
        <img id="bottomFlap" :src="images.find(img => img.name == 'bottomFlap').url" alt="Envelope bottom flap" class="absolute aspect-auto max-w-full max-h-[59.35%] left-1/2 -translate-x-1/2 top-[73%] z-30 px-0.5" @load="loadImage('bottomFlap')">
        <img id="envelopeFlap" class="max-w-full max-h-[59.35%] absolute left-1/2 -translate-x-1/2 top-[32.6%] origin-top z-40 px-0.5" :src="images.find(img => img.name == 'envelopeFlap').url" :aria-label="$t('theinvitation.envelopeFlap')" @load="loadImage('envelopeFlap')">
        <img id="waxSeal" class="absolute top-[88%] -translate-y-1/2 left-1/2 -translate-x-1/2 max-h-[25%] max-w-[25%] z-50" :src="images.find(img => img.name == 'waxSeal').url" :aria-label="$t('theinvitation.waxSealOn')" @load="loadImage('waxSeal')">
      </div>
    </div>
  </div>

  <Teleport to="body">
    <div id="scroller" :class="{invisible: !loaded}" class="fixed w-fit bottom-0 right-1/2 translate-x-1/2 py-2 flex z-20 cursor-pointer" @click="scrollToBottom">
      <chevron-double-down-icon class="h-10 w-10 md:h-12 md:w-12 pt-3.5 animate-bounce stroke-accent stroke-2"/>
    </div>

  </Teleport>
</div>



</template>
  
<script>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ScrollSmoother } from "gsap/ScrollSmoother";
import LoadingView from '@/components/shared/LoadingView.vue'
import { ChevronDoubleDownIcon } from "@heroicons/vue/24/outline";

gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

export default {
  name: 'TheInvitation',
  components: {
    LoadingView,
    ChevronDoubleDownIcon,
  },
  data () {
    return {
      loaded: false,
      tl: null,
      smoother: null,
      images: [ 
        {
          name: 'waxSeal',
          url:  new URL("@/assets/waxSeal.webp", import.meta.url).href,
          loaded: false,
        },
        {
          name: 'envelopeFlap',
          url: new URL("@/assets/envelopeFlap.webp", import.meta.url).href,
          loaded: false,
        },
        {
          name: 'base',
          url: new URL("@/assets/base.webp", import.meta.url).href,
          loaded: false,
        },
        {
          name: 'bottomFlap',
          url: new URL("@/assets/bottomFlap.webp", import.meta.url).href,
          loaded: false,
        },
        {
          name: 'sideFlaps',
          url: new URL("@/assets/sideFlaps.webp", import.meta.url).href,
          loaded: false,
        },
        {
          name: 'letterBase',
          url: new URL("@/assets/letterBase.webp", import.meta.url).href,
          loaded: false,
        },
       ]
    }
  },
  beforeUnmount () {
    this.cleanup();
  },
  methods: {
    loadImage (img) {
      this.images.find(image => image.name == img).loaded = true;
      if (this.images.every(image => image.loaded)) {
        this.loaded = true;
        this.setupEnvelopeAnimation();
      }
    },
    cleanup () {
      this.tl?.kill();
      this.smoother?.kill();
    },
    setupEnvelopeAnimation () {
      this.cleanup();

      this.smoother = ScrollSmoother.create({
        // smoothTouch: 0.1,
        ignoreMobileResize: true,
        normalizeScroll: true,
        content: '#main',
        wrapper: '#app'
      });
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: '#main',
          scrub: true,
          start: 'top top',
          end: 'bottom bottom',
          pin: '#envelopeContainer',
          pinSpacing: false,
          anticipatePin: 1,
        },
      })
      tl
        .to('#waxSeal', {
          opacity: 0,
          duration: 0.2
        })
        .to('#envelopeFlap', {
          rotationX: 180,
          duration: 0.3,
        }, 0.2)
        .set('#envelopeFlap', {zIndex: 0}, 0.5)
        .to('#envelopeFlap, #sideFlaps, #bottomFlap, #base', {
          y: `+=${window.innerHeight}`,
          duration: 0.5,
          ease: 'none',
        }, 0.5)
        .set('#scroller', {autoAlpha: 0}, .5);
      this.tl = tl;
    },
    scrollToBottom () {
      window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'})
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @font-face {
    font-family: 'Tangerine';
    font-style: normal;
    font-weight: 400;
    font-display: swap;
    src: local('Tangerine'), url('@/assets/Tangerine-Regular.ttf') format('truetype');
  }
</style>
