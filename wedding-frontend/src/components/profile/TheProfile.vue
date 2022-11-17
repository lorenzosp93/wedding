<template>
  <div class="flex flex-col max-w-2xl mx-auto">
    <div class="w-full overflow-auto px-5">
      <table v-if="!!profile" id="mainTable" class="table-auto mx-auto my-5 text-right py-3 px-5">
        <tbody class="">
          <tr>
            <td>{{ $t('profile.theprofile.first_name') }}</td>
            <td>{{ profile.user?.first_name }}</td>
          </tr>
          <tr>
            <td>{{ $t('profile.theprofile.last_name') }}</td>
            <td>{{ profile.user?.last_name }}</td>
          </tr>
          <tr>
            <td>{{ $t('profile.theprofile.email', ) }}</td>
            <td>{{ profile.user?.email }}</td>
          </tr>
          <tr v-if="profile?.plus">
            <td>{{ $t('profile.theprofile.plusOne', ) }}</td>
            <td class="flex w-full"> 
              <p class="my-auto ml-auto">{{ profile.plus }} </p>
              <div v-if="profile?.plus - profile?.childs?.length" class="ml-auto mr-2">
                <button  class="rounded-md bg-secondary py-1 px-2" @click="togglePlusOne">{{ $t('profile.theprofile.invite') }} </button>
                <plus-one v-if="showPlusOne" :toggle="togglePlusOne" />
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="profile?.childs.length" class="w-full overflow-auto px-5">
      <p class="font-bold">
        {{ $t('profile.theprofile.yourPlusOnes') }}
      </p>
      <table class="table-auto mx-auto my-5 text-right py-3 px-5">
        <tbody>
          <tr >
            <td>
              <table class="w-full text-left">
                <thead>
                  <th>{{ $t('profile.theprofile.email') }}</th>
                  <th>{{ $t('profile.theprofile.first_name') }}</th>
                  <th>{{ $t('profile.theprofile.last_name') }}</th>
                </thead>
                <tbody>
                  <tr v-for="child in profile?.childs" :key="child.uuid">
                    <td>{{ child.user.email}}</td>
                    <td>{{ child.user.first_name}}</td>
                    <td>{{ child.user.last_name}}</td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <button class="rounded-md bg-secondary dark:bg-darkPale py-1 px-2 ml-auto mr-5 my-3" @click="logout">{{ $t('profile.theprofile.logOut') }}</button>
  </div>
</template>

<script>
import PlusOne from './PlusOne.vue'
import profile from '@/components/mixins/profile'

export default {
  
  name: 'TheProfile',
  components: { 
    PlusOne
   },
  mixins: [
    profile
  ],
  data () {
    return {
      showPlusOne: false,
    }
  },
  mounted () {
  },
  methods: {
    togglePlusOne(){
      this.showPlusOne = !this.showPlusOne;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

tr:not(:last-child), th {
  @apply border-b;
};
td {
  @apply py-3 pr-5 text-right pl-3;
};
#mainTable td:first-child {
  @apply font-bold text-left pr-5;
};
th {
  @apply pr-5 pb-3;
}
</style>
