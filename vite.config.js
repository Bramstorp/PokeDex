import vue from '@vitejs/plugin-vue'
import ssr from 'vite-plugin-ssr/plugin'

export default {
  server: {
    hmr: {
      clientPort: 3001,
    },
  },
  plugins: [vue(), ssr()],
}
