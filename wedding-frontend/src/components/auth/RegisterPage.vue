<template>
  <div class="flex py-5 px-3">
    <div
      class="bg-pale dark:bg-darkPale p-5 rounded-2xl text-primary dark:text-darkPrimary mx-auto w-full max-w-xl shadow-lg"
    >
      <h1 class="text-lg font-bold dark:text-darkNeutral my-2">
        {{ $t("auth.registerpage.registerPage") }}
      </h1>
      <p class="dark:text-darkNeutral mb-2">
        {{ $t("auth.registerpage.welcomeToThe") }}
      </p>
      <form class="flex flex-col" @submit="register(user)">
        <label
          class="block mx-auto my-1 dark:text-darkNeutral"
          for="email_input"
          >{{ $t("auth.registerpage.firstName") }}</label
        >
        <p
          v-if="registerError?.first_name?.length"
          class="text-alert font-bold text-sm mx-auto pb-1"
        >
          {{ registerError.first_name[0] }}
        </p>
        <input
          id="email_input"
          v-model.trim="user.first_name"
          class="block bg-neutral dark:bg-darkNeutral rounded-md mx-auto px-2 w-full max-w-xs mb-1"
          type="email"
        />
        <label
          class="block mx-auto my-1 dark:text-darkNeutral"
          for="email_input"
          >{{ $t("auth.registerpage.lastName") }}</label
        >
        <p
          v-if="registerError?.last_name?.length"
          class="text-alert font-bold text-sm mx-auto pb-1"
        >
          {{ registerError.last_name[0] }}
        </p>
        <input
          id="email_input"
          v-model.trim="user.last_name"
          class="block bg-neutral dark:bg-darkNeutral rounded-md mx-auto px-2 w-full max-w-xs mb-1"
          type="email"
        />
        <label
          class="block mx-auto my-1 dark:text-darkNeutral"
          for="email_input"
          >{{ $t("auth.registerpage.email") }}</label
        >
        <p
          v-if="registerError?.email?.length"
          class="text-alert font-bold text-sm mx-auto pb-1"
        >
          {{ registerError.email[0] }}
        </p>
        <input
          id="email_input"
          v-model.trim="user.email"
          class="block bg-neutral dark:bg-darkNeutral rounded-md mx-auto px-2 w-full max-w-xs mb-1"
          type="email"
        />
        <button
          v-if="!loading"
          class="flex mx-auto my-2 px-2 py-1 rounded-lg bg-accent text-primary shadow-lg"
          type="submit"
          @click.prevent="register(user)"
        >
          {{ $t("auth.loginpage.submit") }}
        </button>
        <div v-if="loading" class="relative w-10 h-10 my-1 mx-auto">
          <loading-view>{{ $t("auth.loginpage.loading") }}</loading-view>
        </div>
        <p
          v-if="!!registerError?.non_field_errors"
          class="text-alert font-bold text-sm mx-auto py-2"
        >
          {{
            $t("auth.loginpage.thereWasAn", {
              a: registerError.non_field_errors[0],
            })
          }}
        </p>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import LoadingView from "@/components/shared/LoadingView.vue";
import { useAuthStore } from "@/stores";
import { mapState, mapActions } from "pinia";
import type { User } from "@/models/auth.interface";

export default defineComponent({
  name: "RegisterPage",
  components: {
    LoadingView,
  },
  data() {
    return {
      user: {
        email: "",
        first_name: "",
        last_name: "",
      } as User,
    };
  },
  computed: {
    ...mapState(useAuthStore, ["loading", "registerError"]),
  },
  methods: {
    ...mapActions(useAuthStore, ["register"]),
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
