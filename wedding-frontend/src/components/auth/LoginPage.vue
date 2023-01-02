<template>
  <div class="flex py-5 px-3">
    <div
      class="bg-pale dark:bg-darkPale p-5 rounded-2xl text-primary dark:text-darkPrimary mx-auto w-full max-w-xl shadow-lg"
    >
      <h1 class="text-lg font-bold dark:text-darkNeutral py-2">
        {{ $t("auth.loginpage.loginPage") }}
      </h1>
      <p class="dark:text-darkNeutral pb-2">
        {{ $t("auth.loginpage.pleaseEnterYour") }}
      </p>
      <form class="flex flex-col mt-3" @submit="handleLogin()">
        <div class="max-w-sm mx-auto w-full">
          <div class="flex flex-wrap">
            <label
              class="block dark:text-darkNeutral pb-0.5 my-auto"
              for="email_input"
              >{{ $t("auth.loginpage.emailAddress") }}</label
            >
            <p
              v-if="error?.email"
              class="text-alert dark:text-darkAlert ml-auto my-auto"
            >
              {{ error.email[0] }}
            </p>
          </div>
          <input
            id="email_input"
            v-model.trim="email"
            class="block bg-neutral dark:bg-darkNeutral rounded-md px-2 w-full mb-1 focus:ring-accent border-none shadow-inner"
            type="email"
            data-test="email-input"
          />
        </div>
        <button
          v-if="!loading"
          class="flex mx-auto my-3 px-2 py-1 rounded-lg bg-accent text-primary shadow-lg"
          type="submit"
          data-test="form-button"
          @click.prevent="handleLogin()"
        >
          {{ $t("auth.loginpage.submit") }}
        </button>
        <div v-if="loading" class="relative w-10 h-10 my-1 mx-auto">
          <loading-view>{{ $t("auth.loginpage.loading") }}</loading-view>
        </div>
        <p
          v-if="!!error?.non_field_errors"
          class="text-alert dark:text-darkAlert mx-auto py-2 text-center"
        >
          {{
            $t("auth.loginpage.thereWasAn", { a: error.non_field_errors[0] })
          }}
        </p>
        <p v-if="message" class="font-bold text-sm mx-auto py-2">
          {{ message }}
        </p>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { login } from "@/services/login.service";
import LoadingView from "@/components/shared/LoadingView.vue";
import type { AxiosError } from "axios";
import type { UserError } from "@/models/auth.interface";

export default defineComponent({
  name: "LoginPage",
  components: {
    LoadingView,
  },
  data() {
    return {
      loading: false as boolean,
      email: "" as string,
      error: undefined as UserError | undefined,
      message: "" as string,
    };
  },
  methods: {
    handleLogin() {
      this.loading = true;
      login(this.email).catch((error: AxiosError<UserError>) => {
        this.loading = false;
        this.error = error.response?.data ?? undefined;
      });
    },
  },
  mounted() {
    this.email = (this.$route.query?.email as string) ?? "";
    this.message = (this.$route.query?.message as string) ?? "";
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
