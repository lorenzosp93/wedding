<template>
  <div class="flex flex-col">
    <div class="mx-auto">
      <div class="max-w-2xl my-5 mx-3 p-5 rounded-md bg-pale dark:bg-darkPale dark:text-darkNeutral shadow-md prose">
        <p class="mx-auto">{{ $t('thehome.hi', { 'a': profile?.user.first_name }) }}</p>
        <p class="mx-auto">{{ $t('thehome.weAreDelighted') }}</p>
        <p class="mx-auto">{{ $t('thehome.withLove') }} <br>
        {{ $t('thehome.priscillaAndLorenzo') }}</p>
      </div>
      <count-down :end-date="endDate" class="my-10"></count-down>
      <div id="invite-link" class="flex w-fit mx-auto my-8 bg-accent text-primary px-2 py-1 rounded-md shadow-md">
        <router-link :to="{name: 'invitation'}" class="" >{{ $t('thehome.openYourInvitation') }}</router-link>
      </div>
    </div>
    <onboarding-tour></onboarding-tour>
  </div>
</template>

<script>
import profile from '@/components/mixins/profile'
import CountDown from '@/components/shared/CountDown.vue'
import OnboardingTour from './shared/OnboardingTour.vue'

export default {
  name: 'TheHome',
  components: {
    CountDown,
    OnboardingTour
  },
  mixins: [
    profile
  ],
  data () {
    return {
      endDate: new Date('2023-10-01T14:30:00.00Z'),
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
