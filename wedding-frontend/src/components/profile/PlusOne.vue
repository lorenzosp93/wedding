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
    <user-form
      @register="(user: User) => callSetupPlusOne(user)"
      :user="plusOne"
      :loading="loading"
      :register-error="registerError"
    />
  </OnClickOutside>
</template>

<script lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import { useAuthStore } from "@/stores";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";
import type { User } from "@/models/auth.interface";
import { OnClickOutside } from "@vueuse/components";
import UserForm from "../shared/UserForm.vue";

export default defineComponent({
  name: "PlusOne",
  components: {
    LoadingView,
    OnClickOutside,
    UserForm,
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
    callSetupPlusOne(user: User) {
      this.setupPlusOne(user)
        .then(() => {
          this.$emit("toggle");
        })
        .catch();
    },
  },
});
</script>
