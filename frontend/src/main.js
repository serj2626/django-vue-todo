import axios from 'axios'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'


const app = createApp(App)
axios.defaults.baseURL = 'http://localhost:5173/';

app.use(router, axios)

app.mount('#app')
