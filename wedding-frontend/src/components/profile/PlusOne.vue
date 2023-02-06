<template>
  <div
    class="z-20 absolute left-0 top-0 backdrop-blur-sm h-screen w-screen cursor-pointer"
    data-test="outside"
  ></div>
  <OnClickOutside
    @trigger="$emit('toggle')"
    class="z-30 absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 rounded-lg bg-pale dark:bg-darkPale p-3 w-full max-w-sm shadow-sm"
  >
    <p class="text-left p-1 mb-2">{{ $t("profile.plusone.pleaseEnterThe") }}</p>
    <UserForm
      @register="(user: User) => callSetupPlusOne(user)"
      :user="plusOne"
      :loading="authStore.loading"
      :register-error="authStore.registerError"
    />
  </OnClickOutside>
</template>

<script setup lang="ts">
import { useAuthStore } from "@/stores";
import { type Ref, ref } from "vue";
import type { User } from "@/models/auth.interface";
import { OnClickOutside } from "@vueuse/components";
import UserForm from "../shared/UserForm.vue";

const emit = defineEmits(["toggle"]);

const plusOne: Ref<User> = ref({
  first_name: "",
  last_name: "",
  email: "",
});

const authStore = useAuthStore();
function callSetupPlusOne(user: User) {
  authStore
    .setupPlusOne(user)
    .then(() => {
      emit("toggle");
    })
    .catch();
}
</script>
