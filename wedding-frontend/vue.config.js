const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  pages: {
    index: {
      // entry for the page
      entry: 'src/main.js',
      title: "Priscilla and Lorenzo's wedding",
    },
  },
  configureWebpack: {
    devtool: 'source-map'
  },
  transpileDependencies: true,
})