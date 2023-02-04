<template>
  <div
    class="text-3xl md:text-5xl text-center flex w-full items-center justify-center dark:text-darkPale"
  >
    <div class="text-2xl mr-1 font-extralight">
      {{ $t("shared.countdown.in") }}
    </div>
    <div class="mx-1 p-2 rounded-lg">
      <div class="p-1 leading-none" :x-text="$t('shared.countdown.days')">
        {{ days }}
      </div>
      <div class="uppercase text-sm md:text-base leading-none">
        {{ $t("shared.countdown.days") }}
      </div>
    </div>
    <div class="mx-1 p-2 rounded-lg">
      <div class="p-1 leading-none" :x-text="$t('shared.countdown.hours')">
        {{ hour }}
      </div>
      <div class="uppercase text-sm md:text-base leading-none">
        {{ $t("shared.countdown.hours") }}
      </div>
    </div>
    <div class="mx-1 p-2 rounded-lg">
      <div class="p-1 leading-none" :x-text="$t('shared.countdown.minutes')">
        {{ min }}
      </div>
      <div class="uppercase text-sm md:text-base leading-none">
        {{ $t("shared.countdown.minutes") }}
      </div>
    </div>
    <div class="mx-1 p-2 rounded-lg">
      <div class="p-1 leading-none" :x-text="$t('shared.countdown.seconds')">
        {{ sec }}
      </div>
      <div class="uppercase text-sm md:text-base leading-none">
        {{ $t("shared.countdown.seconds") }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { type Ref, watch, ref, computed, onBeforeUnmount } from "vue";

const props = defineProps({
  endDate: {
    // pass date object till when you want to run the timer
    type: Date,
    default() {
      return new Date();
    },
  },
  negative: {
    // optional, should countdown after 0 to negative
    type: Boolean,
    default: false,
  },
});

const now = ref(new Date());
const timer: Ref<undefined | NodeJS.Timer> = ref(undefined);

const days = computed(() => {
  let d = Math.trunc(
    (props.endDate.valueOf() - now.value.valueOf()) / 1000 / 3600 / 24
  );
  return d > 9 ? d : "0" + d;
});

const hour = computed(() => {
  let h =
    Math.trunc((props.endDate.valueOf() - now.value.valueOf()) / 1000 / 3600) %
    24;
  return h > 9 ? h : "0" + h;
});

const min = computed(() => {
  let m =
    Math.trunc((props.endDate.valueOf() - now.value.valueOf()) / 1000 / 60) %
    60;
  return m > 9 ? m : "0" + m;
});

const sec = computed(() => {
  let s =
    Math.trunc((props.endDate.valueOf() - now.value.valueOf()) / 1000) % 60;
  return s > 9 ? s : "0" + s;
});

watch(
  () => props.endDate,
  async (newVal) => {
    if (timer.value) {
      clearInterval(timer.value);
    }
    timer.value = setInterval(() => {
      now.value = new Date();
      if (props.negative) return;
      if (now.value > newVal) {
        now.value = newVal;
        clearInterval(timer.value);
      }
    }, 1000);
  },
  { immediate: true }
);
onBeforeUnmount(() => {
  clearInterval(timer.value);
});
</script>

<style></style>
