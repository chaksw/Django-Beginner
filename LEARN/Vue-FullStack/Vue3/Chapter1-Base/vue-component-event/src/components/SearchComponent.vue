<template>
    Search :
    <input type="text" v-model="search" />
</template>
<script>
export default {
    data() {
        return {
            search: "",
        };
    },
    // listener
    watch: {
        search(newValue, oldValue) {
            this.$emit("searchEvent", newValue);
        },
    },
    components: {},
};
</script>
