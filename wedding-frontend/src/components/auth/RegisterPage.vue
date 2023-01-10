<template>
  <div class="flex py-5 px-3">
    <div
      class="bg-pale dark:bg-darkPale p-5 rounded-2xl text-primary dark:text-darkPrimary mx-auto w-full max-w-xl shadow-sm"
    >
      <h1 class="text-lg font-bold dark:text-darkNeutral py-2">
        {{ $t("auth.registerpage.registerPage") }}
      </h1>
      <p class="dark:text-darkNeutral pb-2">
        {{ $t("auth.registerpage.welcomeToThe") }}
      </p>
      <user-form
        @register="(user: User) => register(user)"
        :user="user"
        :loading="loading"
        :register-error="registerError"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import LoadingView from "@/components/shared/LoadingView.vue";
import { useAuthStore } from "@/stores";
import { mapState, mapActions } from "pinia";
import type { User } from "@/models/auth.interface";
import UserForm from "../shared/UserForm.vue";

export default defineComponent({
  name: "RegisterPage",
  components: {
    LoadingView,
    UserForm,
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
