import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
// import VueFileAgent from "vue-file-agent";
import VueFileAgentNext from '@boindil/vue-file-agent-next'
import '@boindil/vue-file-agent-next/dist/vue-file-agent-next.css'



loadFonts()

createApp(App)
  // .use(VueFileAgent)
  .use(VueFileAgentNext)
  .use(vuetify)
  .mount('#app')
