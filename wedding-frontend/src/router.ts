import { createRouter, createWebHistory, type RouteLocation } from "vue-router";
import { useAuthStore } from "@/stores";

import LoginPage from "@/components/auth/LoginPage.vue";
import RegisterPage from "@/components/auth/RegisterPage.vue";

// Lazy load
const LoginSuccess = () => import("@/components/auth/LoginSuccess.vue");
const TheHome = () => import("@/components/TheHome.vue");
const TheInvitation = () => import("@/components/TheInvitation.vue");
const TheNavbar = () => import("@/components/shared/TheNavbar.vue");
const TheInbox = () => import("@/components/inbox/TheInbox.vue");
const TheInfo = () => import("@/components/information/TheInfo.vue");
const TheGallery = () => import("@/components/gallery/TheGallery.vue");
const TheProfile = () => import("@/components/profile/TheProfile.vue");
const TheGuestBook = () => import("@/components/guestbook/TheGuestBook.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { name: "login", path: "/login", component: LoginPage },
    { name: "register", path: "/register", component: RegisterPage },
    { name: "login-success", path: "/login/success", component: LoginSuccess },
    { name: "home", path: "/", components: { default: TheHome, TheNavbar } },
    {
      name: "invitation",
      path: "/invitation",
      components: { default: TheInvitation, TheNavbar },
    },
    {
      name: "inbox",
      path: "/inbox/:active?",
      components: { default: TheInbox, TheNavbar },
    },
    {
      name: "info",
      path: "/info/:infoType?/:active?",
      components: { default: TheInfo, TheNavbar },
    },
    {
      name: "gallery",
      path: "/gallery",
      components: { default: TheGallery, TheNavbar },
    },
    {
      name: "profile",
      path: "/profile",
      components: { default: TheProfile, TheNavbar },
    },
    {
      name: "guestbook",
      path: "/guestbook",
      components: { default: TheGuestBook, TheNavbar },
    },
  ],
});

router.beforeEach(async (to: RouteLocation) => {
  // redirect to login page if not logged in and trying to access a restricted page

  const publicPages = ["login", "login-success", "register"];
  const authRequired = !publicPages.includes(to.name as string);

  const auth = useAuthStore();
  const token = auth.token || to.query["token"];

  if (!auth.profile?.id && token) {
    await auth.login(token as string);
    return;
  }

  if (authRequired && !token) {
    return { ...to, name: "login" };
  }
  if (!authRequired && token) {
    return { ...to, name: "home" };
  }
});

export default router;
