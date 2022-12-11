<template>
    <section id="object-widgets">
        <div v-if="calendarWidget">
            <calendar-icon class="h-6 w-6" />
        </div>
        <div v-if="mapsWidget">
            <map-pin-icon class="h-6 w-6" />
        </div>
    </section>
</template>

<script>
import { CalendarIcon, MapPinIcon } from '@heroicons/vue/24/outline'
import ics from 'ics'

export default {
    components: {
        CalendarIcon,
        MapPinIcon,
    },
    props: {
        activeObject: {type: Object},
    },
    computed: {
        calendarWidget () {
            return this.activeObject.widget.find(w => w.type == 'Calendar')
        },
        mapsWidget () {
            return this.activeObject.widget.find(w => w.type == 'Maps')
        }
    },
    methods: {
        createICalBase64 () {
            const event = {
                start: this.calendarWidget.start, // [2018, 5, 30, 6, 30],
                duration: this.calendarWidget.duration, //{ hours: 6, minutes: 30 },
                title: this.activeObject.subject,
                description: this.activeObject.content,
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
            const ical = ics.createEvent(event);
            return ical
        },
    },
}
</script>

<style scoped>
</style>
