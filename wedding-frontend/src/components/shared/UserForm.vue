<template>
  <form v-if="user" class="flex flex-col mt-3" @submit.prevent="register(user)">
    <div class="grid grid-cols-6 gap-5 mx-3 mb-3">
      <div class="col-span-6 sm:col-span-3">
        <div class="flex flex-wrap">
          <label
            class="block dark:text-darkNeutral pb-0.5 my-auto"
            for="last_name_input"
            >{{ $t("auth.registerpage.firstName") }}</label
          >
          <p
            v-if="registerError?.first_name?.length"
            class="text-alert dark:text-darkAlert ml-auto my-auto"
          >
            {{ registerError.first_name[0] }}
          </p>
        </div>
        <input
          id="first_name_input"
          v-model.trim="user.first_name"
          class="block bg-neutral dark:bg-darkNeutral rounded-md px-2 w-full mb-1 border-none shadow-inner focus:ring-accent"
          type="text"
          required
          autofocus
        />
      </div>
      <div class="col-span-6 sm:col-span-3">
        <div class="flex flex-wrap">
          <label
            class="block dark:text-darkNeutral pb-0.5 my-auto"
            for="last_name_input"
            >{{ $t("auth.registerpage.lastName") }}</label
          >
          <p
            v-if="registerError?.last_name?.length"
            class="text-alert dark:text-darkAlert ml-auto my-auto"
          >
            {{ registerError.last_name[0] }}
          </p>
        </div>
        <input
          id="last_name_input"
          v-model.trim="user.last_name"
          class="block bg-neutral dark:bg-darkNeutral rounded-md px-2 w-full mb-1 border-none shadow-inner focus:ring-accent"
          type="text"
          required
        />
      </div>
      <div class="col-span-6">
        <div class="flex flex-wrap">
          <label
            class="block dark:text-darkNeutral pb-0.5 my-auto"
            for="email_input"
            >{{ $t("auth.registerpage.email") }}</label
          >
          <p
            v-if="registerError?.email?.length"
            class="text-alert dark:text-darkAlert ml-auto my-auto"
          >
            {{ registerError.email[0] }}
          </p>
        </div>
        <input
          id="email_input"
          v-model.trim="user.email"
          class="block bg-neutral dark:bg-darkNeutral rounded-md px-2 w-full mb-1 border-none shadow-inner focus:ring-accent"
          type="email"
          required
        />
      </div>
    </div>
    <button
      v-if="!loading"
      class="flex ml-auto mr-3 my-2 px-2 py-1 rounded-lg bg-accent text-primary shadow-md"
      type="submit"
      @click.prevent="register(user)"
    >
      {{ $t("auth.loginpage.submit") }}
    </button>
    <div v-if="loading" class="relative w-10 h-10 my-1 mx-auto">
      <loading-view>{{ $t("auth.loginpage.loading") }}</loading-view>
    </div>
    <p
      v-if="registerError?.non_field_errors?.length"
      class="text-alert dark:text-darkAlert mx-auto py-2 text-center"
    >
      {{
        $t("auth.loginpage.thereWasAn", {
          a: registerError.non_field_errors[0],
        })
      }}
    </p>
  </form>
</template>

<script lang="ts">
import type { User, UserError } from "@/models/auth.interface";
import LoadingView from "./LoadingView.vue";
import { defineComponent, type PropType } from "vue";

export default defineComponent({
  name: "UserForm",
  components: {
    LoadingView,
  },
  props: {
    user: { type: Object as PropType<User> },
    registerError: { type: Object as PropType<UserError> },
    loading: { type: Boolean, default: false },
  },
  emits: ["register"],
  methods: {
    register(user: User | undefined) {
      if (user) {
        this.$emit("register", user);
      }
    },
  },
});
</script>
