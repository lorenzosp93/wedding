<template>
  <div class="flex flex-col">
    <h1 class="m-3 text-xl font-bold">User profile</h1>
    <div class="mx-auto" v-if="!!profile">
      <h1>First name: {{ profile.user?.first_name }}</h1>
      <h1>Last name(s): {{ profile.user?.last_name }}</h1>
      <h1>Email: {{ profile.user?.email }}</h1>
      <h1>Plus one: {{ profile?.plus ?? 0 }}</h1>
      <p v-if="profile.childs.length" class="font-bold"> Your plus ones </p> 
      <div v-for="child in profile?.childs" :key="child.uuid">
        <ul>
          <li>{{ child.user.email }} | {{ child.user.first_name }} {{ child.user.last_name }}</li>
        </ul>
      </div>
      
      <button v-if="profile?.plus" @click="togglePlusOne" class="rounded-md bg-secondary py-1 px-2 mx-2">Invite +1</button>
      <plus-one :toggle="togglePlusOne" v-if="showPlusOne" />
      <h1>Language:</h1>
      <form v-if="profile?.language">
        <select class="bg-pale dark:bg-darkPale rounded-md py-1" name="language" id="lang" v-model="profile.language" @change="updateLanguage">
          <option v-for="l in languages" :key="l.iso" :value="l.iso">{{ l.display }}</option>
          <button ></button>
        </select>
      </form>
    </div>
    <button @click="logout" class="rounded-md bg-accent py-1 px-2 ml-auto mr-5">Log out</button>
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
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
