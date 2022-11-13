<template>
<div id="the-invitation" class="h-[200vh]">
  <div class="flex max-h-screen">
    <div id="envelopeContainer" class="relative w-full mx-auto max-w-md md:max-w-2xl">
      <svg id="envelope" class="w-full overflow-visible" viewBox="0 0 572 642" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <title>envelope</title>
          <defs>
              <polygon id="path-1" points="1 237 24.7881718 188.473418 283.5 5.61220497e-14 542.8762 188.473418 566 237 21.245112 237"></polygon>
              <filter x="-0.5%" y="-1.2%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox" id="filter-2">
                  <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                  <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                  <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                  <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
              </filter>
              <polygon id="path-3" points="32.8370339 342.27023 532.538115 342.27023 532.538115 623.52023 32.538115 623.52023"></polygon>
              <filter x="-0.2%" y="-0.4%" width="100.8%" height="101.4%" filterUnits="objectBoundingBox" id="filter-4">
                  <feOffset dx="1" dy="1" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
                  <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                  <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.5 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
              </filter>
              <polygon id="path-5" points="1.000015 237.17223 283.682115 473.20623 566.217115 236.91623 566.217115 636.91663 1.000015 636.91663"></polygon>
              <filter x="-0.4%" y="-0.9%" width="101.2%" height="102.0%" filterUnits="objectBoundingBox" id="filter-6">
                  <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                  <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                  <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                  <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.298978365 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
              </filter>
              <polygon id="path-7" points="0 637 23.8302747 588.473418 283 400 542.835273 588.473418 566 636.91663 20.2809441 637"></polygon>
              <filter x="-0.5%" y="-1.2%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox" id="filter-8">
                  <feMorphology radius="0.5" operator="dilate" in="SourceAlpha" result="shadowSpreadOuter1"></feMorphology>
                  <feOffset dx="1" dy="1" in="shadowSpreadOuter1" result="shadowOffsetOuter1"></feOffset>
                  <feGaussianBlur stdDeviation="0.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
                  <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.304769449 0" type="matrix" in="shadowBlurOuter1"></feColorMatrix>
              </filter>
            </defs>
          <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g id="envelope" transform="translate(1.661885, 1.729770)">
                  <g class="invisible" id="topFlap">
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
      <svg id="envelopeFlap" class="w-full absolute top-0 translate-y-[99.8%] translate-x-[0.4%] origin-top" viewBox="0 0 572 241" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <title>envelopeFlap</title>
          <defs>
              <polygon id="path-1" points="1.661885 237.72977 25.5342627 189.203188 285.161885 0.72977 545.456231 189.203188 568.661885 237.72977 21.9786611 237.72977"></polygon>
              <filter x="-0.5%" y="-2.0%" width="101.4%" height="103.1%" filterUnits="objectBoundingBox" id="filter-2">
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
      <img @load="upsertEnvelopeAnimation" id="waxSeal" class="absolute top-[70%] -translate-y-[50%] left-1/2 -translate-x-1/2 w-[18%]" :src="require('@/assets/waxSeal.webp')">
    </div>
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
  mounted () {
    try {
      screen.orientation.lock('portrait');
    } catch (error) {console.log(error)}
  },
  beforeUnmount () {
    this.tl?.kill();
    screen.orientation.unlock();
  },
  methods: {
    upsertEnvelopeAnimation () {
      let envelope = document.querySelectorAll("#envelope")[0];
      let topFlap = document.querySelectorAll("#topFlap")[0];
      let invite = document.querySelectorAll("#invite")[0];

      let flapRatio = 2.5 * topFlap.getBoundingClientRect().height / (envelope.getBoundingClientRect().height + invite.getBoundingClientRect().height);

      this.tl?.kill();

      const tl = this.$gsap.timeline({
        scrollTrigger: {
          trigger: '#app',
          scrub: true,
          start: 'top top',
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
        .to(envelope, {
          y: flapRatio * envelope.getBoundingClientRect().height,
          duration: 0.5,
          ease: 'none',
        }, 0.5)
        .to(invite, {
          y: - flapRatio * (envelope.getBoundingClientRect().height + invite.getBoundingClientRect().height),
          duration: 0.5,
          ease: 'none',
        }, 0.5);
      this.tl = tl;
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
