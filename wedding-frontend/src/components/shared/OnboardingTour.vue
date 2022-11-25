<template>
    <div class="fixed bottom-0 right-0 p-3  fill-secondary dark:fill-darkPale">
        <button id="tour-trigger" @click="tour.start()">
            <svg class="w-6 md:w-7" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2.033 16.01c.564-1.789 1.632-3.932 1.821-4.474.273-.787-.211-1.136-1.74.209l-.34-.64c1.744-1.897 5.335-2.326 4.113.613-.763 1.835-1.309 3.074-1.621 4.03-.455 1.393.694.828 1.819-.211.153.25.203.331.356.619-2.498 2.378-5.271 2.588-4.408-.146zm4.742-8.169c-.532.453-1.32.443-1.761-.022-.441-.465-.367-1.208.164-1.661.532-.453 1.32-.442 1.761.022.439.466.367 1.209-.164 1.661z"/>
            </svg>
        </button>
    </div>
</template>

<script>
export default {
    name: 'OnboardingTour',
    data () {
        return {
            tour: null,
        }
    },
    created() {
        this.setupTour();
        this.tour.on('cancel', this.dismissTour);
    },
    mounted () {
        this.startTour();
    },
    methods: {
        setupTour () {
            this.tour = new this.$shepherd.Tour({
            useModalOverlay: true,
            defaultStepOptions: {
                keyboardNavigation: false,
                arrow: false,
                modalOverlayOpeningPadding: 5,
                modalOverlayOpeningRadius: 5,
                title: false,
                canClickTarget: false,
                modalContainer: '#app',
                stepsContainer: '#app',
                scrollTo: {
                    behavior: 'smooth',
                    block: 'center',
                },
                buttons: [
                {
                    action: () => {
                    return this.tour.back();
                    },
                    secondary: true,
                    text: this.$t('shared.tour.back')
                },
                {
                    action: () => {
                    return this.tour.next();
                    },
                    text: this.$t('shared.tour.next')
                }
                ],
                cancelIcon: {
                class: 'fill-primary',
                enabled: true,
                },
            },
            steps: [{
                    id: 'intro',
                    text: this.$t('shared.tour.intro'),
                    buttons: [
                        {
                        action: () => {
                            this.$router.push({name: 'home'}).then( () => {
                                return this.tour.next()
                            })
                        },
                        text: this.$t('shared.tour.next')
                        }
                    ],
                },{
                    id: 'invite',
                    text: this.$t('shared.tour.invite'),
                    classes: 'mt-3',
                    attachTo: {
                        element: '#invite-link',
                        on: 'bottom',
                    },
                },{
                    id: 'mobile-menu',
                    text: this.$t('shared.tour.mobile-menu'),
                    classes: 'mt-3',
                    attachTo: {
                        element: '#menu-toggle',
                        on: 'bottom',
                    },
                    canClickTarget: true,
                    showOn: () => {
                        return window.innerWidth < 768 && window.getComputedStyle(document.getElementById('navbar-default')).visibility == 'hidden'
                    },
                    buttons: [{
                        action: () => {
                            return this.tour.back();
                        },
                        secondary: true,
                        text: this.$t('shared.tour.back')
                    }],
                    advanceOn: {
                        selector: '#menu-toggle',
                        event: 'click'
                    },
                    highlightClass: 'shepherd-highlight'
                    },{
                    id: 'information',
                    text: this.$t('shared.tour.information'),
                    attachTo: {
                        element: '#navbar-information',
                        on: 'bottom',
                    },
                    classes: 'mt-3',
                },{
                    id: 'inbox-navbar',
                    text: this.$t('shared.tour.inbox.navbar'),
                    attachTo: {
                        element: '#navbar-inbox',
                        on: 'bottom',
                    },
                    classes: 'mt-3',
                    buttons: [
                        {
                        action: () => {
                            return this.tour.back();
                        },
                        secondary: true,
                        text: this.$t('shared.tour.back')
                        },
                        {
                        action: () => {
                            this.tour.hide();
                            this.$router.push({name: 'inbox'}).then(
                            () => {
                                this.tour.show('inbox-navbar');
                                return this.tour.next();
                            }
                            )
                        },
                        text: this.$t('shared.tour.next')
                        }
                    ],
                },{
                    id: 'inbox-list',
                    text: this.$t('shared.tour.inbox.list'),
                    attachTo: {
                        element: '#list-view',
                        on: 'right'
                    },
                    modalOverlayOpeningPadding: 0,
                    buttons: [
                        {
                        action: () => {
                            this.$router.push({name: 'home'}).then(
                            () =>  {return this.tour.back()}
                            )
                        },
                        secondary: true,
                        text: this.$t('shared.tour.back')
                        },
                        {
                        action: () => {
                            this.$router.push({name: 'inbox', params: {active: 0}}).then(
                            () => {return this.tour.next()}
                            )
                        },
                        text: this.$t('shared.tour.next')
                        }
                    ],
                },{
                    id: 'inbox-detail',
                    text: this.$t('shared.tour.inbox.detail'),
                    attachTo: {
                        element: '#detail-view',
                        on: 'left'
                    },
                    modalOverlayOpeningPadding: 0,
                    buttons: [
                        {
                        action: () => {
                            this.$router.push({name: 'inbox', params: {active: null}}).then(
                            () => {return this.tour.back()}
                            )
                        },
                        secondary: true,
                        text: this.$t('shared.tour.back')
                        },
                        {
                        action: () => {
                            return this.tour.next()
                        },
                        text: this.$t('shared.tour.next')
                        }
                    ],
                },{
                    id: 'gallery',
                    text: this.$t('shared.tour.gallery'),
                    attachTo: {
                        element: '#navbar-gallery',
                        on: 'bottom'
                    },
                    classes: 'mt-3',
                },
                {
                    id: 'profile',
                    text: this.$t('shared.tour.profile'),
                    attachTo: {
                        element: '#navbar-profile',
                        on: 'bottom'
                    },
                    classes: 'mt-3',
                    buttons: [
                        {
                        action: () => {
                            return this.tour.back();
                        },
                        secondary: true,
                        text: this.$t('shared.tour.back')
                        },
                        {
                        action: () => {
                            this.dismissTour();
                            this.tour.complete();
                            this.$router.push({name: 'home'});
                        },
                        text: this.$t('shared.tour.finish')
                        }
                    ],
                },
            ]
            });

        },
        dismissTour () {
            if(!localStorage.getItem('shepherd-tour')) {
                localStorage.setItem('shepherd-tour', 'true');
            }
        },
        startTour () {
            if(!localStorage.getItem('shepherd-tour')) {
                this.tour.start();
            }
        }
    }
}
</script>

<style>
  @import 'shepherd.js/dist/css/shepherd.css';

  .shepherd-element {
    @apply  bg-neutral dark:bg-darkNeutral rounded-lg font-serif max-w-md;
  }

  .shepherd-content {
    @apply whitespace-pre-line;
  }

  .shepherd-cancel-icon {
    @apply text-secondary dark:text-darkPale;
  };

  .shepherd-text {
    @apply text-primary dark:text-darkPrimary px-5;
  };
  
  .shepherd-highlight {
    @apply ring-2 ring-accent text-accent stroke-accent;
  };

  .shepherd-header {
    @apply h-6 px-3;
  };
  
  .shepherd-button {
    @apply py-1 px-2 rounded-md shadow-md mx-2 bg-accent text-primary !important;
  };

  .shepherd-button-secondary {
    @apply bg-secondary text-neutral !important;
  };

</style>