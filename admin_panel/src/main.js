import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueAxios from 'vue-axios'
import axios from 'axios'
// import materialize from 'vue-materialize'
// import VueSession from 'vue-session'

// import 'materialize-css/dist/css/materialize.min.css'

createApp(App).use(router).use(VueAxios, axios).mount('#app')
// .use(VueSession)
// .use(materialize)