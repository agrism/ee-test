/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Eesti Brändi DDS 2.0 Color Palette
        brand: {
          blue: '#0047B3',      // Primary EIS Blue
          darkBlue: '#002B80',  // Deep Blue
          lightBlue: '#E6F0FF', // Tint Blue
          accent: '#0066FF',    // Vivid Action Blue
          teal: '#00A389',      // Innovation Teal
          navy: '#0A1A3A',      // Headings & Dark background
          gray: {
            50: '#F8FAFC',
            100: '#F1F5F9',
            200: '#E2E8F0',
            300: '#CBD5E1',
            600: '#475569',
            800: '#1E293B',
            900: '#0F172A',
          }
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        heading: ['Outfit', 'Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      borderRadius: {
        'brand': '10px',
        'brand-sm': '6px',
        'brand-lg': '16px',
      }
    },
  },
  plugins: [],
};
