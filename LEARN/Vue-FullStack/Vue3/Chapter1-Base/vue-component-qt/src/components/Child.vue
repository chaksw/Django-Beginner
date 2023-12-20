<template>
    <h3>Child</h3>
    <!-- use data by template syntax -->
    <p>{{ title }}</p>
    <p>{{ demo }}</p>
    <p>{{ dynamic }}</p>
    <p>{{ age }}</p>
    <p>{{ names }}</p>
    <ul>
        <li v-for="(item, index) in names" :key="index">
            {{ item }} - {{ index }}
        </li>
    </ul>
    <p>{{ userInfo.name }}</p>
    <p>{{ userInfo.age }}</p>
</template>
<script>
export default {
    data() {
        return {};
    },
    // invoke data from Parent, format: string declaration ["string"]
    props: ["title", "demo", "dynamic", "age", "names", "userInfo"],
};
</script>
