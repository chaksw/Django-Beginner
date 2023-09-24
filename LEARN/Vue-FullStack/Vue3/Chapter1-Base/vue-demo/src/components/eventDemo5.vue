<template>
    <h3>Passing Argument in Event Handler 2</h3>
    <p
        @click="getNameHandler(item, $event)"
        v-for="(item, index) in names"
        :key="index">
        {{ item }}
    </p>
</template>

<script>
export default {
    data() {
        return {
            names: ["iwen", "ime", "frank"],
        };
    },
    // All method and function placed here
    methods: {
        getNameHandler(name, e) {
            // using this to refer variable in data()
            console.log(name);
            console.log(e);
        },
    },
};
</script>
