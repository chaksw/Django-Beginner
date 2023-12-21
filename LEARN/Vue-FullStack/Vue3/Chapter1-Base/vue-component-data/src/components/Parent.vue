<template>
    <h3>Parent</h3>
    <p>{{ globalData }}</p>

    <Child />
</template>
<script>
import Child from "./Child.vue";
export default {
    inject: ["globalData"],
    data() {
        return {};
    },
    components: {
        Child,
    },
};
</script>
