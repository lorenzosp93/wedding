<template>
<div>
  <div id="the-invitation" :class="{'h-[200vh]': loaded}" class="overflow-y-hidden ">
    <div id="invitation-content" class="flex ">
      <loading-view v-if="!loaded"></loading-view>
      <div id="envelopeContainer" :class="{invisible: !loaded}" class="relative w-full mx-auto max-w-3xl aspect-[1.41384211] max-h-[80vh] top-40 sm:-top-20">
        <img id="base" :src="images.find(img => img.name == 'base').url" alt="Envelope base" class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.2%] z-0 px-1" @load="loadImage('base')">
        <svg class="z-10 w-full max-h-full p-3 absolute left-1/2 -translate-x-1/2 top-[33%]" viewBox="0 0 543 384" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <defs>
            <polygon id="path-1" points="0.321195 4.11996826e-14 537.261195 4.11996826e-14 537.261195 380 1.28629342e-14 380"></polygon>
            <filter id="filter-2" x="-0.5%" y="-0.7%" width="101.3%" height="101.8%" filterUnits="objectBoundingBox">
                <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.5 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
            </filter>
        </defs>
        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g id="invite" transform="translate(1.661885, 1.729770)">
            <g>
                <use fill="black" fill-opacity="1" filter="url(#filter-2)" xlink:href="#path-1"></use>
                <use fill="#FFFFFF" fill-rule="evenodd" xlink:href="#path-1"></use>
            </g>
                  <text id="Daniel-Cabrera-Uscan" font-family="Tangerine-Regular, Tangerine" font-size="18" font-weight="normal" letter-spacing="0.00145161749" fill="#1F4045">
                      <tspan x="30.1843401" y="55">{{ $t('theinvitation.danielCabreraUscangaAndReginaMatos') }}</tspan>
                      <tspan x="35.5853562" y="73">{{ $t('theinvitation.canoCommunicateTheWeddingOfTheirDaughter') }}</tspan>
                      <tspan x="102.669759" y="91">{{ $t('theinvitation.priscillaWith') }}</tspan>
                  </text>
                  <text id="Renato-R.-Spinelli-e" font-family="Tangerine-Regular, Tangerine" font-size="18" font-weight="normal" letter-spacing="0.00145161749" fill="#1F4045">
                      <tspan x="312.86034" y="55">{{ $t('theinvitation.renatoRSpinelliAndVincenzaAlessio') }}</tspan>
                      <tspan x="303.988082" y="73">{{ $t('theinvitation.ruffoDiCalabriaCommunicateTheWeddingOf') }}</tspan>
                      <tspan x="359.472501" y="91">{{ $t('theinvitation.theirSonLorenzoWith') }}</tspan>
                  </text>
                  <text id="Lorenzo-Spinelli" font-family="Tangerine-Regular, Tangerine" font-size="21" font-weight="normal" letter-spacing="0.00169355374" fill="#1F4045">
                      <tspan x="88.1421466" y="145">{{ $t('theinvitation.lorenzoSpinelli') }}</tspan>
                  </text>
                  <text id="Priscilla-Cabrera-Ma" font-family="Tangerine-Regular, Tangerine" font-size="21" font-weight="normal" letter-spacing="0.00169355374" fill="#1F4045">
                      <tspan x="335.094719" y="145">{{ $t('theinvitation.priscillaCabreraMatos') }}</tspan>
                  </text>
                  <text id="Domenica,-1-ottobre" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="209.603872" y="193">{{ $t('theinvitation.sundayOct1st2023h1630') }}</tspan>
                  </text>
                  <text id="Roma" font-family="Tangerine-Regular, Tangerine" font-size="16" font-weight="normal" letter-spacing="0.00129032666" fill="#1F4045">
                      <tspan x="254.770614" y="244">{{ $t('theinvitation.rome') }}</tspan>
                  </text>
                  <text id="Amsterdam,-the-Nethe" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="216.588518" y="294">{{ $t('theinvitation.amsterdamTheNetherlands') }}</tspan>
                      <tspan x="223.722082" y="309">{{ $t('theinvitation.witteDeWithstraat1601') }}</tspan>
                  </text>
                  <text id="Roma,-Italia-via-Ett" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="445.546421" y="346">{{ $t('theinvitation.romeItaly') }}</tspan>
                      <tspan x="433.899211" y="361">{{ $t('theinvitation.viaEttorePetrolini11') }}</tspan>
                  </text>
                  <text id="Puebla,-Messico-Pase" font-family="Tangerine-Regular, Tangerine" font-size="14" font-weight="normal" letter-spacing="0.00112903583" fill="#1F4045">
                      <tspan x="41.8317272" y="331">{{ $t('theinvitation.pueblaMexico') }}</tspan>
                      <tspan x="26.3415175" y="346">{{ $t('theinvitation.paseoToscana165Cluster') }}</tspan>
                      <tspan x="26.6990821" y="361">{{ $t('theinvitation.888LomasDeAngelopolis') }}</tspan>
                  </text>
                  <text id="Basilica-dei-Santi-G" font-family="Tangerine-Regular, Tangerine" font-size="21" font-weight="normal" letter-spacing="0.00169355374" fill="#1F4045">
                      <tspan x="154.248437" y="219">{{ $t('theinvitation.basilicaDeiSantiGiovanniEPaoloAlCelio') }}</tspan>
                  </text>
              </g>
          </g>
        </svg>
        <img id="sideFlaps" :src="images.find(img => img.name == 'sideFlaps').url" alt="Envelope side flaps" class="max-w-full max-h-full aspect-auto absolute left-1/2 -translate-x-1/2 top-[32.3%] z-20 px-0.5" @load="loadImage('sideFlaps')">
        <img id="bottomFlap" :src="images.find(img => img.name == 'bottomFlap').url" alt="Envelope bottom flap" class="absolute aspect-auto max-w-full max-h-[60%] left-1/2 -translate-x-1/2 top-[72.5%] z-30 px-0.5" @load="loadImage('bottomFlap')">
        <img id="envelopeFlap" class="max-w-full max-h-[60%] absolute left-1/2 -translate-x-1/2 top-[32.3%] origin-top z-40 px-0.5" :src="images.find(img => img.name == 'envelopeFlap').url" :aria-label="$t('theinvitation.envelopeFlap')" @load="loadImage('envelopeFlap')">
        <img id="waxSeal" class="absolute top-[88%] -translate-y-1/2 left-1/2 -translate-x-1/2 max-h-[25%] max-w-[25%] z-50" :src="images.find(img => img.name == 'waxSeal').url" :aria-label="$t('theinvitation.waxSealOn')" @load="loadImage('waxSeal')">
      </div>
    </div>
  </div>

  <Teleport to="body">
    <div id="scroller" :class="{invisible: !loaded}" class="fixed w-fit bottom-0 right-0 py-2 flex z-20 font-serif text-accent" >
      <p>{{ $t('theinvitation.scrollDown') }}</p>
      <svg
    class="h-7 w-7 block m-auto pt-3.5 animate-bounce fill-accent" version="1.1" xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 1000 1000" xml:space="preserve">
          <g>
            <path
              d="M34.6,228.4L472,481c8.8,5.1,18.5,7.1,28,6.4c9.5,0.7,19.2-1.3,28-6.4l437.4-252.6c23.7-13.7,31.6-44.3,17.7-68.4c-13.9-24.1-44.4-32.5-68.1-18.8L500,380.9L84.9,141.2C61.2,127.5,30.8,136,16.9,160C2.9,184.1,10.9,214.7,34.6,228.4z" />
            <path
              d="M915.1,519L500,758.7L84.9,519c-23.7-13.7-54.2-5.2-68.1,18.8c-13.9,24.1-6,54.7,17.7,68.4L472,858.8c8.8,5.1,18.5,7.1,28,6.4c9.5,0.7,19.2-1.3,28-6.4l437.4-252.6c23.7-13.7,31.6-44.3,17.7-68.4C969.2,513.8,938.8,505.4,915.1,519z" />
          </g>
      </svg>
    </div>

  </Teleport>
</div>



</template>
  
<script>
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ScrollSmoother } from "gsap/ScrollSmoother";
import LoadingView from '@/components/shared/LoadingView.vue'

gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

export default {
  name: 'TheInvitation',
  components: {
    LoadingView
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
        this.upsertEnvelopeAnimation();
      }
    },
    cleanup () {
      this.tl?.kill();
      this.smoother?.kill();
    },
    upsertEnvelopeAnimation () {
      this.cleanup();

      this.smoother = ScrollSmoother.create({
        smoothTouch: 0.1,
        ignoreMobileResize: true,
        normalizeScroll: true,
        content: '#main',
        wrapper: '#app'
      });
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: '#the-invitation',
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
        // .set('#topFlap', {autoAlpha: 1}, 0.5)
        .to('#envelopeFlap, #sideFlaps, #bottomFlap, #base', {
          y: `+=${window.innerHeight}`,
          duration: 0.5,
          ease: 'none',
        }, 0.5)
        .set('#scroller', {autoAlpha: 0}, .6);
      this.tl = tl;
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
