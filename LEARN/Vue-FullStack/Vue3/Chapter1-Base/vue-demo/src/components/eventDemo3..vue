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
        addCount(e) {
            // using this to refer variable in data()
            this.count++;
            // Event object in vue is the original JS object
            console.log((e.target.innerHTML = "Add " + this.count));
        },
    },
};
</script>
