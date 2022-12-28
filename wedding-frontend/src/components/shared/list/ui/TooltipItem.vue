<template>
  <span
    class="absolute w-48 -left-52 top-1/2 -translate-y-1/2 hidden group-hover:flex bg-pale dark:bg-darkPale px-2 py-1 rounded-md shadow-lg h-fit before:content-[''] before:absolute before:top-1/2 before:left-[100%] before:-translate-y-1/2 before:border-8 before:border-pale dark:before:border-darkPale dark:before:border-r-transparent before:border-r-transparent dark:before:border-y-transparent before:border-y-transparent select-none"
  >
    <slot></slot>
  </span>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "TooltipItem",
});
</script>
