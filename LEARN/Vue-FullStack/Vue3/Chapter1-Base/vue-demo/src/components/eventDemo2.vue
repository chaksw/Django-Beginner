<template>
    <h3>Method event handler</h3>
    <button @click="addCount">Add</button>
    <p>Count is: {{ count }}</p>
</template>

<script>
export default {
    data() {
        return {
            count: 0,
        };
    },
    // All method and function placed here
    methods: {
        addCount() {
            // using this to refer variable in data()
            this.count += 1;
        },
    },
};
</script>
