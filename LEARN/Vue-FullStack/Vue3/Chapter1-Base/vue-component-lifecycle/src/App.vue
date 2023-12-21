<template>
    <keep-alive>
        <component :is="tabComponent"></component>
    </keep-alive>
    <button @click="switchHandle">Switch Component</button>
</template>

<script>
import { defineAsyncComponent } from "vue";
import ComponentLifecycleApp from "./components/ComponentLifecycleApp.vue";
import ComponentA from "./components/ComponentA.vue";
// import ComponentB from "./components/ComponentB.vue";
// 将 ComponentB 设置为异步加载
const ComponentB = defineAsyncComponent(() =>
    import("./components/ComponentB.vue")
);
export default {
    data() {
        return {
            // 赋值需要以字符串形式
            tabComponent: "ComponentA",
        };
    },
    methods: {
        switchHandle() {
            this.tabComponent =
                this.tabComponent == "ComponentA" ? "ComponentB" : "ComponentA";
        },
    },
    components: {
        ComponentLifecycleApp,
        ComponentA,
        ComponentB,
    },
};
</script>
