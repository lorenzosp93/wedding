<template>
    <section id="object-widgets">
        <Teleport to="#header-title">
            <a v-if="calendarWidget" :href="`data:text/calendar;base64,${createICalBase64()}`" class="my-auto ml-auto px-2 py-1 shadow-lg rounded-md bg-accent w-fit text-primary font-semibold flex cursor-pointer whitespace-nowrap">
                <calendar-icon class="h-6 w-6 my-auto" />
                <time class="hidden lg:block px-2 my-auto">
                    {{ dateForDisplay('full') }}
                </time>
                <time class="hidden md:max-lg:block px-2 my-auto">
                    {{ dateForDisplay('medium') }}
                </time>
                <plus-icon class="h-6 w-6 my-auto" />
            </a>

        </Teleport>

        <div v-if="mapsWidget" class="bg-pale dark:bg-darkPale dark:text-darkNeutral rounded-md shadow-lg p-3 w-full block sm:flex my-3">
            <div id="location-table" class="flex">
                <map-pin-icon class="h-6 md:h-7 w-6 md:w-7" />
                <table class="mx-1 mb-auto font-semibold">
                    <tr>{{ mapsWidget?.address1 }}</tr>
                    <tr>{{ mapsWidget?.address2 }}</tr>
                    <tr>{{ mapsWidget?.city }}</tr>
                    <tr>{{ mapsWidget?.postalCode }}</tr>
                    <tr>{{ mapsWidget?.country }}</tr>
                </table>
            </div>
            <iframe v-if="mapsWidget?.src" class="w-full mt-3 sm:my-auto sm:w-[40%] max-sm:mx-auto sm:ml-auto aspect-square rounded-md shadow-lg" :src="mapsWidget.src" style="border:0;"  loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe> 
        </div>
    </section>
</template>

<script>
import { CalendarIcon, MapPinIcon, PlusIcon } from '@heroicons/vue/24/outline'
import { createEvent } from 'ics'
import i18n from '@/i18n'

export default {
    components: {
        CalendarIcon,
        MapPinIcon,
        PlusIcon,
    },
    props: {
        activeObject: {type: Object},
    },
    computed: {
        calendarWidget () {
            return this.activeObject.widget.find(w => w.type == 'calendar')?.content
        },
        mapsWidget () {
            return this.activeObject.widget.find(w => w.type == 'maps')?.content
        },
    },
    methods: {
        createICalBase64 () {
            const event = {
                start: this.calendarWidget.start, // [2018, 5, 30, 6, 30],
                startInputType: 'utc', // provide dates in UTC
                duration: this.calendarWidget?.duration ?? {hours: 2},
                title: this.activeObject.subject,
                description: this.calendarWidget?.description,
                location: this.activeObject?.location,
                url: import.meta.url,
                geo: this.calendarWidget?.geo, //{ lat: 40.0095, lon: 105.2669 },
                status: this.calendarWidget?.status ?? "CONFIRMED",
                busyStatus: 'BUSY',
                organizer: {
                    name: 'Priscilla and Lorenzo',
                    email: 'info@priscillalorenzo.com'
                },
            };
            return createEvent(event, (error, value) => {
                if (error) {
                    console.log(error);
                    return
                }
                return window.btoa(value)
            });
        },
        dateForDisplay (format='full') {
            let start = this.calendarWidget?.start
            start = [...start] // shallow copy
            if (!start) {return null};
            start[1] -= 1 // months are 0-indexed
            const date = new Date(...start)
            return date.toLocaleDateString(i18n.global.locale.value, {dateStyle: format})
        }
    },
}
</script>

<style scoped>
</style>
