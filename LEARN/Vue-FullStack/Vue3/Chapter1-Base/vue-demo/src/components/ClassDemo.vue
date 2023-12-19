<!-- Class Binding -->
<template>
    <p :class="{ active: isActive, 'text-danger': hasError }">
        Class Binding 1
    </p>
    <p :class="classObject">Class Binding 2</p>
    <p :class="[arrActive, arrHasError]">Class Binding 3</p>
    <p :class="[isActive ? 'active' : '', hasError ? 'text-danger' : '']">
        Class Binding 4
    </p>
    <p :class="[isActive ? 'active' : '', { 'text-danger': hasError }]">
        Class Binding 5
    </p>
</template>
<script>
import { isReactive } from "vue";

export default {
    data() {
        return {
            // 属性绑定布尔值, 条件渲染
            isActive: false,
            hasError: true,
            // 将属性创建为对象
            classObject: {
                active: true,
                "text-danger": true,
            },
            // 数组，非条件渲染
            arrActive: "active",
            arrHasError: "text-danger",
        };
    },
};
</script>

<style>
.active {
    font-size: 30px;
}
.text-danger {
    color: red;
}
</style>
