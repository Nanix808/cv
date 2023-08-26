import { createApp } from 'vue'
import App from './App.vue'
import { store } from './store/index.js'
import { routers } from './routers/index.js'


createApp(App)
.use(store)
.use(routers)
.mount('#app')
