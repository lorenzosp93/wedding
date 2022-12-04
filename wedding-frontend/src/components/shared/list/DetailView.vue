<!-- eslint-disable vue/no-v-html -->
<template>
    <div>
        <div class="flex justify-between items-center border-b-2 mb-8">
            <div class="flex space-x-4 items-center">
            <div class="h-6 w-6 md:hidden" @click="$emit('hideDetail')">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
    stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
                </svg>
            </div>
            <div class="flex flex-col">
                <h3 class="font-semibold text-2xl py-5">{{ activeObject?.subject }}</h3>
            </div>
            </div>
            <div>
            <ul class="flex text-primary dark:text-darkPrimary space-x-4 cursor-pointer">
                <li v-show="active != 0" class="w-6 h-6 rotate-90" @click="$emit('setActive', (active - 1))">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
                </svg>
                </li>
                <li v-show="active != searchedList?.length - 1 && searchedList?.length" class="w-6 h-6 rotate-90" @click="$emit('setActive', (active + 1))">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                </li>
            </ul>
            </div>
        </div>
        <div>
            <div v-if="activeObject?.picture" class="w-full">
            <img :src="activeObject?.picture" alt="Information article picture" class="rounded-lg shadow-md" >
            </div>
            <article class="my-3 leading-7 tracking-wider" v-html="activeObject?.content"></article>
            <div v-if="activeObject?.questions?.every(q => q.response) && activeObject?.questions?.length">
            <p class="my-2 text-accent" >{{ $t('shared.listview.alreadyAnswered') }}</p>
            <button class="bg-pale dark:bg-darkpale text-primary rounded-md px-2 py-1 mx-auto my-3" @click.prevent="$emit('deleteResponses')">{{ $t('shared.listview.changeResponses') }}</button>
            </div>
            <form v-if="activeObject?.questions?.length && responses?.length" @submit="$emit('submitResponse', responses)">
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
        </div>
    </div>
</template>

<script>
import LoadingView from '@/components/shared/LoadingView.vue';

export default {
    components: {
        LoadingView
    },
    props: {
        viewDetail: { type: Boolean, default: false},
        activeObject: {type: Object},
        active: {type: Number},
        searchedList: {type: Array[Object]},
        responses: {type: Array[Object]},
    },
    emits: [
        'hideDetail',
        'setActive',
        'deleteResponses',
        'submitResponse',
    ],
    data () {
        return {
        }
    },
    mounted () {
        window.addEventListener('keydown', (event) => {
            if (event.key == "ArrowRight" && this.active < this.searchedList?.length - 1) {
                this.$emit('setActive', this.active + 1);
            }
            if (event.key == "ArrowLeft" && this.active > 0) {
                this.$emit('setActive', this.active - 1)
            }
        })
    }
}

</script>

<style scoped>
</style>