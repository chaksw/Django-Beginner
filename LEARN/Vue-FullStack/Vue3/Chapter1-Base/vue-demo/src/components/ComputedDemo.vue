<template>
    <h3>{{ itbaizhan.name }}</h3>
    <p>{{ itbaizhanContent }}</p>
    <p>{{ itbaizhanContents() }}</p>
</template>

<script>
export default {
    data() {
        return {
            itbaizhan: {
                name: "BaizhanProgrammer",
                content: ["Front-end", "Java", "python"],
            },
        };
    },
    // Computed Property
    computed: {
        itbaizhanContent() {
            return this.itbaizhan.content.length > 0 ? "Yes" : "No";
        },
    },
    methods: {
        itbaizhanContents() {
            return this.itbaizhan.content.length > 0 ? "Yes" : "No";
        },
    },
};
</script>
