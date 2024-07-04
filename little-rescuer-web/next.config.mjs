/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "zoobgm9uaafsrivd.public.blob.vercel-storage.com",
        port: "",
      },
    ],
  },
};

export default nextConfig;
