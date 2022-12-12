<template>
    <section id="object-widgets">
        <Teleport to="#header-title">
            <a v-if="calendarWidget" :href="`data:text/calendar;base64,${createICalBase64()}`" class="my-auto ml-auto px-2 py-1 shadow-lg rounded-md bg-accent w-fit text-primary flex cursor-pointer">
                <calendar-icon class="h-6 w-6" />
                <plus-icon class="h-6 w-6" />
            </a>

        </Teleport>

        <div v-if="mapsWidget" class="bg-pale dark:bg-darkPale dark:text-darkNeutral rounded-md shadow-lg p-3 w-full block md:flex my-3">
            <div id="location-table" class="flex">
                <map-pin-icon class="h-6 w-6" />
                <table class="mx-1 mb-auto">
                    <tr>{{ mapsWidget?.address1 }}</tr>
                    <tr>{{ mapsWidget?.address2 }}</tr>
                    <tr>{{ mapsWidget?.city }}</tr>
                    <tr>{{ mapsWidget?.postalCode }}</tr>
                    <tr>{{ mapsWidget?.country }}</tr>
                </table>
            </div>
            <iframe v-if="mapsWidget?.src" class="w-full my-2 md:my-auto md:w-1/2 ml-auto aspect-square rounded-md" :src="mapsWidget.src" style="border:0;"  loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe> 
        </div>
    </section>
</template>

<script>
import { CalendarIcon, MapPinIcon, PlusIcon } from '@heroicons/vue/24/outline'
import { createEvent } from 'ics'

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
        }
    },
    methods: {
        createICalBase64 () {
            const event = {
                start: this.calendarWidget.start, // [2018, 5, 30, 6, 30],
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
    },
}
</script>

<style scoped>
</style>
