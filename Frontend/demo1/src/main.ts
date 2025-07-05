// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// 2. Quiz App
import router from './projects/2_car_app/router'
import Home from './projects/2_car_app/Home.vue'
const app = createApp(Home)
app.use(createPinia())
app.use(router)
app.mount('#app')
