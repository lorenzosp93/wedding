<!-- eslint-disable vue/no-v-html -->
<template>
  <div class="py-5 px-3 flex">
    <div
      class="bg-pale dark:bg-darkPale p-5 rounded-2xl mx-auto max-w-xl w-full shadow-lg dark:text-darkNeutral"
    >
      <p v-html="$t('auth.loginsuccess.loginWasSuccessful')"></p>
      <p class="py-2" v-html="$t('auth.loginsuccess.ifYouGetYourEmail')"></p>
      <form class="w-fit mx-auto flex flex-col" @submit="getToken">
        <label for="otp" class="block mx-auto my-1 dark:text-darkNeutral">{{
          $t("auth.loginsuccess.otp")
        }}</label>
        <p
          v-if="error?.token"
          class="text-alert dark:text-darkAlert font-bold text-sm mx-auto pb-1"
        >
          {{ error.token[0] }}
        </p>
        <input
          v-model="token"
          type="text"
          inputmode="numeric"
          maxlength="6"
          pattern="[0-9]{6}"
          class="block bg-neutral dark:bg-darkNeutral dark:text-darkPrimary rounded-md mx-auto px-2 w-full max-w-xs mb-1 text-center"
        />
        <button
          v-if="!loading"
          class="flex mx-auto my-2 px-2 py-1 rounded-lg bg-accent text-primary shadow-lg"
          type="submit"
          @click.prevent="getToken"
        >
          {{ $t("auth.loginpage.submit") }}
        </button>
        <div v-if="loading" class="relative w-10 h-10 my-1 mx-auto">
          <loading-view>{{ $t("auth.loginpage.loading") }}</loading-view>
        </div>
        <p
          v-if="!!error?.non_field_errors"
          class="text-alert dark:text-darkAlert font-bold text-sm mx-auto py-2"
        >
          {{
            $t("auth.loginpage.thereWasAn", { a: error.non_field_errors[0] })
          }}
        </p>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import { get_token } from "@/services/login.service.js";
import type { AxiosError } from "axios";
import { defineComponent } from "vue";

export default defineComponent({
  name: "LoginSuccess",
  components: {
    LoadingView,
  },
  data() {
    return {
      email: "" as string,
      token: "" as string,
      loading: false as boolean,
      error: null as any,
    };
  },
  mounted() {
    this.email = this.$route.query.email as string;
  },
  methods: {
    getToken() {
      this.loading = true;
      get_token(this.email, this.token)
        .then()
        .catch((error: AxiosError) => {
          this.loading = false;
          this.error = error.response?.data ?? "Unable to log you in";
        });
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
