<template>
  <div class="flex flex-col">
    <div class="mx-auto">
      <div class="max-w-2xl my-5 mx-3 p-5 rounded-md bg-pale dark:bg-darkPale dark:text-darkNeutral shadow-md">
        <p class="mx-auto mt-2">{{ $t('thehome.hi', { 'a': profile?.user.first_name }) }}</p>
        <p class="mx-auto mt-2 font-thin">{{ $t('thehome.weAreDelighted') }}</p>
        <p class="mx-auto mt-2 font-thin">{{ $t('thehome.withLove') }}</p>
        <p class="mx-auto mt-2 font-thin">{{ $t('thehome.priscillaAndLorenzo') }}</p>
      </div>
      <div class="flex w-fit mx-auto mt-8 bg-accent px-2 py-1 rounded-md">
        <router-link :to="{name: 'invitation'}" class="" >{{ $t('thehome.openYourInvitation') }}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import profile from '@/components/mixins/profile'

export default {
  name: 'TheHome',
  mixins: [
    profile
  ]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
