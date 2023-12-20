<template>
    <h3>ComponentB</h3>
    <p>{{ title }}</p>
    <!-- 实例化参数数据 -->
    <p>{{ onEvent("Transfer Data") }}</p>
</template>
<script>
export default {
    data() {
        return {};
    },
    components: {},
    props: {
        title: {
            type: String,
        },
        onEvent: Function,
    },
};
</script>
