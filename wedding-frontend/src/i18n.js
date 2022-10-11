import { createI18n } from "vue-i18n";

// On change of language, switch the /locals/_language_.json file
function loadLocaleMessages() {
  const locales = require.context(
    "./locales",
    true,
    /[A-Za-z0-9-_,\s]+\.json$/i
  );
  const messages = {};
  locales.keys().forEach((key) => {
    const matched = key.match(/([A-Za-z0-9-_]+)\./i);
    if (matched && matched.length > 1) {
      const locale = matched[1];
      messages[locale] = locales(key);
    }
  });
  return messages;
}

// Detect default language of browser, and apply it on start
function detectLanguage() {
  const lng = window.navigator.userLanguage || window.navigator.language;
  const locales = require.context(
    "./locales",
    true,
    /[A-Za-z0-9-_,\s]+\.json$/i
  );
  const lang = locales
    .keys()
    .find((key) => lng.includes(key.replace("./", "").replace(".json", "")));
  return lang ? lang.replace("./", "").replace(".json", "") : null;
}

const i18n = createI18n({
  legacy: false,
  locale:
    localStorage.getItem('lang') ||
    // Detect user's browser language
    detectLanguage() ||
    process.env.VUE_APP_I18N_LOCALE,
  fallbackLocale: process.env.VUE_APP_I18N_FALLBACK_LOCALE || 'en',
  // Load selected lang's .json file
  messages: loadLocaleMessages(),
  globalInjection: true,
});

export default i18n;