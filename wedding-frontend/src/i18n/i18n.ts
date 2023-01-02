import { createI18n } from "vue-i18n";
import messages from "@intlify/unplugin-vue-i18n/messages";

const i18n = createI18n({
  locale:
    localStorage.getItem("lang") ||
    navigator.language ||
    // Detect user's browser language
    import.meta.env.VITE_APP_I18N_LOCALE,
  fallbackLocale: import.meta.env.VITE_APP_I18N_FALLBACK_LOCALE || "en",
  // Load selected lang's .json file
  availableLocales: ["en", "it", "es"],
  messages: messages,
  globalInjection: true,
});

export default i18n;
