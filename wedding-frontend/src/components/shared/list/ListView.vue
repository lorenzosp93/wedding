<!-- eslint-disable vue/no-v-html -->
<template>
  <div class="w-full mx-auto max-w-5xl mt-2">
    <loading-view v-if="loading"></loading-view>
    <main v-show="!loading" class="flex w-full">
      <section
        id="list-view"
        class="flex flex-col w-full pt-3 px-3 md:w-[40%] lg:w-[35%] bg-neutral dark:bg-darkNeutral h-full max-h-rest"
      >
        <div class="flex flex-initial">
          <push-subscribe></push-subscribe>
          <input
            v-model.trim="search"
            type="text"
            class="rounded-lg my-auto p-3 bg-pale dark:bg-darkPale transition duration-200 w-full placeholder-secondary dark:placeholder-darkNeutral shadow-inner focus:ring-accent border-none"
            :placeholder="$t('shared.listview.search')"
          />
        </div>
        <ul class="mt-1 flex-auto overflow-y-auto">
          <list-item
            v-for="(obj, idx) in searchedList"
            :key="obj.uuid"
            @click="setActive(obj?.slug ?? '')"
            :obj="obj"
            :active="active == obj.slug"
          />
          <li v-if="searchedList?.length == 0 && objList?.length">
            <p class="p-3">{{ $t("shared.listview.noMessage") }}</p>
          </li>
          <li v-if="!objList?.length">
            <p class="p-3">{{ $t("shared.listview.done") }}</p>
          </li>
        </ul>
      </section>
      <detail-view
        :class="{ hidden: !viewDetail }"
        id="detail-view"
        :active-idx="searchedList?.indexOf(activeObject ?? searchedList[0])"
        :active-object="activeObject"
        :searched-list-length="searchedList?.length"
        :submit-error="submitError"
        :delete-error="deleteError"
        :submit-loading="submitLoading"
        :delete-loading="deleteLoading"
        :submit-success="submitSuccess"
        :delete-success="deleteSuccess"
        @hide-detail="hideDetail"
        @set-active="setActiveByIdx"
        @submit-response="
          (responses: Response[]) => emit('submitResponse', responses, activeObject?.uuid)
        "
        @delete-responses="(_) => emit('deleteResponses', activeObject?.uuid)"
      ></detail-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import LoadingView from "@/components/shared/LoadingView.vue";
import PushSubscribe from "@/components/shared/PushSubscribe.vue";
import DetailView from "./DetailView.vue";
import ListItem from "./ui/ListItem.vue";
import { ref, type PropType, Ref, computed, watch, onMounted } from "vue";
import type {
  ResponseErrors,
  ListObject,
  Response,
} from "@/models/listObjects.interface";
import type { AxiosError } from "axios";
import { useRoute, useRouter } from "vue-router";

const props = defineProps({
  objList: { type: Array<ListObject> },
  loading: { type: Boolean },
  error: { type: Object as PropType<AxiosError> },
  submitLoading: { type: Boolean },
  submitError: { type: Array<ResponseErrors> },
  submitSuccess: { type: Boolean },
  deleteLoading: { type: Boolean },
  deleteError: { type: Array<ResponseErrors> },
  deleteSuccess: { type: Boolean },
});
const emit = defineEmits(["submitResponse", "deleteResponses"]);

const active: Ref<string> = ref("");
const search: Ref<string> = ref("");
const viewDetail: Ref<boolean> = ref(false);

const searchedList: Ref<ListObject[] | undefined> = computed(() => {
  if (!search.value) {
    return props.objList;
  }
  return props.objList?.filter((obj) => {
    return (
      (obj?.subject + obj?.content)
        .toLowerCase()
        .search(search.value.toLowerCase()) != -1
    );
  });
});

const activeObject: Ref<ListObject | undefined> = computed(() => {
  return props.objList?.length
    ? props.objList.find((obj) => obj.slug == active.value) ?? props.objList[0]
    : undefined;
});

const route = useRoute();
const router = useRouter();

watch(
  () => route.params.active,
  async () => {
    if (route.params.active) {
      getActiveFromRoute();
    }
  }
);

onMounted(() => {
  getActiveFromRoute();
});

function getActiveFromRoute() {
  viewDetail.value = !!route.params.active;
  setActive(route.params.active as string);
}
function setActive(a: string) {
  active.value = a;
  router.push({
    name: route.name ?? undefined,
    params: { ...route.params, active: a },
  });
}

function setActiveByIdx(idx: number) {
  if (searchedList.value?.length) {
    let a = searchedList.value[idx]?.slug ?? "";
    setActive(a);
  }
}

function hideDetail() {
  setActive("");
  viewDetail.value = false;
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.max-h-rest {
  max-height: 90vh;
  max-height: calc(100vh - 80px);
  max-height: calc(100svh - 80px);
}
</style>
