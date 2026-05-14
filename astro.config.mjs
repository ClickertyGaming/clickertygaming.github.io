import { defineConfig, fontProviders } from "astro/config";

import db from "@astrojs/db";

// https://astro.build/config
export default defineConfig({
  output: 'static',
  site: "https://clickertygaming.github.io",

  devToolbar: {
      enabled: false
  },

  fonts: [{
      provider: fontProviders.fontsource(),
      name: "Roboto",
      cssVariable: "--font-roboto"
  }],

  integrations: [db()]
});