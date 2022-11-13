<template>
<div id="the-invitation" class="h-[200vh] overflow-auto">
  <div class="flex max-h-screen mt-[25vh]">
    <div id="envelopeContainer" class="relative w-full mx-auto my-auto max-w-2xl">
      <svg id='envelope' class="w-full" viewBox="0 0 572 406" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <title>envelope</title>
        <defs>
            <polygon id="path-1" points="37.832849 18.354 530.538115 18.354 530.538115 382.354 37.538115 382.354"></polygon>
            <filter x="-0.2%" y="-0.3%" width="100.8%" height="101.1%" filterUnits="objectBoundingBox" id="filter-2">
                <feOffset dx="1" dy="1" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
                <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.5 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
            </filter>
            <polygon id="path-3" points="1.000015 0.256 283.682115 236.29 566.217115 0 566.217115 400.0004 1.000015 400.0004"></polygon>
            <filter x="-0.4%" y="-0.9%" width="101.2%" height="102.0%" filterUnits="objectBoundingBox" id="filter-4">
                <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.298978365 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
            </filter>
            <polygon id="path-5" points="0 400.08377 23.8302747 351.557188 283 163.08377 542.835273 351.557188 566 400.08377 20.2809441 400.08377"></polygon>
            <filter x="-0.5%" y="-1.2%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox" id="filter-6">
                <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
            </filter>
        </defs>
        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
            <g id="envelope" transform="translate(1.661885, 2.646000)">
                <polygon id="base" fill="#EAE6D3" points="1.338115 0.354 566.538115 0.354 566.538115 400.354 1.000015 400.354"></polygon>
                <g id="invite">
                    <use fill="black" fill-opacity="1" filter="url(#filter-2)" xlink:href="#path-1"></use>
                    <use fill="#FFFFFF" fill-rule="evenodd" xlink:href="#path-1"></use>
                </g>
                <g id="sideFlaps">
                    <use fill="black" fill-opacity="1" filter="url(#filter-4)" xlink:href="#path-3"></use>
                    <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-3"></use>
                </g>
                <g id="bottomFlap">
                    <use fill="black" fill-opacity="1" filter="url(#filter-6)" xlink:href="#path-5"></use>
                    <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-5"></use>
                </g>
            </g>
        </g>
      </svg> 
      <svg id="envelopeFlap" class="w-full absolute top-[0.7%] left-[0.55%] origin-top" viewBox="0 0 573 406" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <defs>
            <polygon id="path-7" points="0 237.08377 23.8302747 188.557188 283 0.08377 542.835273 188.557188 566 237.08377 20.2809441 237.08377"></polygon>
            <filter x="-0.5%" y="-2.0%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox" id="filter-8">
                <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                <feOffset dx="1" dy="-1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
            </filter>
        </defs>
        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                <g id="envelopeFlap" transform="translate(283.000000, 118.583770) scale(1, -1) translate(-283.000000, -118.583770) ">
                    <use fill="black" fill-opacity="1" filter="url(#filter-8)" xlink:href="#path-7"></use>
                    <use fill="#EAE6D3" fill-rule="evenodd" xlink:href="#path-7"></use>
                </g>
        </g>
      </svg>
          <img @load="addEnvelopeAnimation" id="waxSeal" class="absolute top-1/2 -translate-y-[30%] left-1/2 -translate-x-1/2 w-[18%]" :src="require('@/assets/waxSeal.webp')">
    </div>
  </div>
  <div id="showInvite" class="invisible w-full fixed top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 max-h-screen">
    <object class="w-full p-5" :data="require('@/assets/invite.svg')">
  </object>
  </div>
</div>

</template>
  
<script>

export default {
  name: 'TheInvitation',
  data () {
    return {
      tl: null,
    }
  },
  beforeUnmount () {
    this.tl?.kill();
  },
  methods: {
    addEnvelopeAnimation () {
      console.log('entered')
      this.tl?.kill();
      const tl = this.$gsap.timeline({
        scrollTrigger: {
          trigger: '#the-invitation',
          scrub: true,
          start: 'top top',
          end: 'bottom bottom',
          pin: '#envelopeContainer',
        }
      })
      tl
        .to('#waxSeal', {
          opacity: 0,
          duration: 0.3
        })
        .to('#envelopeFlap', {
          rotationX: 180,
          // tranformOrigin: 'top',
          duration: 0.3,
        }, 0.3)
        .to('#invite', {
          y: '-18px',
          duration: 0.4
        }, 0.6)
        .set('#showInvite', {autoAlpha: 1}, 1.0)
        // .set('#invite', {autoAlpha: 0}, 1.0) // swap inner invite with outer one and zoom
      this.tl = tl;
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
