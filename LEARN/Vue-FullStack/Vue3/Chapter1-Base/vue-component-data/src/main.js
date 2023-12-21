import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);
app.provide("globalData", "global data");
app.mount("#app");
