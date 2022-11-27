<template>
  <div class="z-20 absolute left-0 top-0 backdrop-blur-sm h-screen w-screen" @click="toggle">
  </div>
  <div
class="z-30 absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2
 rounded-lg bg-pale dark:bg-darkPale ring-1 ring-accent p-3 w-full max-w-sm">
    <form class="flex flex-wrap" @submit="setupPlusOne">
      <div v-for="field in submit" :key="field.name" class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" :for="field.name">{{ $t('profile.plusone.' + field.name) }}</label>
        <input v-model="submit.find(x=>x.name == field.name).value" class="w-full rounded-md bg-neutral dark:bg-darkNeutral" :type="field.name == 'email' ? field.name : 'text'">
        <p v-if="error ? error[field.name] : false" class="text-alert mx-3">{{ error[field.name][0] }}</p>
      </div>
      <p v-if="error?.non_field_errors" class="text-alert mx-auto">{{ error.non_field_errors }}</p>
      <div class="relative w-full h-16">
        <button v-show="!loading & !success" class="flex mx-auto px-2 py-1 bg-accent rounded-md my-5" @click.prevent="setupPlusOne">{{ $t('profile.plusone.submit') }}</button>
        <loading-view v-if="loading"></loading-view>
        <p v-if="success">{{ $t('profile.plusone.success') }}</p>
      </div>
    </form>


  </div>
</template>

<script>
import ApiService from './../../services/api.service';
import LoadingView from '@/components/shared/LoadingView.vue'

export default {
  name: 'PlusOne',
  components: {LoadingView},
  props: {
    toggle: {type: Function}
  },
  data () {
    return {
      submit: [ 
        {
          name: 'email',
          value: ''
        },
        {
          name: 'first_name',
          value: ''
        },
        {
          name: 'last_name',
          value: ''
        },
      ],
      error: null,
      loading: false,
      success: false,
    }
  },
  computed: {
  },
  mounted () {
  },
  methods: {
    setupPlusOne(){
      this.loading = true;
      console.log(this.submit)
      ApiService.setupPlusOne(
        this.submit.find(x => x.name == 'email').value,
        this.submit.find(x => x.name == 'first_name').value,
        this.submit.find(x => x.name == 'last_name').value,
      ).then(
        (response) => {
          if(response.status == 200){
            this.error = null;
            this.loading = false;
            this.success = true;
            setTimeout(() => this.toggle(), 2000)
          }
        },
        (error) => {
          this.loading = false;
          this.error = error.response.data;
        }
      )
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
