<template>
  <div class="flex flex-col max-w-2xl mx-auto">
    <div class="w-full overflow-auto px-5">
      <table class="table-auto mx-auto my-5 text-right py-3 px-5" v-if="!!profile">
        <tbody class="">
          <tr>
            <td>{{ $t('profile.theprofile.firstName') }}</td>
            <td>{{ profile.user?.first_name }}</td>
          </tr>
          <tr>
            <td>{{ $t('profile.theprofile.lastNames') }}</td>
            <td>{{ profile.user?.last_name }}</td>
          </tr>
          <tr>
            <td>{{ $t('profile.theprofile.email', ) }}</td>
            <td>{{ profile.user?.email }}</td>
          </tr>
          <tr>
            <td>{{ $t('profile.theprofile.language') }}</td>
            <td>
              <form v-if="profile?.language">
                <select class="bg-pale dark:bg-darkPale rounded-md py-1" name="language" id="lang" v-model="profile.language" @change="updateLanguage">
                  <option v-for="l in languages" :key="l.iso" :value="l.iso">{{ l.display }}</option>
                  <button ></button>
                </select>
              </form>
            </td>
          </tr>
          <tr>
            <td>{{ $t('profile.theprofile.plusOne', ) }}</td>
            <td class="flex"> <p class="my-auto">{{ profile?.plus ?? 0 }} </p>
              <button v-if="profile?.plus - profile?.childs?.length" @click="togglePlusOne" class="rounded-md bg-secondary py-1 px-2 mr-2 ml-auto">{{ $t('profile.theprofile.invite') }} </button>
              <plus-one :toggle="togglePlusOne" v-if="showPlusOne" />
            </td>
          </tr>
          <tr v-if="profile.childs.length">
            <td>
              <p>
                {{ $t('profile.theprofile.yourPlusOnes') }}
              </p>
            </td>
            <td>
              <table class="w-full text-left">
                <thead>
                  <th>{{ $t('profile.theprofile.email') }}</th>
                  <th>{{ $t('profile.theprofile.firstName') }}</th>
                  <th>{{ $t('profile.theprofile.lastNames') }}</th>
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
    <button @click="logout" class="rounded-md bg-secondary dark:bg-darkPale py-1 px-2 ml-auto mr-5">{{ $t('profile.theprofile.logOut') }}</button>
  </div>
</template>

<script>
import PlusOne from './PlusOne.vue'
import profile from '@/mixins/profile'

export default {
  
  name: 'TheProfile',
  data () {
    return {
      showPlusOne: false,
    }
  },
  components: { 
    PlusOne
   },
  mixins: [
    profile
  ],
  methods: {
    togglePlusOne(){
      this.showPlusOne = !this.showPlusOne;
    }
  },
  mounted () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

tr:not(:last-child), th {
  @apply border-b;
};
td {
  @apply py-3 pr-5 text-right;
};
td:first-child {
  @apply font-bold text-left pr-5;
};
th {
  @apply pr-5 pb-3;
}
</style>
