import { createApp } from "vue";
import App from "./App.vue";
import Header from "./pages/Header.vue";

const app = createApp(App);
// Global Registration, define among const app =  createApp(App) & app.mount('#app')
app.component("Header", Header);
app.mount("#app");
