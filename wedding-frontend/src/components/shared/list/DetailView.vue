<!-- eslint-disable vue/no-v-html -->
<template>
    <article>
        <header class="flex justify-between items-center border-b-2 mb-8">
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
        </header>
        <section v-if="activeObject?.picture" class="w-full">
            <img :src="activeObject?.picture" alt="Information article picture" class="rounded-lg shadow-md" >
        </section>
        <section id="object-content" class="my-3 leading-7 tracking-wider" v-html="activeObject?.content"></section>
        <question-view v-if="activeObject?.questions?.length" :active-object="activeObject" :responses="responses" :submit-loading="submitLoading" :submit-error="submitError" :submit-success="submitSuccess" @submit-response="$emit('submitResponse', responses)" @delete-responses="$emit('deleteResponses', response)" ></question-view>
    </article>
</template>

<script>
import QuestionView from './QuestionView.vue';

export default {
    components: {
        QuestionView,
    },
    props: {
        viewDetail: { type: Boolean, default: false},
        activeObject: {type: Object},
        active: {type: Number},
        searchedList: {type: Array[Object]},
        responses: {type: Array[Object]},
        submitLoading: {type: Boolean},
        submitError: {type:Object},
        submitSuccess: {type: Boolean},
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