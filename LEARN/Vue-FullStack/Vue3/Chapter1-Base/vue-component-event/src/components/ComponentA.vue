<template>
    <h3>ComponentA</h3>
    <!-- 1. 传递带参函数给子组件 -->
    <ComponentB title="Title" :on-event="dataFn" />
    <p>{{ message }}</p>
</template>
<script>
import ComponentB from "./ComponentB.vue";
export default {
    data() {
        return {
            message: "",
        };
    },
    components: {
        ComponentB,
    },
    methods: {
        dataFn(data) {
            // 3. 接受参数数据
            this.message = data;
        },
    },
};
</script>
