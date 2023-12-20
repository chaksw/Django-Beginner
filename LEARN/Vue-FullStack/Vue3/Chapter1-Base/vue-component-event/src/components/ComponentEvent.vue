<template>
    <h3>Component Event</h3>
    <!-- listener (kebab-case) -->
    <Child @some-event="getHandle" />
    <p>{{ message }}</p>
</template>
<script>
import Child from "./Child.vue";
export default {
    data() {
        return {
            message: "",
        };
    },
    components: {
        Child,
    },
    methods: {
        // listener event, here argument link to data from $emit
        getHandle(data) {
            console.log("triggle child event", data);
            this.message = data;
        },
    },
};
</script>
