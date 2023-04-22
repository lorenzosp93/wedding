<!-- eslint-disable vue/no-v-html -->
<template>
  <div class="py-5 px-3 flex">
    <div
      class="bg-pale dark:bg-darkPale p-5 rounded-2xl mx-auto max-w-xl w-full shadow-sm"
    >
      <p
        class="dark:text-darkNeutral"
        v-html="$t('auth.loginsuccess.loginWasSuccessful')"
      ></p>
      <p
        class="py-2 dark:text-darkNeutral"
        v-html="$t('auth.loginsuccess.ifYouGetYourEmail')"
      ></p>
      <form
        class="w-fit mx-auto flex flex-col mt-3"
        @submit.prevent="getAuthToken"
      >
        <label for="otp" class="block mx-auto my-1 dark:text-darkNeutral">{{
          $t("auth.loginsuccess.otp")
        }}</label>
        <OtpInput v-model:token="token" />
        <p
          v-if="error?.token"
          class="text-alert dark:text-darkAlert font-bold text-sm mx-auto pt-1"
        >
          {{ error.token[0] }}
        </p>
        <button
          v-if="!loading"
          class="flex mx-auto mt-3 px-2 py-1 rounded-lg bg-accent text-primary shadow-md"
          type="submit"
          data-test="form-button"
          @click.prevent="getAuthToken"
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

<script setup lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import { getToken } from "@/services/login.service.js";
import type { AxiosError } from "axios";
import { type Ref, ref, onMounted } from "vue";
import OtpInput from "./ui/OtpInput.vue";
import { useRoute } from "vue-router";

const email: Ref<string> = ref("");
const token: Ref<string[]> = ref(["", "", "", "", "", ""]);
const loading: Ref<boolean> = ref(false);
const error: Ref<any> = ref(null);

const route = useRoute();

onMounted(() => {
  email.value = route?.query.email as string;
});

function getAuthToken() {
  loading.value = true;
  getToken(email.value, token.value.join(""))
    .then()
    .catch((e: AxiosError) => {
      loading.value = false;
      error.value = e.response?.data ?? "Unable to log you in";
    });
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
