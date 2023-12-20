<template>
    <h3>Child</h3>
    <button @click="clickEventHandle">Transfer data</button>
</template>
<script>
export default {
    data() {
        return {
            msg: "Child data!",
        };
    },
    methods: {
        clickEventHandle() {
            // use $emit to declarate component event, where 2 argument accepted, first for listener name in parent component (camelCase), second for data to transfer
            this.$emit("someEvent", this.msg);
        },
    },
};
</script>
