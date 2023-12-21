<template>
    <h3>Child</h3>
    <p>{{ message }}</p>
    <p>{{ msg }}</p>
</template>
<script>
export default {
    inject: ["message"],
    data() {
        return {
            msg: this.message,
        };
    },
};
</script>
