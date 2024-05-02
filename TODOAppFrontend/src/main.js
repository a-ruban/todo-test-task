import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { errorHandler } from '@/utils.js'

const app = createApp(App)

app.use(router)
app.config.errorHandler = errorHandler

app.mount('#app')
