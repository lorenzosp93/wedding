<template>
<div id="the-invitation" :class="{'h-[200vh]': loaded}" class="overflow-y-hidden">
  <div class="flex max-h-screen">
    <loading-view v-if="!loaded"></loading-view>
    <div id="envelopeContainer" :class="{invisible: !loaded}" class="relative w-full mx-auto max-w-2xl max-h-[80vh]">
      <svg class="w-full h-full overflow-visible" viewBox="0 0 572 642" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>{{ $t('theinvitation.envelope') }}</title>
    <defs>
        <polygon id="path-1" points="1 237 24.7881718 188.473418 283.5 5.61220497e-14 542.8762 188.473418 566 237 21.245112 237"></polygon>
        <filter id="filter-2" x="-0.5%" y="-1.2%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox">
            <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
            <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
            <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
            <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
        </filter>
        <polygon id="path-3" points="17.8562676 251.52023 549.710246 251.52023 549.710246 622.52023 17.538115 622.52023"></polygon>
        <filter id="filter-4" x="-0.2%" y="-0.3%" width="100.8%" height="101.1%" filterUnits="objectBoundingBox">
            <feOffset dx="1" dy="1" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
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
            <g id="invite">
                <use fill="black" fill-opacity="1" filter="url(#filter-4)" xlink:href="#path-3"></use>
                <use fill="#FFFFFF" fill-rule="evenodd" xlink:href="#path-3"></use>
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
          <title>{{ $t('theinvitation.envelopeflap') }}</title>
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
      <img id="waxSeal" class="absolute top-[70%] -translate-y-1/2 left-1/2 -translate-x-1/2 max-h-[18%] max-w-[18%]" :src="waxSeal" @load="upsertEnvelopeAnimation">
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
import LoadingView from '@/components/shared/LoadingView.vue'

export default {
  name: 'TheInvitation',
  components: {
    LoadingView
  },
  data () {
    return {
      loaded: false,
      tl: null,
      waxSeal: new URL("../assets/waxSeal.webp", import.meta.url).href,
    }
  },
  beforeUnmount () {
    this.tl?.kill();
  },
  methods: {
    upsertEnvelopeAnimation () {
      this.loaded = true;
      this.tl?.kill();
      const tl = this.$gsap.timeline({
        scrollTrigger: {
          trigger: '#app',
          scrub: true,
          start: '1% top',
          end: 'bottom bottom',
          pin: '#envelopeContainer',
        }
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
          y: window.innerHeight,
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

</style>
