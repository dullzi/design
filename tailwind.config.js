/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./js/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'sans-serif'],
      },
      colors: {
        brand: {
          blue: '#20658B',
          dark: '#015581',
          text: '#333333',
          black: '#F8F9FA',
          white: '#111827',
          cream: '#E5E7EB',
          accent: '#0A6BAA',
          accent2: '#E63C2F',
        }
      }
    },
  },
  plugins: [],
}
