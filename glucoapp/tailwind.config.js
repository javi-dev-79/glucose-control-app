const forms = require('@tailwindcss/forms')
const typography = require('@tailwindcss/typography')
const aspectRatio = require('@tailwindcss/aspect-ratio')

module.exports = {
  content: [
    '../templates/**/*.html',
    './templates/**/*.html',
    './**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [forms, typography, aspectRatio],
}
