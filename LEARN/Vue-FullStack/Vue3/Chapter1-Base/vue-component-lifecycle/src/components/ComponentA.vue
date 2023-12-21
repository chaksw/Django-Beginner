<template>
    <h3>Component A</h3>
    <p>{{ message }}</p>
    <button @click="updateHandle">update data</button>
</template>

<script>
export default {
    data() {
        return {
            // 切换组件后组件会被销毁，再切换回来后组件会重新进行生命周期，所以会显示 old data
            message: "old data",
        };
    },
    methods: {
        updateHandle() {
            this.message = "new Data";
        },
    },
    // 在没有keep-alive情况下，每次切换组件后都会触发销毁流程
    beforeUnmount() {
        console.log("before component unmounted");
    },
    unmounted() {
        console.log("component unmounted");
    },
};
</script>
