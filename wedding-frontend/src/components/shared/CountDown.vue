<template>
      <div class="text-3xl md:text-6xl text-center flex w-full items-center justify-center dark:text-darkPale">
            <div class="text-2xl mr-1 font-extralight">in</div>
            <div class=" mx-1 p-2 rounded-lg">
                <div class="p-1 leading-none" :x-text="$t('shared.countdown.days')">{{ days }}</div>
                <div class="uppercase text-sm leading-none">{{ $t('shared.countdown.days') }}</div>
            </div>
            <div class=" mx-1 p-2 rounded-lg">
                <div class="p-1 leading-none" :x-text="$t('shared.countdown.hours')">{{ hour }}</div>
                <div class="uppercase text-sm leading-none">{{ $t('shared.countdown.hours') }}</div>
            </div>
            <div class=" mx-1 p-2 rounded-lg">
                <div class="p-1 leading-none" :x-text="$t('shared.countdown.minutes')">{{ min }}</div>
                <div class="uppercase text-sm leading-none">{{ $t('shared.countdown.minutes') }}</div>
            </div>
            <div class=" mx-1 p-2  rounded-lg">
                <div class="p-1 leading-none" :x-text="$t('shared.countdown.seconds')">{{ sec }}</div>
                <div class="uppercase text-sm leading-none">{{ $t('shared.countdown.seconds') }}</div>
            </div>
        </div>
</template>

<script>
export default {
  name: 'CountDown',
  props : {
    endDate : {  // pass date object till when you want to run the timer
      type : Date,
      default(){
        return new Date()
      }
    },
    negative : {  // optional, should countdown after 0 to negative
      type : Boolean,
      default : false
    }
  },
  data () {
    return{
      now : new Date(),
      timer : null
    }
  },
  computed:{
    days () {
      let d = Math.trunc((this.endDate - this.now) / 1000 / 3600 / 24);
      return d>9?d:'0'+d;
    },
    hour () {
      let h = Math.trunc((this.endDate - this.now) / 1000 / 3600) % 24;
      return h>9?h:'0'+h;
    },
    min () {
      let m = Math.trunc((this.endDate - this.now) / 1000 / 60) % 60;
      return m>9?m:'0'+m;
    },
    sec () {
      let s = Math.trunc((this.endDate - this.now)/1000) % 60
      return s>9?s:'0'+s;
    }
  },
  watch : {
    endDate : {
      immediate : true,
      handler(newVal){
        if(this.timer){
          clearInterval(this.timer)
        }
        this.timer = setInterval(()=>{
          this.now = new Date()
          if(this.negative)
            return
          if(this.now > newVal){
            this.now = newVal
            clearInterval(this.timer)
          }
        }, 1000)
      }
    }
  },
  beforeUnmount () {
    clearInterval(this.timer)
  },
}

</script>

<style>
</style>