<template>
    <h3>Inline event handler</h3>
    <button @click="count++">Add</button>
    <p>Count is: {{ count }}</p>
</template>

<script>
export default {
    data() {
        return {
            count: 0,
        };
    },
};
</script>
