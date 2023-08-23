<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Plans</h1>
            </div>

            <div class="column is-4">
                <p>Thank you for scbscribing to a plan !</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Plans",
    data() {
        return {};
    },
    mounted() {},
    methods: {
        async subscribe(type) {
            this.$store.commit("setIsLoading", true);
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
