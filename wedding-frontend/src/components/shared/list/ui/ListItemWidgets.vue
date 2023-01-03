<template>
  <div>
    <div v-if="hasResponses" class="group float-left relative mb-auto">
      <chat-bubble-left-right-icon class="w-6 h-6 stroke-secondary">
      </chat-bubble-left-right-icon>
      <tooltip-item>
        {{ $t("shared.list.ui.listitem.youAlreadyReplied") }}
      </tooltip-item>
    </div>
    <div
      v-if="hasQuestions && !hasResponses"
      class="group float-left relative mb-auto"
    >
      <chat-bubble-left-icon class="w-6 h-6 stroke-accent">
      </chat-bubble-left-icon>
      <tooltip-item>
        {{ $t("shared.list.ui.listitem.youStillHavent") }}
      </tooltip-item>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  ChatBubbleLeftIcon,
  ChatBubbleLeftRightIcon,
} from "@heroicons/vue/24/outline";
import TooltipItem from "./TooltipItem.vue";

export default defineComponent({
  name: "ListItemWidgets",
  components: {
    ChatBubbleLeftIcon,
    ChatBubbleLeftRightIcon,
    TooltipItem,
  },
  props: {
    hasQuestions: { type: Boolean },
    hasResponses: { type: Boolean },
  },
});
</script>
