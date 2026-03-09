import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        "qc-blue": "#003da5",
        "qc-red": "#c8102e",
        "qc-light": "#f0f4ff",
      },
    },
  },
  plugins: [],
};

export default config;
