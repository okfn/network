const withMT = require("@material-tailwind/html/utils/withMT");

module.exports = withMT({
  darkMode: false, // or 'media' or 'class'
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  purge: ['layouts/**/*.html'],
  theme: {
    colors: {
      'project': '#AEFFEC',
      'specialist': '#FF80DB'
    },
    extend: {

    },
    fontFamily: {
      'body': ['"DM Sans"'],
      'dmsans': ['"DM Sans"'],
      'miriam': ['"Miriam Libre"']
    },
  },
  variants: {},
  plugins: [],
})
