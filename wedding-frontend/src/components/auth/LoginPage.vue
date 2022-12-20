<template>
  <div class="flex py-5 px-3">
    <div
      class="bg-pale dark:bg-darkPale p-5 rounded-2xl text-primary dark:text-darkPrimary mx-auto w-full max-w-xl shadow-lg"
    >
      <h1 class="text-lg font-bold dark:text-darkNeutral my-2">
        {{ $t("auth.loginpage.loginPage") }}
      </h1>
      <form class="flex flex-col" @submit="handleLogin()">
        <label
          class="block mx-auto my-1 dark:text-darkNeutral"
          for="email_input"
          >{{ $t("auth.loginpage.emailAddress") }}</label
        >
        <p
          v-if="error?.email"
          class="text-alert font-bold text-sm mx-auto pb-1"
        >
          {{ error.email[0] }}
        </p>
        <input
          id="email_input"
          v-model.trim="email"
          class="block bg-neutral dark:bg-darkNeutral rounded-md mx-auto px-2 w-full max-w-xs mb-1"
          type="email"
        />
        <button
          v-if="!loading"
          class="flex mx-auto my-2 px-2 py-1 rounded-lg bg-accent text-primary shadow-lg"
          type="submit"
          @click.prevent="handleLogin()"
        >
          {{ $t("auth.loginpage.submit") }}
        </button>
        <div v-if="loading" class="relative w-10 h-10 my-1 mx-auto">
          <loading-view>{{ $t("auth.loginpage.loading") }}</loading-view>
        </div>
        <p
          v-if="!!error?.non_field_errors"
          class="text-alert font-bold text-sm mx-auto py-2"
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
import { defineComponent } from "vue";
import { login } from "@/services/login.service";
import LoadingView from "@/components/shared/LoadingView.vue";
import type { AxiosError } from "axios";

export default defineComponent({
  name: "LoginPage",
  components: {
    LoadingView,
  },
  data() {
    return {
      loading: false as boolean,
      email: "" as string,
      error: null as any,
    };
  },
  methods: {
    handleLogin() {
      this.loading = true;
      login(this.email).catch((error: AxiosError) => {
        this.loading = false;
        this.error = error.response?.data ?? "Unable to return response";
      });
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
