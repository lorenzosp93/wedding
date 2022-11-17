module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      scale: {
        '102.5': '1.025'
      }
    },
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      primary: '#1F4045',
      secondary: '#7F9593',
      accent: '#D5B19B',
      pale: '#ECCDC4',
      neutral: '#EAE6E3',
      darkPrimary: '#EAE6E3',
      darkSecondary: '#ECCDC4',
      darkAccent: '#D5B19B',
      darkPale: '#7F9593',
      darkNeutral: '#1F4045',
      alert: 'red'
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
