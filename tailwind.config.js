const withMT = require("@material-tailwind/html/utils/withMT");

module.exports = withMT({
  darkMode: false, // or 'media' or 'class'
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  content: ['layouts/**/*.html'],
  theme: {
    colors: {
      'project': '#AEFFEC',
      'specialist': '#FF80DB',
      'skyblue': {
        500: '00D1FF',
      },
      'aeroblue':{
        500: '#AEFFEC'
      },
      'lightpink':{
        500: '#ff80db'
      }
    },
    extend: {

    },
    fontFamily: {
      'body': ['"DM Sans"'],
      'dmsans': ['"DM Sans"'],
      'miriam': ['"Miriam Libre"']
    },
    borderRadius: {
      '3xl': '90px',
    },
  },
  variants: {},
  plugins: [],
})
