<template>
  <div
    class="z-20 absolute left-0 top-0 backdrop-blur-sm h-screen w-screen cursor-pointer"
    data-test="outside"
  ></div>
  <OnClickOutside
    @trigger="$emit('toggle')"
    class="z-30 absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 rounded-lg bg-pale dark:bg-darkPale p-3 w-full max-w-sm shadow-lg"
  >
    <p class="text-left p-1 mb-2">{{ $t("profile.plusone.pleaseEnterThe") }}</p>
    <form class="flex flex-wrap" @submit="callSetupPlusOne">
      <div class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" for="first_name">{{
          $t("profile.plusone.first_name")
        }}</label>
        <input
          id="first_name"
          v-model.trim="plusOne.first_name"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral"
          type="text"
        />
        <p
          v-if="registerError?.first_name"
          class="text-alert dark:text-darkAlert mx-3"
        >
          {{ registerError.first_name[0] }}
        </p>
      </div>
      <div class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" for="last_name">{{
          $t("profile.plusone.last_name")
        }}</label>
        <input
          id="last_name"
          v-model.trim="plusOne.last_name"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral"
          type="text"
        />
        <p
          v-if="registerError?.last_name"
          class="text-alert dark:text-darkAlert mx-3"
        >
          {{ registerError.last_name[0] }}
        </p>
      </div>
      <div class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" for="email">{{
          $t("profile.plusone.email")
        }}</label>
        <input
          id="email"
          v-model.trim="plusOne.email"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral"
          type="email"
        />
        <p
          v-if="registerError?.email"
          class="text-alert dark:text-darkAlert mx-3"
        >
          {{ registerError.email[0] }}
        </p>
      </div>
      <p
        v-if="registerError?.non_field_errors"
        class="text-alert dark:text-darkAlert mx-auto"
      >
        {{ registerError.non_field_errors }}
      </p>
      <div class="relative w-full h-16">
        <button
          v-show="!loading && !success"
          class="flex mx-auto px-2 py-1 bg-accent rounded-md my-5"
          @click.prevent="callSetupPlusOne"
        >
          {{ $t("profile.plusone.submit") }}
        </button>
        <loading-view v-if="loading"></loading-view>
        <p v-if="success">{{ $t("profile.plusone.success") }}</p>
      </div>
    </form>
  </OnClickOutside>
</template>

<script lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import { useAuthStore } from "@/stores";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import type { User } from "@/models/auth.interface";
import { OnClickOutside } from "@vueuse/components";

export default defineComponent({
  name: "PlusOne",
  components: {
    LoadingView,
    OnClickOutside,
  },
  emits: ["toggle"],
  data() {
    return {
      plusOne: {
        first_name: "",
        last_name: "",
        email: "",
      } as User,
    };
  },
  computed: {
    ...mapState(useAuthStore, ["registerError", "loading", "success"]),
  },
  mounted() {},
  methods: {
    ...mapActions(useAuthStore, ["getProfile", "setupPlusOne"]),
    callSetupPlusOne() {
      this.setupPlusOne(this.plusOne).then(() => {
        this.$emit("toggle");
      });
    },
  },
});
</script>
