<!-- eslint-disable vue/no-v-html -->
<template>
    <div v-if="activeObject?.questions?.every(q => q.response)">
    <p class="my-2 text-accent" >{{ $t('shared.listview.alreadyAnswered') }}</p>
    <button class="bg-pale dark:bg-darkpale text-primary rounded-md px-2 py-1 mx-auto my-3" @click.prevent="$emit('deleteResponses')">{{ $t('shared.listview.changeResponses') }}</button>
    </div>
    <form v-if="responses?.length" @submit="$emit('submitResponse', responses)">
    <div v-for="(question, idx) in activeObject?.questions" :key="question.uuid">
        <h1 class="text-lg">{{ idx + 1 }}. {{ question.subject }}</h1>
        <p v-html="question.content"></p>
        <ul v-if="question.options?.length" :multiple="question.multi_select" class="w-full my-2 bg-pale dark:bg-darkPale rounded-md">
        <li v-for="option in question.options" :key="option.uuid" >
            <input
            :id="option.uuid"
            v-model="responses.find(r => r.question == question.uuid).option"
            :name="question.uuid"
            :type="question.multi_select ? 'checkbox' : 'radio'"
            :value="option.uuid"
            class="my-2 bg-neutral dark:bg-darkNeutral text-accent"
            :disabled="question.response ? (question.multi_select ? true : question?.response?.option != option.uuid) : false"
            :required="question.mandatory">
            <label :for="option.uuid" class="ml-3">{{ option.content }}</label>
        </li>
        </ul>
        <p v-if="submitError?.find(e => e.q == question.uuid && e.e?.option)" class="text-alert">{{ submitError.find(e => e.q == question.uuid)?.e.option[0] }}</p>
        <div v-if="question.free_text" class="mb-5">
        <label v-if="question.options?.length" for="input" class="my-1">{{ $t('shared.listview.other') }}</label>
        <input v-model="responses.find(r => r.question == question.uuid).text" type="text" class="w-full rounded-md bg-pale dark:bg-darkPale px-2 py-1" :readonly="question.response" :required="question.mandatory && question.options.length == 0" >
        <p v-if="submitError?.find(e => e.q == question.uuid && e.e?.text)" class="text-alert mx-3"> {{ submitError.find(e => e.q == question.uuid)?.e.text[0] }}</p>
        </div>
        <p v-if="question.uuid == submitError?.find(e => e.q == question.uuid && e.e?.non_field_errors)">{{ submitError.find(e => e.q == question)?.e.non_field_errors[0] }}</p>
    </div>
    <div class="relative h-20 w-full pt-5 mx-auto">
        <button v-show="!submitLoading && activeObject?.questions.some(q => !q.response)" class="bg-accent text-primary rounded-md px-2 py-1 flex mx-auto" @click.prevent="$emit('submitResponse', responses)">{{ $t('shared.listview.submit') }}</button>
        <loading-view v-if="submitLoading"></loading-view>
        <p v-if="submitSuccess">{{ $t('shared.listview.success') }}</p>
    </div>
    </form>
</template>

<script>
import LoadingView from '@/components/shared/LoadingView.vue';

export default {
    components: {
        LoadingView,
    },
    props: {
        activeObject: {type: Object},
        responses: {type: Array[Object]},
        submitLoading: {type: Boolean},
        submitError: {type:Object},
        submitSuccess: {type: Boolean},
    },
    emits: ['deleteResponses', 'submitResponse'],
}
</script>

<style scoped>
</style>