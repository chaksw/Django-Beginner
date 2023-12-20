<template>
    <h3>ComponentA</h3>
    <ComponentB :title="title" :age="age" :names="names" />
</template>
<script>
import ComponentB from "./ComponentB.vue";
export default {
    data() {
        return {
            title: "Test Title",
            age: 20,
            names: ["iwen", "amy", "frank"], // array
        };
    },
    components: {
        ComponentB,
    },
};
</script>
