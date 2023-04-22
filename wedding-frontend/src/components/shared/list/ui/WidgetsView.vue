<template>
  <section id="object-widgets" class="px-3">
    <Teleport to="#header-title">
      <a
        v-if="calendarWidget"
        :href="`data:text/calendar;base64,${createICalBase64()}`"
        class="my-auto ml-auto px-2 py-1 shadow-md rounded-md bg-accent w-fit text-primary font-semibold flex cursor-pointer whitespace-nowrap"
      >
        <calendar-icon class="h-5 w-5 my-auto" />
        <time class="hidden @xl:block px-2 my-auto">
          {{ dateForDisplay("full") }}
        </time>
        <time class="hidden @md:block @xl:hidden px-2 my-auto">
          {{ dateForDisplay("medium") }}
        </time>
        <plus-icon class="h-5 w-5 my-auto" />
      </a>
    </Teleport>

    <div
      v-if="mapsWidget"
      class="bg-pale dark:bg-darkPale dark:text-darkNeutral rounded-md shadow-inner p-3 w-full @sm:flex my-3"
    >
      <div id="location-table" class="flex @sm:pl-3">
        <table class="mx-1 mb-auto">
          <tr>
            <map-icon class="h-6 w-6 float-left mr-1" />
            {{
              mapsWidget?.address1
            }}
          </tr>
          <tr>
            {{
              mapsWidget?.address2
            }}
          </tr>
          <tr>
            {{
              mapsWidget?.city
            }}
          </tr>
          <tr>
            {{
              mapsWidget?.postalCode
            }}
          </tr>
          <tr>
            {{
              mapsWidget?.country
            }}
          </tr>
        </table>
      </div>
      <iframe
        v-if="mapsWidget?.src"
        class="w-full mt-3 @sm:my-auto @sm:w-[50%] @md:w-[40%] mx-auto @sm:mx-0 @sm:mr-auto @sm:order-first aspect-square rounded-md shadow-inner"
        :src="mapsWidget.src"
        style="border: 0"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>
  </section>
</template>

<script setup lang="ts">
import { CalendarIcon, MapIcon, PlusIcon } from "@heroicons/vue/24/outline";
import { createEvent, type EventAttributes } from "ics";
import i18n from "@/i18n";
import { Teleport, type PropType, computed } from "vue";
import {
  WidgetType,
  type Widget,
  type ListObject,
} from "@/models/listObjects.interface";

const props = defineProps({
  activeObject: { type: Object as PropType<ListObject> },
});

const calendarWidget = computed(() => {
  return props.activeObject?.widget?.find(
    (w: Widget) => w.type == WidgetType.calendar
  )?.content;
});

const mapsWidget = computed(() => {
  return props.activeObject?.widget?.find(
    (w: Widget) => w.type == WidgetType.maps
  )?.content;
});
function createICalBase64() {
  const event: EventAttributes = {
    start: calendarWidget.value?.start ?? [2030, 1, 1], // [2018, 5, 30, 6, 30],
    startInputType: "utc", // provide dates in UTC
    duration: calendarWidget.value?.duration ?? { hours: 2 },
    title: props.activeObject?.subject,
    description: calendarWidget.value?.description,
    location: calendarWidget.value?.location,
    url: import.meta.url,
    geo: calendarWidget.value?.geo, //{ lat: 40.0095, lon: 105.2669 },
    status: calendarWidget.value?.status ?? "CONFIRMED",
    busyStatus: "BUSY",
    organizer: {
      name: "Priscilla and Lorenzo",
      email: "info@priscillalorenzo.com",
    },
  };
  return createEvent(event, (error, value) => {
    if (error) {
      console.log(error);
      return;
    }
    return window.btoa(value);
  });
}

function dateForDisplay(format: "full" | "long" | "medium" | "short" = "full") {
  let start = calendarWidget.value?.start as number[];
  start = [...(start as number[])]; // shallow copy
  if (!start) {
    return null;
  }
  start[1] -= 1; // months are 0-indexed
  const date = new Date(...(start as []));
  return date.toLocaleDateString(i18n.global.locale.value, {
    dateStyle: format,
  });
}
</script>

<style scoped></style>
