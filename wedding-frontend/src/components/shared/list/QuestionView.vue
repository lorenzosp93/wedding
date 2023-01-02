// @ts-ignore
<template>
  <section id="object-questions">
    <form
      v-if="responses && responses?.length"
      @submit="$emit('submitResponse', responses)"
    >
      <div
        v-for="(question, idx) in activeObject?.questions"
        :key="question.uuid"
      >
        <h1 class="text-lg">{{ idx + 1 }}. {{ question.subject }}</h1>
        <p v-html="question.content" class="text-sm pl-5"></p>
        <ul
          v-if="question.options?.length"
          :multiple="question.multi_select"
          class="w-full my-2 bg-pale dark:bg-darkPale rounded-md shadow-inner border-none"
        >
          <li
            v-for="option in question.options"
            :key="option.uuid"
            class="select-none"
          >
            <input
              :id="option.uuid"
              v-model="getInputResponse(question).option"
              :value="option.uuid"
              :name="question.uuid"
              :type="question.multi_select ? 'checkbox' : 'radio'"
              class="my-2 bg-neutral dark:bg-darkNeutral text-accent border-none focus:ring-accent"
              :disabled="
                question.response
                  ? question.multi_select
                    ? true
                    : question?.response?.option != option.uuid
                  : false
              "
              :required="question.mandatory"
            />
            <label :for="option.uuid" class="ml-3">{{ option.content }}</label>
          </li>
        </ul>
        <p
          v-if="submitError?.find((e: ResponseErrors) => e.q == question.uuid && e.e?.option?.length)"
          class="text-alert dark:text-darkAlert"
        >
          {{ submitError.find((e) => e.q == question.uuid)?.e.option[0] }}
        </p>
        <div v-if="question.free_text" class="mb-5">
          <label v-if="question.options?.length" for="input" class="my-1">{{
            $t("shared.listview.other")
          }}</label>
          <input
            v-model="getInputResponse(question).text"
            type="text"
            class="w-full rounded-md bg-pale dark:bg-darkPale px-2 py-1 border-none shadow-inner focus:ring-accent"
            :readonly="question.response"
            :required="question.mandatory && question.options.length == 0"
          />
          <p
            v-if="submitError?.find((e: ResponseErrors) => e.q == question.uuid && e.e?.text?.length)"
            class="text-alert dark:text-darkAlert mx-3"
          >
            {{ submitError.find((e) => e.q == question.uuid)?.e.text[0] }}
          </p>
        </div>
        <p
          v-if="
            question.uuid ==
            submitError?.find(
              (e) => e.q == question.uuid && e.e?.non_field_errors?.length
            )
          "
        >
          {{ submitError?.find((e) => e.q == question)?.e.non_field_errors[0] }}
        </p>
      </div>
      <div
        v-if="activeObject?.questions?.every((q: Question) => q.response)"
        class="flex flex-wrap"
      >
        <p class="py-1 font-bold text-accent my-auto">
          {{ $t("shared.listview.alreadyAnswered") }}
        </p>
        <div class="ml-auto my-auto relative w-48 min-h-[2.5rem] p-2">
          <button
            v-show="!deleteLoading"
            class="bg-pale dark:bg-darkPale text-primary rounded-md px-2 py-1 my-auto"
            @click.prevent="$emit('deleteResponses')"
          >
            {{ $t("shared.listview.changeResponses") }}
          </button>
          <loading-view v-if="deleteLoading"></loading-view>
        </div>
      </div>
      <div
        v-if="activeObject?.questions.some((q: Question) => !q.response)"
        class="relative h-20 w-full pt-5 mx-auto"
      >
        <button
          v-show="!submitLoading"
          class="bg-accent text-primary rounded-md px-2 py-1 flex mx-auto"
          @click.prevent="$emit('submitResponse', responses)"
        >
          {{ $t("shared.listview.submit") }}
        </button>
        <loading-view v-if="submitLoading"></loading-view>
        <p v-if="submitSuccess">{{ $t("shared.listview.success") }}</p>
      </div>
    </form>
  </section>
</template>

<script lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import { defineComponent, type PropType } from "vue";
import type {
  Question,
  Response,
  ResponseErrors,
} from "@/models/listObjects.interface";

export default defineComponent({
  components: {
    LoadingView,
  },
  props: {
    activeObject: { type: Object },
    responses: { type: Array<Response> },
    submitLoading: { type: Boolean },
    submitError: { type: Array<ResponseErrors> },
    submitSuccess: { type: Boolean },
    deleteLoading: { type: Boolean },
    deleteError: { type: Array<ResponseErrors> },
    deleteSuccess: { type: Boolean },
  },
  emits: ["deleteResponses", "submitResponse"],
  methods: {
    getInputResponse(question: Question): Response {
      return (
        this.responses?.find((r: Response) => r.question == question.uuid) ?? {
          option: [],
          text: "",
          question: question.uuid,
        }
      );
    },
  },
});
</script>

<style scoped></style>
