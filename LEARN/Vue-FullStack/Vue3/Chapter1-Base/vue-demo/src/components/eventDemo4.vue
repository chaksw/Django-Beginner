<template>
    <h3>Passing Argument in Event Handler 1</h3>
    <button @click="addCount('hello')">Add</button>
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
        addCount(msg) {
            // using this to refer variable in data()
            this.count++;
            console.log(msg);
        },
    },
};
</script>
