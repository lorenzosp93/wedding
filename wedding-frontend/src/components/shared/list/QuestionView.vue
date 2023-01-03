// @ts-ignore
<template>
  <section id="object-questions">
    <form
      v-if="responses && responses?.length"
      @submit="$emit('submitResponse', responses)"
    >
      <div v-for="(question, idx) in questions" :key="question.uuid">
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
              :value="option.uuid"
              @input="
                (event) => {
                  handleInput(question, event);
                }
              "
              :checked="!!question.response?.option.includes(option.uuid)"
              :name="question.uuid"
              :type="question.multi_select ? 'checkbox' : 'radio'"
              class="my-2 bg-neutral dark:bg-darkNeutral text-accent border-none focus:ring-accent disabled:text-primary"
              :disabled="question.response ? true : false"
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
            v-model="getResponse(question).text"
            type="text"
            class="w-full rounded-md bg-pale dark:bg-darkPale px-2 py-1 border-none shadow-inner focus:ring-accent"
            :readonly="!!question.response"
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
            )?.q
          "
        >
          {{
            submitError?.find((e) => e.q == question.uuid)?.e
              .non_field_errors[0]
          }}
        </p>
      </div>
      <div
        v-if="questions?.every((q: Question) => q.response)"
        class="flex flex-wrap"
      >
        <p class="py-1 font-bold my-auto">
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
        v-if="questions.some((q: Question) => !q.response)"
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
  data() {
    return {
      responses: [] as Response[],
    };
  },
  components: {
    LoadingView,
  },
  props: {
    questions: { type: Array<Question>, default: [] },
    submitLoading: { type: Boolean },
    submitError: { type: Array<ResponseErrors> },
    submitSuccess: { type: Boolean },
    deleteLoading: { type: Boolean },
    deleteError: { type: Array<ResponseErrors> },
    deleteSuccess: { type: Boolean },
  },
  watch: {
    questions(newVal: Question[], oldVal: Question[]) {
      if (newVal != oldVal) {
        this.responseSetup();
      }
    },
  },
  emits: ["deleteResponses", "submitResponse"],
  mounted() {
    this.responseSetup();
  },
  methods: {
    responseSetup() {
      this.responses = [];
      if (this.questions.length) {
        this.questions.forEach((question: Question) => {
          this.responses = [
            ...this.responses,
            {
              question: question.uuid,
              option: question?.response?.option ?? [],
              text: question?.response?.text ?? "",
            },
          ];
        });
      }
    },
    handleInput(question: Question, event: Event) {
      let value = (event?.target as HTMLInputElement).value;
      let response = this.getResponse(question);
      if (response) {
        if (question.multi_select) {
          this.multiSelectInputHandler(value, response);
        } else {
          this.singleSelectInputHandler(value, response);
        }
      }
    },
    multiSelectInputHandler(value: string, response: Response) {
      if (response.option.includes(value)) {
        response.option = response.option.filter((o: string) => o != value);
      } else {
        response.option = [...response.option, value];
      }
    },
    singleSelectInputHandler(value: string, response: Response) {
      response.option = [value];
    },
    getResponse(question: Question): Response {
      return (
        this.responses.find((r: Response) => r.question == question.uuid) ?? {
          option: [],
          text: "",
        }
      );
    },
  },
});
</script>

<style scoped></style>
