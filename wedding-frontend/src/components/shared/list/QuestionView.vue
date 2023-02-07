// @ts-ignore
<template>
  <section id="object-questions">
    <form
      v-if="responses && responses?.length"
      @submit.prevent="emit('submitResponse', responses)"
    >
      <div
        v-for="(question, idx) in questions"
        :key="question.uuid"
        class="my-3"
      >
        <hr class="my-1" />
        <h1 class="text-lg">{{ idx + 1 }}. {{ question.subject }}</h1>
        <p v-html="question.content" class="text-sm pl-5 py-1"></p>
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
        <div v-if="question.free_text" class="">
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
        v-if="questions?.every((q: IQuestion) => q.response)"
        class="flex flex-wrap"
      >
        <p class="py-1 font-bold my-auto">
          {{ $t("shared.listview.alreadyAnswered") }}
        </p>
        <div class="ml-auto py-3 relative w-56 min-h-[2.5rem]">
          <button
            v-show="!deleteLoading"
            class="bg-pale dark:bg-darkPale text-primary rounded-md px-2 py-1 my-auto flex ml-auto"
            @click.prevent="emit('deleteResponses')"
          >
            <pencil-square-icon
              class="w-5 h-5 mr-1 my-auto"
            ></pencil-square-icon>
            {{ $t("shared.listview.changeResponses") }}
          </button>
          <loading-view v-if="deleteLoading"></loading-view>
        </div>
      </div>
      <div
        v-if="questions.some((q: IQuestion) => !q.response)"
        class="relative h-20 w-full pt-5 mx-auto"
      >
        <button
          v-show="!submitLoading"
          class="bg-accent text-primary rounded-md px-2 py-1 flex mx-auto"
          @click.prevent="emit('submitResponse', responses)"
        >
          <paper-airplane-icon
            class="w-5 h-5 mr-1 my-auto"
          ></paper-airplane-icon>
          {{ $t("shared.listview.submit") }}
        </button>
        <loading-view v-if="submitLoading"></loading-view>
        <p v-if="submitSuccess">{{ $t("shared.listview.success") }}</p>
      </div>
    </form>
  </section>
</template>

<script setup lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import { type Ref, ref, watch, onMounted } from "vue";
import type {
  IQuestion,
  Response,
  ResponseErrors,
} from "@/models/listObjects.interface";
import { PencilSquareIcon, PaperAirplaneIcon } from "@heroicons/vue/24/outline";

const responses: Ref<Response[]> = ref([]);
const props = defineProps({
  questions: { type: Array<IQuestion>, default: [] },
  submitLoading: { type: Boolean },
  submitError: { type: Array<ResponseErrors> },
  submitSuccess: { type: Boolean },
  deleteLoading: { type: Boolean },
  deleteError: { type: Array<ResponseErrors> },
  deleteSuccess: { type: Boolean },
});

watch(
  () => props.questions,
  (newVal: IQuestion[], oldVal: IQuestion[]) => {
    if (newVal != oldVal) {
      responseSetup();
    }
  }
);

function responseSetup() {
  responses.value = [];
  if (props.questions.length) {
    props.questions.forEach((question: IQuestion) => {
      responses.value = [
        ...responses.value,
        {
          question: question.uuid,
          option: question?.response?.option ?? [],
          text: question?.response?.text ?? "",
        },
      ];
    });
  }
}

const emit = defineEmits(["deleteResponses", "submitResponse"]);

onMounted(() => {
  responseSetup();
});

function handleInput(question: IQuestion, event: Event) {
  let value = (event?.target as HTMLInputElement).value;
  let response = getResponse(question);
  if (response) {
    if (question.multi_select) {
      multiSelectInputHandler(value, response);
    } else {
      singleSelectInputHandler(value, response);
    }
  }
}

function multiSelectInputHandler(value: string, response: Response) {
  if (response.option.includes(value)) {
    response.option = response.option.filter((o: string) => o != value);
  } else {
    response.option = [...response.option, value];
  }
}

function singleSelectInputHandler(value: string, response: Response) {
  response.option = [value];
}

function getResponse(question: IQuestion): Response {
  return (
    responses.value.find((r: Response) => r.question == question.uuid) ?? {
      option: [],
      text: "",
    }
  );
}
</script>

<style scoped></style>
