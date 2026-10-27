/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  images: {
    domains: ['localhost', 'eis.ee', 'directus'],
  },
};

module.exports = nextConfig;
