<template>
    <h3>Watchers</h3>
    <p>{{ message }}</p>
    <button @click="updateHandle">Change data</button>
</template>
<script>
export default {
    data() {
        return {
            message: "Hello",
        };
    },
    methods: {
        updateHandle() {
            this.message += "World";
        },
    },
    watch: {
        // watch 函数名要与对应的响应式数据名相同
        message(newValue, oldValue) {
            // 数据发生变化时执行的逻辑
            console.log(newValue, oldValue);
        },
    },
};
</script>
