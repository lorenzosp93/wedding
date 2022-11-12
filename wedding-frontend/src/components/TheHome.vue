<template>
  <div class="flex flex-col mx-auto max-w-2xl">
    <div class="max-w-xl mx-auto">
      <div class="max-w-xl my-3 mx-3 p-5 rounded-md bg-pale dark:bg-darkPale ring-1 ring-accent shadow-md">
        <p class="mx-auto mt-2">{{ $t('thehome.hi', { 'a': profile?.user.first_name }) }}</p>
        <p class="mx-auto mt-2 font-thin">{{ $t('thehome.weAreDelighted') }}</p>
        <p class="mx-auto mt-2 font-thin">{{ $t('thehome.withLove') }}</p>
        <p class="mx-auto mt-2 font-thin">{{ $t('thehome.priscillaAndLorenzo') }}</p>
    </div>
    </div>
  </div>
</template>

<script>
import profile from '@/mixins/profile'

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
