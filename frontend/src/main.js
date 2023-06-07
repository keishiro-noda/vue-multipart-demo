import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import VueFileAgent from "vue-file-agent";



loadFonts()

createApp(App)
  .use(vuetify)
  .mount('#app')
  .use(VueFileAgent)
