<template>
    <h3>Component Lifecycle</h3>
    <p>{{ message }}</p>
    <button @click="clickHandle">Update</button>
</template>

<!-- 
    Lifecycle function
    创建期: beforeCreate    created
    挂载期: beforeMount     mounted
    更新期: beforeUpdate    updated
    销毁期: beforeUnmount   unmounted 
-->

<script>
export default {
    data() {
        return {
            message: "data",
        };
    },
    methods: {
        clickHandle() {
            this.message += " updated";
        },
    },
    beforeCreate() {
        console.log("before component created");
    },
    created() {
        console.log("component created");
    },
    beforeMount() {
        console.log("before component mounted");
    },
    mounted() {
        console.log("component mounted");
    },
    beforeUpdate() {
        console.log("before component updated");
    },
    updated() {
        console.log("component updated");
    },
    beforeUnmount() {
        console.log("before component unmounted");
    },
    unmounted() {
        console.log("component unmounted");
    },
};
</script>
