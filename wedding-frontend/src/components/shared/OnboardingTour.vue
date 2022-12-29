<template>
  <div v-show="tour" id="tour-trigger" class="fixed bottom-0 right-0 p-3">
    <button
      :aria-label="$t('shared.onboardingtour.tourButton')"
      class="p-1 bg-neutral dark:bg-darkNeutral rounded-md"
      @click="tour?.start"
    >
      <information-circle-icon class="h-6 w-6 md:h-7 md:w-7" />
    </button>
  </div>
</template>

<script lang="ts">
import { InformationCircleIcon } from "@heroicons/vue/24/outline";
import { useNotificationStore } from "@/stores/notification.store";
import Shepherd from "shepherd.js";

const notificationStore = useNotificationStore();

let pushSubscribeVisible =
  "serviceWorker" in navigator &&
  "PushManager" in window &&
  !notificationStore.isSubscribed;

export default {
  name: "OnboardingTour",
  components: {
    InformationCircleIcon,
  },
  data() {
    return {
      tour: undefined as undefined | Shepherd.Tour,
    };
  },
  created() {
    this.setupTour();
    this.tour?.on("cancel", this.dismissTour);
  },
  mounted() {
    this.startTour();
  },
  methods: {
    setupTour() {
      this.tour = new Shepherd.Tour({
        useModalOverlay: true,
        confirmCancel: true,
        confirmCancelMessage: this.$t("shared.tour.confirmCancel"),
        keyboardNavigation: false,
        defaultStepOptions: {
          title: undefined,
          arrow: false,
          modalOverlayOpeningPadding: 5,
          modalOverlayOpeningRadius: 5,
          canClickTarget: false,
          scrollTo: {
            behavior: "smooth",
            block: "center",
          },
          buttons: [
            {
              action: () => {
                return this.tour?.back();
              },
              secondary: true,
              text: this.$t("shared.tour.back"),
            },
            {
              action: () => {
                return this.tour?.next();
              },
              text: this.$t("shared.tour.next"),
            },
          ],
          cancelIcon: {
            enabled: true,
          },
        },
        steps: [
          {
            id: "intro",
            text: this.$t("shared.tour.intro"),
            modalOverlayOpeningPadding: -5,
            modalOverlayOpeningRadius: 10,
            buttons: [
              {
                action: () => {
                  this.$router.push({ name: "home" }).then(() => {
                    return this.tour?.next();
                  });
                },
                text: this.$t("shared.tour.next"),
              },
            ],
          },
          {
            id: "invite",
            text: this.$t("shared.tour.invite"),
            attachTo: {
              element: "#invite-link",
              on: "bottom",
            },
          },
          {
            id: "mobile-menu",
            text: this.$t("shared.tour.mobile-menu"),
            classes: "mt-3",
            attachTo: {
              element: "#menu-toggle",
              on: "bottom",
            },
            canClickTarget: true,
            showOn: () => {
              return (
                window.innerWidth < 768 &&
                window.getComputedStyle(
                  document.getElementById("navbar-default") ?? new Element()
                ).visibility == "hidden"
              );
            },
            buttons: [
              {
                action: () => {
                  return this.tour?.back();
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
            ],
            advanceOn: {
              selector: "#menu-toggle",
              event: "click",
            },
            highlightClass: "shepherd-highlight",
          },
          {
            id: "information",
            text: this.$t("shared.tour.information"),
            attachTo: {
              element: "#navbar-information",
              on: "bottom",
            },
            classes: "mt-3",
          },
          {
            id: "guestbook",
            text: this.$t("shared.tour.guestbook"),
            attachTo: {
              element: "#navbar-guestbook",
              on: "bottom",
            },
            classes: "mt-3",
          },
          {
            id: "inbox-navbar",
            text: this.$t("shared.tour.inbox.navbar"),
            attachTo: {
              element: "#navbar-inbox",
              on: "bottom",
            },
            classes: "mt-3",
            buttons: [
              {
                action: () => {
                  return this.tour?.back();
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
              {
                action: () => {
                  this.tour?.hide();
                  this.$router.push({ name: "inbox" }).then(() => {
                    this.tour?.show("inbox-navbar");
                    return this.tour?.next();
                  });
                },
                text: this.$t("shared.tour.next"),
              },
            ],
          },
          {
            id: "inbox-list",
            text: this.$t("shared.tour.inbox.list"),
            attachTo: {
              element: "#list-view",
              on: "bottom",
            },
            modalOverlayOpeningPadding: -5,
            buttons: [
              {
                action: () => {
                  this.$router.push({ name: "home" }).then(() => {
                    return this.tour?.back();
                  });
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
              {
                action: () => {
                  this.$router
                    .push({ name: "inbox", params: { active: 0 } })
                    .then(() => {
                      return this.tour?.next();
                    });
                },
                text: this.$t("shared.tour.next"),
              },
            ],
          },
          {
            id: "inbox-detail",
            text: this.$t("shared.tour.inbox.detail"),
            attachTo: {
              element: "#detail-view",
              on: "bottom",
            },
            modalOverlayOpeningPadding: -5,
            buttons: [
              {
                action: () => {
                  this.$router
                    .push({ name: "inbox", params: { active: null } })
                    .then(() => {
                      return this.tour?.back();
                    });
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
              {
                action: () => {
                  this.$router
                    .push({ name: "inbox", params: { active: null } })
                    .then(() => {
                      return this.tour?.next();
                    });
                },
                text: this.$t("shared.tour.next"),
              },
            ],
          },
          {
            id: "push-subscribe",
            text: this.$t("shared.tour.inbox.pushNotification"),
            modalOverlayOpeningPadding: -4,
            modalOverlayOpeningRadius: 10,
            canClickTarget: true,
            showOn: () => {
              return pushSubscribeVisible;
            },
            attachTo: {
              element: "#notification-trigger",
              on: "top",
            },
            buttons: [
              {
                action: () => {
                  this.$router
                    .push({ name: "inbox", params: { active: 0 } })
                    .then(() => {
                      return this.tour?.back();
                    });
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
              {
                action: () => {
                  return this.tour?.next();
                },
                text: this.$t("shared.tour.next"),
              },
            ],
          },
          {
            id: "gallery",
            text: this.$t("shared.tour.gallery"),
            attachTo: {
              element: "#navbar-gallery",
              on: "bottom",
            },
            classes: "mt-3",
            buttons: [
              {
                action: () => {
                  if (!pushSubscribeVisible) {
                    this.$router
                      .push({ name: "inbox", params: { active: 0 } })
                      .then(() => {
                        return this.tour?.back();
                      });
                  } else {
                    return this.tour?.back();
                  }
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
              {
                action: () => {
                  return this.tour?.next();
                },
                text: this.$t("shared.tour.next"),
              },
            ],
          },
          {
            id: "profile",
            text: this.$t("shared.tour.profile"),
            attachTo: {
              element: "#navbar-profile",
              on: "bottom",
            },
            classes: "mt-3",
            buttons: [
              {
                action: () => {
                  return this.tour?.back();
                },
                secondary: true,
                text: this.$t("shared.tour.back"),
              },
              {
                action: () => {
                  this.dismissTour();
                  this.tour?.complete();
                  this.$router.push({ name: "home" });
                },
                text: this.$t("shared.tour.finish"),
              },
            ],
          },
        ],
      });
    },
    dismissTour() {
      if (!localStorage.getItem("shepherd-tour")) {
        localStorage.setItem("shepherd-tour", "true");
      }
    },
    startTour() {
      if (!localStorage.getItem("shepherd-tour")) {
        this.tour?.start();
      }
    },
  },
};
</script>

<style>
@import "shepherd.js/dist/css/shepherd.css";

.shepherd-element {
  @apply bg-neutral dark:bg-darkNeutral rounded-lg font-serif max-w-md;
}

.shepherd-content {
  @apply whitespace-pre-line;
}

.shepherd-cancel-icon {
  @apply text-secondary dark:text-darkPale;
}

.shepherd-text {
  @apply text-primary dark:text-darkPrimary px-5;
}

.shepherd-highlight {
  @apply ring-2 ring-accent text-accent stroke-accent;
}

.shepherd-header {
  @apply h-6 px-3;
}

.shepherd-button {
  @apply py-1 px-2 rounded-md shadow-md mx-2 bg-accent text-primary !important;
}

.shepherd-button-secondary {
  @apply bg-secondary text-neutral !important;
}
</style>
