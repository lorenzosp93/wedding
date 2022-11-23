<template>
  <div id="main" class="font-serif">
    <router-view name="TheNavbar"></router-view>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
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
          classes: 'font-serif shadow-lg bg-pale dark:bg-darkPale min-w-sm shepherd-progress my-5 text-primary dark:text-darkPrimary',
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
              classes: 'bg-secondary dark:bg-darkNeutral',
              text: this.$t('shared.tour.back')
            },
            {
              action: () => {
                return this.tour.next();
              },
              classes: 'bg-accent text-primary',
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
            attachTo: {
              element: '#main',
              on: 'bottom'
            },
            buttons: [
              {
                action: () => {
                  this.$router.push({name: 'home'}).then( () => {
                    return this.tour.next()
                  })
                },
                classes: 'bg-accent text-primary',
                text: this.$t('shared.tour.next')
              }
            ],
          },{
            id: 'invite',
            text: this.$t('shared.tour.invite'),
            attachTo: {
              element: '#invite-link',
              on: 'bottom',
            },
          },{
            id: 'mobile-menu',
            text: this.$t('shared.tour.mobile-menu'),
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
                classes: 'bg-secondary dark:bg-darkNeutral',
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
          },{
            id: 'inbox-navbar',
            text: this.$t('shared.tour.inbox.navbar'),
            attachTo: {
              element: '#navbar-inbox',
              on: 'bottom',
            },
            buttons: [
              {
                action: () => {
                  return this.tour.back();
                },
                classes: 'bg-secondary dark:bg-darkNeutral',
                text: this.$t('shared.tour.back')
              },
              {
                action: () => {
                  this.$router.push({name: 'inbox'}).then(
                    () => {return this.tour.next()}
                  )
                },
                classes: 'bg-accent text-primary',
                text: this.$t('shared.tour.next')
              }
            ],
          },{
            id: 'inbox-list',
            text: this.$t('shared.tour.inbox.list'),
            attachTo: {
              element: '#list-view',
              on: 'bottom'
            },
            buttons: [
              {
                action: () => {
                  return this.tour.back();
                },
                classes: 'bg-secondary dark:bg-darkNeutral',
                text: this.$t('shared.tour.back')
              },
              {
                action: () => {
                  this.$router.push({name: 'inbox', params: {active: 0}}).then(
                    () => {return this.tour.next()}
                  )
                },
                classes: 'bg-accent text-primary',
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
            buttons: [
              {
                action: () => {
                  this.$router.push({name: 'inbox', params: {active: null}}).then(
                    () => {return this.tour.back()}
                  )
                },
                classes: 'bg-secondary dark:bg-darkNeutral',
                text: this.$t('shared.tour.back')
              },
              {
                action: () => {
                  return this.tour.next()
                },
                classes: 'bg-accent text-primary',
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
          },
          {
            id: 'profile',
            text: this.$t('shared.tour.profile'),
            attachTo: {
              element: '#navbar-profile',
              on: 'bottom'
            },
            buttons: [
              {
                action: () => {
                  return this.tour.back();
                },
                classes: 'bg-secondary dark:bg-darkNeutral',
                text: this.$t('shared.tour.back')
              },
              {
                action: () => {
                  this.dismissTour();
                  this.tour.complete();
                },
                classes: 'bg-accent text-primary',
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
      // if(!localStorage.getItem('shepherd-tour')) {
          this.tour.start();
      // }
    }

  },
}
</script>

<style>
  @import 'shepherd.js/dist/css/shepherd.css';

  .shepherd-cancel-icon {
    @apply text-primary;
  };

  .shepherd-text {
    @apply text-primary dark:text-darkNeutral
  }
  
  .shepherd-highlight {
    @apply ring-2 ring-accent stroke-accent
  }

</style>
