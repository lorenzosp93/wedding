<template>
  <div
    class="z-20 absolute left-0 top-0 backdrop-blur-sm h-screen w-screen"
    @click="$emit('toggle')"
  ></div>
  <div
    class="z-30 absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 rounded-lg bg-pale dark:bg-darkPale ring-1 ring-accent p-3 w-full max-w-sm"
  >
    <form class="flex flex-wrap" @submit="setupPlusOne">
      <div class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" for="first_name">{{
          $t("profile.plusone.first_name")
        }}</label>
        <input
          id="first_name"
          v-model.trim="submit.first_name"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral"
          type="text"
        />
        <p v-if="error?.first_name" class="text-alert mx-3">
          {{ error.first_name[0] }}
        </p>
      </div>
      <div class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" for="last_name">{{
          $t("profile.plusone.last_name")
        }}</label>
        <input
          id="last_name"
          v-model.trim="submit.first_name"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral"
          type="text"
        />
        <p v-if="error?.last_name" class="text-alert mx-3">
          {{ error.last_name[0] }}
        </p>
      </div>
      <div class="my-1 px-5 mx-auto w-full text-start">
        <label class="w-full" for="email">{{
          $t("profile.plusone.email")
        }}</label>
        <input
          id="email"
          v-model.trim="submit.email"
          class="w-full rounded-md bg-neutral dark:bg-darkNeutral"
          type="email"
        />
        <p v-if="error?.email" class="text-alert mx-3">{{ error.email[0] }}</p>
      </div>
      <p v-if="error?.non_field_errors" class="text-alert mx-auto">
        {{ error.non_field_errors }}
      </p>
      <div class="relative w-full h-16">
        <button
          v-show="!loading && !success"
          class="flex mx-auto px-2 py-1 bg-accent rounded-md my-5"
          @click.prevent="setupPlusOne"
        >
          {{ $t("profile.plusone.submit") }}
        </button>
        <loading-view v-if="loading"></loading-view>
        <p v-if="success">{{ $t("profile.plusone.success") }}</p>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import ApiService from "../../services/api.service";
import LoadingView from "@/components/shared/LoadingView.vue";
import { defineComponent } from "vue";
import type { User } from "@/models/auth.interface";
import type { AxiosError } from "axios";

export default defineComponent({
  name: "PlusOne",
  components: { LoadingView },
  emits: ["toggle"],
  data() {
    return {
      submit: {
        first_name: "",
        last_name: "",
        email: "",
      } as User,
      error: null as any,
      loading: false,
      success: false,
    };
  },
  computed: {},
  mounted() {},
  methods: {
    setupPlusOne() {
      this.loading = true;
      console.log(this.submit);
      ApiService.setupPlusOne(
        this.submit.email,
        this.submit.first_name,
        this.submit.last_name
      ).then(
        (response) => {
          if (response.status == 200) {
            this.error = null;
            this.loading = false;
            this.success = true;
            setTimeout(() => this.$emit("toggle"), 2000);
          }
        },
        (error: AxiosError) => {
          this.loading = false;
          this.error = error?.response?.data ?? "There was an unexpected error";
        }
      );
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
