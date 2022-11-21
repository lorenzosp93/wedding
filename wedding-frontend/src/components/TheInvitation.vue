<template>

<div id="the-invitation" :class="{'h-[200vh]': loaded}" class="overflow-y-hidden ">
  <div id="invitation-content" class="flex max-h-screen">
    <loading-view v-if="!loaded"></loading-view>
    <div id="envelopeContainer" :class="{invisible: !loaded}" class="relative w-full mx-auto max-w-3xl max-h-screen top-10 sm:-top-20 lg:-top-40">
      <svg class="w-full h-full overflow-visible" viewBox="0 0 572 642" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <polygon id="path-1" points="1 237 24.7881718 188.473418 283.5 5.61220497e-14 542.8762 188.473418 566 237 21.245112 237"></polygon>
        <filter id="filter-2" x="-0.5%" y="-1.2%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox">
            <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
            <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
            <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
            <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
        </filter>
        <polygon id="path-3" points="0.321195 4.11996826e-14 537.261195 4.11996826e-14 537.261195 380 1.28629342e-14 380"></polygon>
        <filter id="filter-4" x="-0.5%" y="-0.7%" width="101.3%" height="101.8%" filterUnits="objectBoundingBox">
            <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
            <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
            <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
            <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.5 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
        </filter>
        <polygon id="path-5" points="1.000015 237.17223 283.682115 473.20623 566.217115 236.91623 566.217115 636.91663 1.000015 636.91663"></polygon>
        <filter id="filter-6" x="-0.4%" y="-0.9%" width="101.2%" height="102.0%" filterUnits="objectBoundingBox">
            <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
            <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
            <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
            <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.298978365 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
        </filter>
        <polygon id="path-7" points="0 637 23.8302747 588.473418 283 400 542.835273 588.473418 566 636.91663 20.2809441 637"></polygon>
        <filter id="filter-8" x="-0.5%" y="-1.2%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox">
            <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
            <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
            <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
            <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
        </filter>
    </defs>
    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="envelope" transform="translate(1.661885, 1.729770)">
            <g id="topFlap" class="invisible">
                <use fill="black" fill-opacity="1" filter="url(#filter-2)" xlink:href="#path-1"></use>
                <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-1"></use>
            </g>
            <polygon id="base" fill="#EAE6D3" points="1.338115 237.27023 566.538115 237.27023 566.538115 637.27023 1.000015 637.27023"></polygon>
            <g id="invite" transform="translate(15.276920, 247.270230)">
                <g>
                    <use fill="black" fill-opacity="1" filter="url(#filter-4)" xlink:href="#path-3"></use>
                    <use fill="#FFFFFF" fill-rule="evenodd" xlink:href="#path-3"></use>
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
            <g id="sideFlaps">
                <use fill="black" fill-opacity="1" filter="url(#filter-6)" xlink:href="#path-5"></use>
                <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-5"></use>
            </g>
            <g id="bottomFlap">
                <use fill="black" fill-opacity="1" filter="url(#filter-8)" xlink:href="#path-7"></use>
                <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-7"></use>
            </g>
        </g>
    </g>
      </svg>
      <svg id="envelopeFlap" class="w-full h-full absolute top-[37.25%] origin-top" viewBox="-1 1 572 642" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <defs>
              <polygon id="path-1" points="1.661885 237.72977 25.5342627 189.203188 285.161885 0.72977 545.456231 189.203188 568.661885 237.72977 21.9786611 237.72977"></polygon>
              <filter id="filter-2" x="-0.5%" y="-2.0%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox">
                  <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                  <feOffset dx="1" dy="-1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                  <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                  <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
              </filter>
          </defs>
          <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g id="envelopeFlap" transform="translate(285.161885, 119.229770) scale(1, -1) translate(-285.161885, -119.229770) ">
                  <use fill="black" fill-opacity="1" filter="url(#filter-2)" xlink:href="#path-1"></use>
                  <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-1"></use>
              </g>
          </g>
      </svg>
      <img id="waxSeal" class="absolute top-[70%] -translate-y-1/2 left-1/2 -translate-x-1/2 max-h-[18%] max-w-[18%]" :src="waxSeal" aria-label="Wax seal on the envelope" @load="upsertEnvelopeAnimation">
    </div>
  </div>
  <div id="scroller" :class="{invisible: !loaded}" class="fixed bottom-5 right-5 flex">
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
      waxSeal: new URL("@/assets/waxSeal.webp", import.meta.url).href,
    }
  },
  beforeUnmount () {
    this.tl?.kill();
  },
  methods: {
    upsertEnvelopeAnimation () {
      this.loaded = true;

      ScrollSmoother.create({
        smooth: 5,
        effects: true,
        smoothTouch: 0.5,
        normalizeScroll: false,
        ignoreMobileResize: true,
        content: '#main',
        wrapper: '#app'
      });
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: '#main',
          scrub: true,
          start: '1% top',
          end: 'bottom bottom',
          pin: '#envelopeContainer',
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
        .set('#envelopeFlap', {autoAlpha: 0}, 0.5)
        .set('#topFlap', {autoAlpha: 1}, 0.5)
        .to('#topFlap, #sideFlaps, #bottomFlap, #base', {
          y: `+=${window.innerHeight}`,
          duration: 0.5,
          ease: 'none',
        }, 0.5)
        .set('#scroller', {autoAlpha: 0}, 1.0)
      this.tl = tl;
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Tangerine&display=swap');
</style>
