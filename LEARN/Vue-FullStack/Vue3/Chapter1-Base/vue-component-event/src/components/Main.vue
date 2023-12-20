<template>
    <h3>Main</h3>
    <SearchComponent @search-event="getSearch" />
    <p>Search Result: {{ search }}</p>
</template>
<script>
import SearchComponent from "./SearchComponent.vue";
export default {
    data() {
        return { search: "" };
    },
    methods: {
        getSearch(data) {
            this.search = data;
        },
    },
    components: {
        SearchComponent,
    },
};
</script>
