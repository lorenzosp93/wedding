<!-- eslint-disable vue/no-v-html -->
<template>
    <article>
        <header id="object-header" class="flex justify-between items-center border-b-2 mb-8">
            <div class="h-6 w-6 mr-2 md:hidden" @click="$emit('hideDetail')">
                <arrow-left-icon class="h-6 w-6" />
            </div>
            <div id="header-title" class="flex w-full">
                <h3 class="font-semibold text-2xl py-5">{{ activeObject?.subject }}</h3>
            </div>
            <div>
                <ul class="flex text-primary dark:text-darkPrimary ml-2 space-x-4 cursor-pointer order-last">
                    <li v-show="active != 0" class="w-6 h-6" @click="$emit('setActive', (active - 1))">
                        <arrow-up-icon class="h-6 w-6" />
                    </li>
                    <li v-show="active != searchedList?.length - 1 && searchedList?.length" class="w-6 h-6" @click="$emit('setActive', (active + 1))">
                        <arrow-down-icon class="h-6 w-6" />
                    </li>
                </ul>
            </div>
        </header>
        <section v-if="activeObject?.picture" id="object-picture" class="w-full">
            <img :src="activeObject?.picture" alt="Information article picture" class="rounded-lg shadow-md" >
        </section>
        <section id="object-content" class="my-3 leading-7 tracking-wider" v-html="activeObject?.content"></section>
        <widgets-view v-if="activeObject?.widget?.length && loadWidgets" :active-object="activeObject"></widgets-view>
        <question-view v-if="activeObject?.questions?.length" :active-object="activeObject" :responses="responses" :submit-loading="submitLoading" :submit-error="submitError" :submit-success="submitSuccess" @submit-response="$emit('submitResponse', responses)" @delete-responses="$emit('deleteResponses', response)" ></question-view>
    </article>
</template>

<script>
import QuestionView from './QuestionView.vue';
import WidgetsView from './WidgetsView.vue';
import { ArrowLeftIcon, ArrowUpIcon, ArrowDownIcon } from '@heroicons/vue/24/outline';

export default {
    components: {
        QuestionView,
        WidgetsView,
        ArrowDownIcon,
        ArrowLeftIcon,
        ArrowUpIcon,
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
            loadWidgets: false,
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
        });
        this.loadWidgets = true;
    }
}

</script>

<style scoped>
</style>