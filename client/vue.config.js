// vue.config.js
module.exports = {
  // options...
  runtimeCompiler: true,
  css: {
    loaderOptions: {
      sass: {
        prependData: `
          @import "@/assets/scss/colors.scss";
        `,
      },
    },
  },
};
