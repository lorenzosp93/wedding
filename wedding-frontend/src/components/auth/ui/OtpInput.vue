<template>
  <div ref="otpCont" class="flex flex-row mx-auto w-fit">
    <input
      v-for="idx in Array(token.length).keys()"
      :key="idx"
      :value="token[idx]"
      type="text"
      class="block bg-neutral dark:bg-darkNeutral rounded-md px-1 w-8 mx-1 text-center focus:ring-accent border-none shadow-inner placeholder:text-secondary text-2xl"
      :autofocus="idx === 0"
      pattern="\d{1}"
      maxlength="1"
      :placeholder="(idx + 1).toString()"
      onfocus="this.select();"
      @input.prevent="handleInput($event as InputEvent, idx)"
      @paste.prevent="handlePaste"
    />
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps({
  token: { type: Array<string>, default: ["", "", "", "", "", ""] },
});

function handlePaste(event: ClipboardEvent) {
  const pasteData = event.clipboardData?.getData("text/plain") ?? "";
  let nextEl = (event.target as HTMLInputElement).nextElementSibling;
  for (let i = 0; i < props.token.length; i++) {
    props.token[i] = pasteData[i];
    if (nextEl) {
      nextEl = nextEl.nextElementSibling;
    } else {
      (event.target as HTMLInputElement).form?.requestSubmit();
    }
  }
}

function handleInput(event: InputEvent, idx: number) {
  let target = event.target as HTMLInputElement;
  let data = event.data ?? target?.value ?? "";
  props.token[idx] = data;
  if (data && target.nextElementSibling) {
    (target.nextElementSibling as HTMLInputElement).focus();
  } else if (!data && target.previousElementSibling) {
    (target.previousElementSibling as HTMLInputElement).focus();
  }
}
</script>
