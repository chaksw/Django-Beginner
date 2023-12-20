<template>
    <h3>ComponentB</h3>
    <p>{{ title }}</p>
    <p>{{ age }}</p>
    <p v-for="(item, index) in names" :key="index">{{ item }}</p>
</template>
<script>
export default {
    data() {
        return {};
    },
    // object format declaration
    props: {
        title: {
            String, // declarate data type
            required: true, // required data from parent
        },
        age: {
            type: Number,
            default: 0,
        },
        // 数组和字符串可以直接default，但是如果是数组和对象，必须通过工厂函数返回默认值
        names: {
            type: Array,
            default() {
                return ["null"];
            },
        },
    },
};
</script>
