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
      <UserForm
        @register="(user: User) => authStore.register(user)"
        :user="user"
        :loading="authStore.loading"
        :register-error="authStore.registerError"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { type Ref, ref, onMounted } from "vue";
import { useAuthStore } from "@/stores";
import type { User } from "@/models/auth.interface";
import UserForm from "../shared/UserForm.vue";
import { useRoute } from "vue-router";

const user: Ref<User> = ref({
  email: "",
  first_name: "",
  last_name: "",
});

const route = useRoute();

onMounted(() => {
  user.value.email = route.query.email as string;
});

const authStore = useAuthStore();
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
