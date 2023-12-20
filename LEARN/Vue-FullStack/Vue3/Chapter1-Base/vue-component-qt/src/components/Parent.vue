<template>
    <h3>Parent</h3>
    <!-- Transfer data (title) to child vue -->
    <Child
        title="Parent Data"
        demo="data"
        :dynamic="message"
        :age="age"
        :names="names"
        :userInfo="userInfo" />
</template>
<script>
import Child from "./Child.vue";
export default {
    data() {
        return {
            // dynamic data
            message: "Dynamic Data",
            age: 20, // number
            names: ["iwen", "amy", "frank"], // array
            userInfo: {
                // object
                name: "iwen",
                age: 20,
            },
        };
    },
    components: {
        Child,
    },
};
</script>
