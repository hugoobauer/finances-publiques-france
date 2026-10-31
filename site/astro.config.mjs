import { defineConfig } from 'astro/config';

// Site statique. Les contenus (fr/site/) et les données (platform/data/) sont lus
// au moment du build par src/lib/ : voir README.md.
export default defineConfig({
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
  devToolbar: { enabled: false },
});
